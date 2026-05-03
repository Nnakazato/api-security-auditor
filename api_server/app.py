from __future__ import annotations

import time
from collections import defaultdict
from flask import Flask, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

USERS = {
    "alice": generate_password_hash("CorrectHorseBatteryStaple!23")
}
FAILED_ATTEMPTS: dict[str, list[float]] = defaultdict(list)
RATE_LIMIT_WINDOW_SECONDS = 60
MAX_FAILED_ATTEMPTS = 5


def too_many_failed_attempts(username: str) -> bool:
    now = time.time()
    FAILED_ATTEMPTS[username] = [
        ts for ts in FAILED_ATTEMPTS[username]
        if now - ts <= RATE_LIMIT_WINDOW_SECONDS
    ]
    return len(FAILED_ATTEMPTS[username]) >= MAX_FAILED_ATTEMPTS


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/login-secure")
def login_secure():
    data = request.get_json(silent=True) or {}
    username = str(data.get("username", ""))[:64]
    password = str(data.get("password", ""))[:128]

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400

    if too_many_failed_attempts(username):
        return jsonify({"error": "too many failed attempts"}), 429

    stored_hash = USERS.get(username)
    if stored_hash and check_password_hash(stored_hash, password):
        FAILED_ATTEMPTS[username] = []
        return jsonify({"status": "login accepted"})

    FAILED_ATTEMPTS[username].append(time.time())
    return jsonify({"error": "invalid credentials"}), 401


@app.post("/login-vulnerable")
def login_vulnerable():
    data = request.get_json(silent=True) or {}
    username = str(data.get("username", ""))
    password = str(data.get("password", ""))

    # Intentionally vulnerable simulation for local lab testing only.
    if "' OR '1'='1" in username or "' OR '1'='1" in password:
        return jsonify({
            "status": "login accepted",
            "warning": "simulated SQL injection bypass"
        })

    if username == "alice" and password == "CorrectHorseBatteryStaple!23":
        return jsonify({"status": "login accepted"})

    # Intentionally leaks implementation-style error details.
    return jsonify({"error": "sqlite auth query returned 0 rows for users table"}), 401


@app.get("/public-data")
def public_data():
    return jsonify({"message": "public demo endpoint"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

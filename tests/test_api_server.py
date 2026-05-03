from api_server.app import app


def test_secure_login_happy_path():
    client = app.test_client()
    response = client.post("/login-secure", json={
        "username": "alice",
        "password": "CorrectHorseBatteryStaple!23",
    })
    assert response.status_code == 200


def test_secure_login_missing_fields_negative():
    client = app.test_client()
    response = client.post("/login-secure", json={})
    assert response.status_code == 400

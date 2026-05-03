from scanner.analyzer import analyze_response


def test_sql_injection_probe_detects_bypass():
    result = analyze_response("sql_injection_probe", 200, "login accepted")
    assert result["passed"] is False
    assert result["severity"] == "high"


def test_error_leakage_detects_database_terms():
    result = analyze_response("error_leakage_probe", 401, "sqlite users table error")
    assert result["passed"] is False
    assert result["severity"] == "medium"


def test_rate_limit_requires_429():
    result = analyze_response("rate_limit_probe", 401, "invalid credentials")
    assert result["passed"] is False

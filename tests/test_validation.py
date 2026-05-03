import pytest
from scanner.main import validate_base_url


def test_valid_base_url():
    assert validate_base_url("http://localhost:5001") == "http://localhost:5001"


def test_invalid_base_url_rejected():
    with pytest.raises(ValueError):
        validate_base_url("not-a-url")

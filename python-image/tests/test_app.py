import json
import logging

from fastapi.testclient import TestClient

from app import JsonFormatter, app as fastapi_app

client = TestClient(fastapi_app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_info_endpoint():
    response = client.get("/info")
    assert response.status_code == 200
    body = response.json()
    assert "app_env" in body
    assert "cwd" in body


def test_json_formatter_produces_valid_json():
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg="hello %s",
        args=("world",),
        exc_info=None,
    )
    payload = json.loads(JsonFormatter().format(record))
    assert payload["message"] == "hello world"
    assert payload["level"] == "INFO"
    assert payload["logger"] == "test"
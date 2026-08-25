from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings

client = TestClient(app)

def test_create_log_requires_auth():
    response = client.post("/logs", json={"source": "test", "message": "test message"})
    assert response.status_code == 401

def test_create_log_with_auth():
    response = client.post(
        "/logs",
        json={"source": "test", "message": "test message"},
        auth=(settings.api_username, settings.api_password),
    )
    assert response.status_code == 200
    assert response.json()["source"] == "test"
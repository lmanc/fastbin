from fastapi.testclient import TestClient

from app.main import app


def test_get():
    client = TestClient(app)
    response = client.get("/get")
    assert response.status_code == 200
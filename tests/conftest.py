import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Provide a pre-configured `TestClient`."""
    return TestClient(app, client=('127.0.0.1', 50000))

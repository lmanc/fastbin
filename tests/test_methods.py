from fastapi import status

from app.api.core import CoreResponse


def test_get(client):
    """Test /get endpoint."""
    response = client.get('/get')

    assert response.status_code == status.HTTP_200_OK
    assert CoreResponse.model_validate(response.json())

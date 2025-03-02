from fastapi import status

from app.api.core import HeadersResponse


def test_headers(client):
    """Test `headers` endpoint."""
    response = client.get('/headers')

    assert response.status_code == status.HTTP_200_OK
    assert HeadersResponse.model_validate(response.json())

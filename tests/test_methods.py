def test_get(client):
    response = client.get('/get')
    assert response.status_code == 200

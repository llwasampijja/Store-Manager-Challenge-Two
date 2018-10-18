import pytest
def test_index(client, auth):
    response = client.get('/')
    # assert b"Log In" in response.data
    # assert b"Register" in response.data
    assert response.status_code == 200
    assert client.get("/wrong-endpoint").status_code == 403
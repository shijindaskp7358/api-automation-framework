from  utils.api_client import APIClient

def test_get_single_user(api_client):

    response = api_client.get("users/2")

    assert response.status_code == 200
    json_data = response.json()
    assert json_data["id"] == 2
    assert "email" in json_data
    assert "name" in json_data
    assert "username" in json_data

def test_get_invalid_user(api_client):

    response = api_client.get("users/9999")

    assert response.status_code == 404
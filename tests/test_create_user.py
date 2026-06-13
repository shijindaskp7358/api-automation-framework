import pytest

def test_create_single_user(api_client):
    payload = {
        "name": "Shijin",
        "username": "shijindas",
        "email": "shijindaskp@gmail.com"
    }
    response = api_client.post("users",payload)

    assert response.status_code == 201
    json_data = response.json()
    assert json_data["name"] == "Shijin"
    assert json_data["email"] == "shijindaskp@gmail.com"
    assert "id" in json_data

    
@pytest.mark.parametrize("name,username,email",[
        ("shijindas","shijin","shijindaskp@gmail.con"),
        ("anurag","anu234","anurag@test.com"),
        ("vishnu","vishnu234","vshnu@test.com")
    ])
    
def test__create_multiple_user(api_client,name,username,email):

        payload = {
            "name": name,
            "username": username,
            "email": email
        }

        response = api_client.post("users",payload)

        assert response.status_code == 201
        json_data = response.json()
        assert json_data["name"] == name
        assert "id" in json_data
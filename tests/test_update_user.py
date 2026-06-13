
def test_upadate_user(api_client):

    payload = {
        "name" : "Shijin updated",
        "email" : "shijindaskp@updated.com" }
    response = api_client.put("users/2",payload)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["name"] == "Shijin updated"
    
def test_update_invalid_user(api_client):


    payload = {
        "name": "wrong"
    }
    response = api_client.put("users/9999",payload)

    assert response.status_code in [404,500]


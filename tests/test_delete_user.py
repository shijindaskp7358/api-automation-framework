
def test_delete_user(api_client):
    

    response = api_client.delete("users/2")
    
    assert response.status_code == 200

def test_delete_invalid_user(api_client):

    response = api_client.delete("users/9999")

    assert response.status_code in  [404,200]
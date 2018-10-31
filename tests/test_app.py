
def test_return_200_on_root(client):
    """ Return status code 200 on root url"""
    response = client.get('/')
    assert response.status_code == 200


def test_unique_generated_uuid(client):
    response = client.post('/create-pingout')
    uuid_1 = response.json['uuid']  

    response = client.post('/create-pingout')  
    uuid_2 = response.json['uuid']
    
    assert uuid_1 != uuid_2
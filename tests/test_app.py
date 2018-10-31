
def test_return_200_on_root(client):
    """ Return status code 200 on root url"""
    response = client.get('/')
    assert response.status_code == 200


def test_unique_generated_uuid(client):
    response = client.post('/create-pingout')
    uuid_1 = response.json['uuid']  
    assert response.status_code == 201

    response = client.post('/create-pingout')  
    uuid_2 = response.json['uuid']
    assert response.status_code == 201

    assert uuid_1 != uuid_2


def test_ping_to_valid_pingout_uuid(client):
    response = client.post('/create-pingout')
    uuid = response.json['uuid']
    client.post(f'/{uuid}/ping')
    response = client.get(f'/{uuid}')
    assert response.status_code == 200


def test_ping_to_invalid_pingout_uuid(client):
    invalid_uuid = '84b9cfd3b8124023b8be4d43720d179a'
    response = client.get(f'/{invalid_uuid}')
    assert response.status_code == 404


def test_filtered_pings(client):
    response = client.post('/create-pingout')
    uuid = response.json['uuid']

    response = client.get(f'/{uuid}/filter/?initial_date=&final')
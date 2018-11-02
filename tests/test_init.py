import pytest
import requests
import json
from uuid import uuid4
from dateutil import parser
import datetime
from dateutil import parser

def test_create_pingoiut_error(client):
    response = client.get('/create-pingout')
    
    assert response.status_code == 405

def test_get_pingouts_occur_range_date_error_404():
    uuid = uuid4()
    response = requests.get('http://0.0.0.0:5000/{}/filter'.format(uuid.hex))
    assert response.status_code == 404

def test_get_pingouts_occur_range_date_invalid_uuid(client):
    invalid_uuid = '84b9cfd3b8124023b8be4d43720d179a'
    response = client.get(f'/{invalid_uuid}/filter')
    assert response.status_code == 404


def test_get_pingouts_occur_range_date_valid_uuid_typer_error(client):
    response = client.post('/create-pingout')
    uuid = response.json['uuid']  
    response = client.get(f'/{uuid}/filter/?initial_date=2018-01-01&final_date=2018-02-02')

    response = client.post('/create-pingout')
    uuid_1 = response.json['uuid']  
    response = client.get(f'/{uuid_1}/filter')

    assert response.status_code == 400


def test_get_pingouts_occur_range_date(client, db_collection):
    response = client.post('/create-pingout')
    uuid = response.json['uuid']  
    response = client.get(f'/{uuid}/filter?initial_date=2018-01-01&final_date=2018-02-02')
    date = datetime.datetime.today().replace(second=0,
                                             microsecond=0)
    db_collection.insert_one({'uuid': uuid, 'pings': [{'count': 1, "date": date}]})
     
    assert response.status_code == 500
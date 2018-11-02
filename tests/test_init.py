import pytest
import requests
import json
from uuid import uuid4

def test_create_pingout():
    response = requests.get('http://0.0.0.0:5000/create-pingout')

    assert response.status_code == 405

def test_get_pingouts_occur_range_date_error_404():
    uuid = uuid4()

    response = requests.get('http://0.0.0.0:5000/{}/filter'.format(uuid.hex))

    assert response.status_code == 404

"""
def test_get_pingouts_occur_range_date_error_type():
    response = requests.post('http://0.0.0.0:5000/create-pingout')

    data = json.loads(response.text)

    payload = {'initial_date': '2018-11-01', 'final_date': '2018-11-02'}

    response = requests.get('http://0.0.0.0:5000/{}/filter'.format(data['uuid']), params=payload)

    assert response.status_code == 400
"""

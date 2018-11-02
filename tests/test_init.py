import pytest
import requests

def test_create_pingout():
    response = requests.get('http://0.0.0.0:5000/create-pingout')

    assert response.status_code == 405

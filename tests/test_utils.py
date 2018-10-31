import pytest
from pingout.utils import validate_uuid, from_json_to_csv
from uuid import uuid4


def test_validate_uuid():
    invalid_uuid = "INVALID"
    res = validate_uuid(invalid_uuid)
    assert res == False

    valid_uuid = "84b9cfd3b8124023b8be4d43720d179a"
    res = validate_uuid(valid_uuid)
    assert res == True

def test_convert_json_to_csv():
    json = {"CleberLixo": {"nome": "ASDADSADS", "id": 12123, "telefone":"997446446", "endereco":"iasjddjsaisd"},
            "IgorLixo": {"nome": "ASDADSADS", "id": 12123, "telefone":"997446446", "endereco":"iasjddjsaisd"},
            "RodrigoLixo": {"nome": "ASDADSADS", "id": 12123, "telefone":"997446446", "endereco":"iasjddjsaisd"}}
    from_json_to_csv(json,"testeConvert")
    assert True
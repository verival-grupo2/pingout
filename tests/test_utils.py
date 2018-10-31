import pytest
from pingout.utils import validate_uuid
from uuid import uuid4


def test_validate_uuid():
    invalid_uuid = "INVALID"
    res = validate_uuid(invalid_uuid)
    assert res == False

    valid_uuid = "84b9cfd3b8124023b8be4d43720d179a"
    res = validate_uuid(valid_uuid)
    assert res == True    
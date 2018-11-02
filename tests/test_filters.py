import pytest
import datetime
from dateutil import parser
from uuid import uuid4
from pingout.filters import filter_pings_range_of_dates


def test_filter_pings_range_of_dates(db_collection):
    uuid = uuid4()
    date = datetime.datetime.today().replace(second=0,
                                             microsecond=0)
    db_collection.insert_one({'uuid': uuid.hex, 'pings': [{'count': 1, "date": date}]})
    
    initial = parser.parse('-'.join([str(date.year), str(date.month), str(date.day)]))
    final = parser.parse('-'.join([str(date.year), str(date.month), str(date.day)]))
    
    test = filter_pings_range_of_dates(uuid.hex, db_collection, initial, final)
    assert test == [{'count': 1, "date": date.date()}]

def test_filter_pings_range_of_dates_error(db_collection):
    uuid = uuid4()
    date = datetime.datetime.today().replace(second=0,
                                             microsecond=0)
    db_collection.insert_one({'uuid': uuid.hex, 'pings': [{'count': 1, "date": date}]})
    
    initial = '-'.join([str(date.year), str(date.month), str(date.day)])
    final = '-'.join([str(date.year), str(date.month), str(date.day)])
    
    with pytest.raises(ValueError) as excinfo:
        filter_pings_range_of_dates(uuid.hex, db_collection, initial, final)
    assert 'Invalid date type' in str(excinfo.value)
import json, pytest
from models.customer import Customer
from decoder.customer_decoder import CustomerDecoder


def test_customer_decoder_json():
    line = '{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}'
    obj = json.loads(line, cls=CustomerDecoder)
    assert type(obj) == Customer

def test_customer_decoder_json_key_error_latitude():
    line = '{"latituxasdde": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}'
    with pytest.raises(KeyError):
        obj = json.loads(line, cls=CustomerDecoder)

def test_customer_decoder_json_key_error_user_id():
    line = '{"latitude": "52.986375", "user_xid": 12, "name": "Christina McArdle", "longitude": "-6.043701"}'
    with pytest.raises(KeyError):
        obj = json.loads(line, cls=CustomerDecoder)

def test_customer_decoder_json_key_error_name():
    line = '{"latitude": "52.986375", "user_id": 12, "namxe": "Christina McArdle", "longitude": "-6.043701"}'
    with pytest.raises(KeyError):
        obj = json.loads(line, cls=CustomerDecoder)


def test_customer_decoder_json_key_error_longitude():
    line = '{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longixtude": "-6.043701"}'
    with pytest.raises(KeyError):
        obj = json.loads(line, cls=CustomerDecoder)
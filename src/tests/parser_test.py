import pytest
from core.parser import Parser
from models.customer import Customer
from decoder.customer_decoder import CustomerDecoder

@pytest.fixture
def customers():
    file_path = './test_customer.json'
    parser = Parser()
    data = parser.parsing(file_path=file_path, decoder=CustomerDecoder)
    yield data

def test_parsed_file_length(customers):
    assert len(customers) == 32

def test_parsed_customer_one_user_id(customers):
    assert customers[0].user_id == 12

def test_parsed_customer_one_name(customers):
    assert customers[0].name == 'Christina McArdle'

def test_parsed_customer_latitude(customers):
    assert customers[0].location.latitude == 52.986375

def test_parsed_customer_longitude(customers):
    assert customers[0].location.longitude == -6.043701

def test_parsed_json_to_object(customers):
    for customer in customers:
        if type(customer) != Customer:
            assert False
    assert True

def test_parsed_missing_file():
    with pytest.raises(Exception):
        file_path = '../missing_file'
        parser = Parser()
        data = parser.parsing(file_path=file_path, decoder=CustomerDecoder)



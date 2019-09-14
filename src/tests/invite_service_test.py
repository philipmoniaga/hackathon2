import pytest
from core.parser import Parser
from decoder.customer_decoder import CustomerDecoder
from service.invite_service import InviteService
from core.distance_strategy import DistanceStrategy
from constants import FILE_NAME, GLOBAL_CIRCLE_DISTANCE


@pytest.fixture
def invitees():
    strategy = DistanceStrategy(GLOBAL_CIRCLE_DISTANCE)
    service = InviteService(distance_estimator=strategy)
    file_path = './test_customer.json'
    parser = Parser()
    data = parser.parsing(file_path=file_path, decoder=CustomerDecoder)
    result =  service.calculate(data)
    yield result

@pytest.fixture
def invitees_zero():
    strategy = DistanceStrategy(GLOBAL_CIRCLE_DISTANCE)
    service = InviteService(distance_estimator=strategy)
    file_path = './test_invite_zero.json'
    parser = Parser()
    data = parser.parsing(file_path=file_path, decoder=CustomerDecoder)
    result =  service.calculate(data)
    yield result

def test_invitees_arr_length(invitees):
    assert len(invitees) == 16

def test_invitees_user_ids(invitees):
    user_ids = []
    for invitee in invitees:
        user_ids.append(invitee.user_id)
    assert sorted(user_ids) == [4,5,6,8,11,12,13,15,17,23,24,26,29,30,31,39]


def test_invitees_length_zero(invitees_zero):
    assert len(invitees_zero) == 0
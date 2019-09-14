import pytest, math
from models.point import Point
from core.global_circle_distance import GlobalCircleDistance
from constants import DUBLIN_OFFICE_LOCATION


def test_global_circle_distance():
    AMS = Point(52.3667, 4.8945)
    distance = GlobalCircleDistance()
    r = distance.estimate(AMS, DUBLIN_OFFICE_LOCATION)
    assert r == pytest.approx(755, 1)

def test_distance_to_self():
    distance = GlobalCircleDistance()
    r = distance.estimate(DUBLIN_OFFICE_LOCATION, DUBLIN_OFFICE_LOCATION)
    assert r == pytest.approx(0, 0.1)

def test_distance_different_order():
    AMS = Point(52.3667, 4.8945)
    distance = GlobalCircleDistance()
    r = distance.estimate(AMS, DUBLIN_OFFICE_LOCATION)
    r2 = distance.estimate(DUBLIN_OFFICE_LOCATION, AMS)
    assert r == pytest.approx(r2, 0.001)

def test_convert_to_radian():
    distance = GlobalCircleDistance()
    assert (math.pi / 2) == distance.deg_to_rad(90)

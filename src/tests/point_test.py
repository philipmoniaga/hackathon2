import pytest
from models.point import Point

def test_point_latitude_out_of_bounds_max():
    with pytest.raises(ValueError):
        p = Point(91, 0)

def test_point_latitude_out_of_bounds_min():
    with pytest.raises(ValueError):
        p = Point(-91, 0)

def test_point_longitude_out_of_bounds_max():
    with pytest.raises(ValueError):
        p = Point(0, 181)

def test_point_longitude_out_of_bounds_min():
    with pytest.raises(ValueError):
        p = Point(0, -181)

def test_point_latitude_type():
    with pytest.raises(Exception):
        p = Point("0", 90)

def test_point_longitude_type():
    with pytest.raises(Exception):
        p = Point(0, "90")
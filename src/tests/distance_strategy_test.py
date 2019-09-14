from core.distance_strategy import DistanceStrategy
from core.global_circle_distance import GlobalCircleDistance
from constants import GLOBAL_CIRCLE_DISTANCE


def test_distance_strategy_global_circle_distance():
    distance = DistanceStrategy(GLOBAL_CIRCLE_DISTANCE)
    assert type(distance.strategy) == GlobalCircleDistance

def test_distance_strategy_default():
    distance = DistanceStrategy(None)
    assert type(distance.strategy) == GlobalCircleDistance

from .global_circle_distance import GlobalCircleDistance
from constants import GLOBAL_CIRCLE_DISTANCE


class DistanceStrategy(object):
    def __init__(self, estimator_type):
        if estimator_type == GLOBAL_CIRCLE_DISTANCE:
            self.strategy = GlobalCircleDistance()
        else:  # default global distance
            self.strategy = GlobalCircleDistance()

    def estimate(self, source, target):
        """Return a float
        Calculate the distance between two points depends on the strategy
        """
        return self.strategy.estimate(source, target)

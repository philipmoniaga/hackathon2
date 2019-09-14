
from math import sin, cos, sqrt, atan2, pi
from constants import EARTH_MEAN_RADIUS


class GlobalCircleDistance(object):

    def estimate(self, a, b):
        """
        Return a float
        Calculate between two points in a sphere in Km
        """
        lat1, lng1 = self.deg_to_rad(degrees=a.latitude), self.deg_to_rad(degrees=a.longitude)  # NOQA
        lat2, lng2 = self.deg_to_rad(degrees=b.latitude), self.deg_to_rad(degrees=b.longitude)  # NOQA

        sin_lat1, cos_lat1 = sin(lat1), cos(lat1)
        sin_lat2, cos_lat2 = sin(lat2), cos(lat2)

        delta_lng = lng2 - lng1
        cos_delta_lng, sin_delta_lng = cos(delta_lng), sin(delta_lng)

        d = atan2(sqrt((cos_lat2 * sin_delta_lng) ** 2 +
                       (cos_lat1 * sin_lat2 -
                        sin_lat1 * cos_lat2 * cos_delta_lng) ** 2),
                  sin_lat1 * sin_lat2 + cos_lat1 * cos_lat2 * cos_delta_lng)
        return EARTH_MEAN_RADIUS * d

    def deg_to_rad(self, degrees):
        """
        Convert degree to radians
        """
        return degrees * (pi / 180)

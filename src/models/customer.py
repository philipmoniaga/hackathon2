from .point import Point


class Customer(object):

    def __init__(self, user_id, latitude, longitude, name):
        self.user_id = user_id
        self.location = Point(float(latitude), float(longitude))
        self.name = name

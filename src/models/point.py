
class Point:
    def __init__(self, latitude, longitude):

        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude must between 90 and -90 degrees")

        if longitude < -180 or longitude > 180:
            raise ValueError("Longitude must between -180 and 180 degrees")

        try:
            self.latitude = latitude
            self.longitude = longitude
        except TypeError:
            raise Exception("Type error must be number")

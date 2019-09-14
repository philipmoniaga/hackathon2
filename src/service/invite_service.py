from constants import DUBLIN_OFFICE_LOCATION


class InviteService(object):

    def __init__(self, distance_estimator):
        self.distance_estimator = distance_estimator

    def calculate(self, customers):
        invitees = []
        target = DUBLIN_OFFICE_LOCATION
        for customer in customers:
            distance = self.distance_estimator.estimate(customer.location, target)  # NOQA
            if distance <= 100.0:
                invitees.append(customer)
        invitees = sorted(
                invitees, key=lambda cust: cust.user_id)
        return invitees

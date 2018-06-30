"""rides class"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from api.validation import validate


class rides():
    all_rides = []

    def __init__(self, ride_id, from_where, to, time, date, cost):
        self.ride_id = ride_id
        self.from_where = from_where
        self.to = to
        self.time = time
        self.date = date
        self.cost = cost

    def creating_ride(self):
        """method for creating a ride offer"""
        create_ride = {}
        data = rides(self.ride_id, self.from_where, self.to,
                     self.time, self.date, self.time)
        if validate.validate_empty(data):
            return "all inputs must be filled"
        elif validate.validate_id(rides.all_rides, data.ride_id):
            return "ID has already been used"
        elif validate.validate_ride(rides.all_rides, data):
            return "Ride was already created"
        else:
            create_ride = data.__dict__
            rides.all_rides.append(create_ride)
            return"Ride has been created"

    @classmethod
    def display_rides(cls):
        """method for displaying all ride offers"""
        return rides.all_rides

    @classmethod
    def getone_ride(cls, data):
        """method for getting a single ride offer"""
        result = "Invalid ID, use a valid one"
        for ride_info in rides.all_rides:
            if ride_info['ride_id'] == data:
                result = ride_info
        return result

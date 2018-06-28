import sys
import os
sys.path.append(os.path.pardir)
from api.Validation import Validate


class Rides():
    all_rides = []

    def __init__(self, Id, From, to, time, date, cost):
        self.create_ride = {}
        self.Id = Id
        self.From = From
        self.to = to
        self.time = time
        self.date = date
        self.cost = cost

    def creating_ride(self):
        """method for creating a ride offer"""
        self.create_ride["From"] = self.From
        self.create_ride["Id"] = self.Id
        self.create_ride["to"] = self.to
        self.create_ride["time"] = self.time
        self.create_ride["date"] = self.date
        self.create_ride["cost"] = self.cost
        if(self.create_ride['From'] == "" or self.create_ride['to'] == ""or
           self.create_ride['date'] == ""or
           self.create_ride['time'] == "" or self.create_ride['Id'] == ""or
           self.create_ride['cost'] == ""):
            return "all inputs must be filled"
        elif Validate.validate_id(Rides.all_rides, self.create_ride["Id"]):
            return "ID has already been used"
        elif Validate.validate_ride(Rides.all_rides, self.create_ride):
            return "Ride was already created"
        else:
            Rides.all_rides.append(self.create_ride)
            self.create_ride = {}
            return"Ride has been created"

    @classmethod
    def display_rides(cls):
        """method for displaying all ride offers"""
        return Rides.all_rides

    @classmethod
    def getone_ride(cls, data):
        """method for getting a single ride offer"""
        result = "Invalid ID, use a valid one"
        for ride_info in Rides.all_rides:
            if ride_info['Id'] == data:
                result = ride_info
        return result

    @classmethod
    def request_ride(cls, data):
        """method for requesting a ride offer"""
        result = "Invalid id"
        for ride_info in Rides.all_rides:
            if ride_info["Id"] == data:
                result = ("you have requested to join the ride from",
                          ride_info['From'], "to", ride_info["to"],
                          "at", ride_info['time'], "on", ride_info["date"])
        return result

"""API class"""
from flask import request, jsonify
from flask_restful import Resource
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from app.api.ride import Rides


class Create_A_Ride(Resource):
    """class where a user creates a ride"""
    @classmethod
    def post(cls):
        """ a user can create a ride here """
        data = request.get_json()
        ride = Rides(data["Id"], data["From"], data["to"],
                     data["time"], data["date"], data["cost"])
        info = ride.creating_ride()
        response = jsonify(info)
        response.status_code = 201
        return response


class Get_All_Rides(Resource):
    """class for getting all available rides"""
    @classmethod
    def get(cls):
        """ a method to view all ride offers """
        result = Rides.display_rides()
        return result


class Get_A_Ride(Resource):
    """class for getting a specific ride"""
    @classmethod
    def get(cls, ride_id):
        """ a user can view info  for a specific ride here """
        result = Rides.getone_ride(ride_id)
        return jsonify({"result": result})


class Request_A_Ride(Resource):
    """class for requesting a ride"""
    @classmethod
    def post(cls, _id):
        """ a user can request for a specific ride here """
        result = "Invalid id"
        data = request.get_json()
        result = Rides.request_ride(data['Id'])
        return jsonify({"result": result})

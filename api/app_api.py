"""API class"""
from flask import request, jsonify
from flask_restful import Resource
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from api.ride import rides
from api.request import requestClass


class createARide(Resource):
    """class where a user creates a ride"""
    @classmethod
    def post(cls):
        """ a user can create a ride here """
        data = request.get_json()
        ride = rides(data["ride_id"], data["from_where"], data["to"],
                     data["time"], data["date"], data["cost"])
        info = ride.creating_ride()
        response = jsonify(info)
        response.status_code = 201
        return response


class getAllRides(Resource):
    """class for getting all available rides"""
    @classmethod
    def get(cls):
        """ a method to view all ride offers """
        result = rides.display_rides()
        return result


class getRide(Resource):
    """class for getting a specific ride"""
    @classmethod
    def get(cls, ride_id):
        """ a user can view info  for a specific ride here """
        result = rides.getone_ride(ride_id)
        return jsonify({"result": result})


class requestARide(Resource):
    """class for requesting a ride"""
    @classmethod
    def post(cls, _id):
        """ a user can request for a specific ride here """
        result = "Invalid id"
        data = request.get_json()
        request_object=requestClass(data["ride_id"])
        result=request_object.request_ride()
        return jsonify({"result": result})

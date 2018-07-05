"""API class"""
from flask import request, jsonify
from flask_restful import Api,Resource
from flask_jwt_extended import (create_access_token,jwt_required,get_jwt_identity)

from app.models.ridedb import RidesConnection
from app.models.request import RequestClass
from app.models.userdata import UserData




class createARide(Resource):
    """class where a user creates a ride"""
    @classmethod
    def post(cls):
        data = request.get_json()
        driver = get_jwt_identity()
        obj = RidesConnection()
        result=obj.create_ride(data["ride_from"], data["ride_to"],
                     data["ride_date"], data["ride_time"], data["cost"], data["driver_id"])
        response = jsonify(result)
        response.status_code = 201
        return response


class getAllRides(Resource):
    """class for getting all available rides"""
    @classmethod
    def get(cls):
        obj = RidesConnection()
        result = obj.fetch_rides()
        return result


class getRide(Resource):
    """class for getting a specific ride"""
    @classmethod
    def get(cls, rideId):
        obj = RidesConnection()
        data = obj.single_ride(rideId)
        return jsonify({"result": data})


class requestARide(Resource):
    """class for requesting a ride"""
    @classmethod
    @jwt_required
    def post(cls):
        data = request.get_json()
        req = RequestClass()
        info = req.getdriver(data)
        driver = get_jwt_identity()
        user = int(driver[0])
        request_object = req.create_requests(data,user,info)
        return jsonify({"created request":request_object})

class createUser(Resource):
    """class where a user creates a ride"""
    @classmethod
    def post(cls):
        """ a user can create a ride here """
        data = request.get_json()
        obj  = UserData()
        result = obj.insert_into_users(data["firstname"], data["lastname"], data["username"],
                                    data["password"], data["gender"],data["contact"],
                                    data["country"], data["city"])
        response = jsonify(result)
        response.status_code = 201
        return response


class getAllUsers(Resource):
    """class for getting all available rides"""
    @classmethod
    @jwt_required
    def get(cls):
        """ a method to view all ride offers """
        obj = UserData()
        result = obj.fetch_users()
        return jsonify({"result":result})

class loginUser(Resource):
    @classmethod   
    def post(cls):
        data = request.get_json() 
        obj = UserData() 
        result = obj.login(data["username"], data["password"])
        response = jsonify(result)
        response.status_code = 201
        return response

class AllRequests(Resource):
    """class for getting all available rides"""
    @classmethod
    def get(cls,rideId):
        req = RequestClass()
        result = req.get_requests(rideId)
        return jsonify({"result":result})    

class Respond(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        req=RequestClass()
        result = req.request_status(data["status"], data["request_id"])
        response = jsonify(result)
        response.status_code = 201
        return response        





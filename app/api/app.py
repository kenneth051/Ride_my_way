"""API class"""
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from app.api.validation import ValidateUsers
from app.api.validaterides import ValidateRides
from app.models.ridedb import RidesConnection
from app.models.request import RequestClass
from app.models.userdata import UserData


class CreateARide(Resource):
    """class where a user creates a ride"""
    @classmethod
    @jwt_required
    def post(cls):
        """class for creating rides"""
        try:
            data = request.get_json()
            driver = get_jwt_identity()
            user = driver[0]
            valid = ValidateRides(data["ride_from"],data["ride_to"], data["ride_date"],
                                    data["ride_time"], data["cost"],user)
            info = valid.validate_empty()
            if info == True:
                obj = RidesConnection()
                result = obj.create_ride(data["ride_from"], data["ride_to"],
                                    data["ride_date"], data["ride_time"], data["cost"], user)
                return jsonify({"result": result})
            else:
                return jsonify({"result":info})
        except:
            return jsonify({"result": "check inputs"})           


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
        return jsonify({"result": result})


class GetRide(Resource):
    """class for getting a specific ride"""
    @classmethod
    @jwt_required
    def get(cls, rideid):
        """class for getting a ride"""
        obj = RidesConnection()
        data = obj.single_ride(rideid)
        return jsonify({"result": data})


class RequestARide(Resource):
    """class for requesting a ride"""
    @classmethod
    @jwt_required
    def post(cls, rideid):
        """method for requesting for a ride"""
        data = request.get_json()
        req = RequestClass()
        num = int(data["id"])
        info = req.getdriver(num)
        driver = get_jwt_identity()
        user = data = driver[0]
        request_object = req.create_requests(num, user, info)
        return jsonify({"created request":request_object})


class getRide(Resource):
    """class for getting a specific ride"""
    @classmethod
    @jwt_required
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
        try:
            data = request.get_json()
            obj  = UserData()
            valid = ValidateUsers(data["firstname"], data["lastname"], data["username"],
                                  data["password"], data["gender"],data["contact"],
                                  data["country"], data["city"])
            info = valid.validate_empty()
            if info == True:
                result = obj.insert_into_users(data["firstname"], data["lastname"],
                                               data["username"], data["password"],
                                               data["gender"], data["contact"],
                                               data["country"], data["city"])
                return result
            else:
                return info 
        except:
            return jsonify({"result":"Error with what your sending"})


class getAllUsers(Resource):
    """class for getting all available rides"""
    @classmethod
    @jwt_required
    def get(cls):
        """ a method to view all ride offers """
        obj = UserData()
        result = obj.fetch_users()
        return jsonify({"result":result})


class LoginUser(Resource):
    """class for logging in user"""
    @classmethod
    def post(cls):
        """method for logging in"""
        data = request.get_json()
        obj = UserData()
        info = obj.login(data["username"], data["password"])
        return info


class AllRequests(Resource):
    """class for getting all available requests rides"""
    @classmethod
    @jwt_required
    def get(cls, rideid):
        """method for getting requests"""
        req = RequestClass()
        result = req.get_requests(rideid)
        return jsonify({"result":result})


class Respond(Resource):
    """class for responding to rides"""
    @classmethod
    @jwt_required
    def post(cls):
        """method for responding to rides"""
        data = request.get_json()
        req = RequestClass()
        result = req.request_status(data["status"], data["request_id"])
        response = jsonify(result)
        response.status_code = 201
        return response

 
class loginUser(Resource):
    @classmethod   
    def post(cls):
        data = request.get_json() 
        obj = UserData() 
        result = obj.login(data["username"], data["password"])
        response = jsonify(result)
        response.status_code = 201
        return response  

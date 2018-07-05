"""API class"""
from flask import request, jsonify
from flask_restful import Api,Resource
from flask_jwt_extended import (create_access_token,jwt_required,get_jwt_identity)
from RideData import RidesConnection
from request import RequestClass
from userdata import UserData


class createARide(Resource):
    """class where a user creates a ride"""
    @classmethod
    @jwt_required
    def post(cls):
        data = request.get_json()
        driver = get_jwt_identity()
        obj=RidesConnection()
        data["driver_id"]=driver
        result=obj.createRide(data["ride_from"], data["ride_to"],
                     data["ride_date"], data["ride_time"], data["cost"], data["driver_id"])
        response = jsonify(result)
        response.status_code = 201
        return response


class getAllRides(Resource):
    """class for getting all available rides"""
    @classmethod
    def get(cls):
        obj=RidesConnection()
        result=obj.fetch_rides()
        return result


class getRide(Resource):
    """class for getting a specific ride"""
    @classmethod
    def get(cls, ride_id):
        obj=RidesConnection()
        data=obj.single_ride(ride_id)
        return jsonify({"result": data})


class requestARide(Resource):
    """class for requesting a ride"""
    @classmethod
    def post(cls, _id):
        data = request.get_json()
        req=RequestClass()
        info=req.getDriver(data)
        req.createRequests(data,user,info)

        request_object=requestClass(data["ride_id"])
        result=request_object.request_ride()
        return jsonify({"result": result})

class createUser(Resource):
    """class where a user creates a ride"""
    @classmethod
    def post(cls):
        """ a user can create a ride here """
        data = request.get_json()
        obj=UserData()
        result=obj.insertIntoUsers(data["firstname"],data["lastname"],data["username"],data["password"],data["gender"],data["contact"],data["country"],data["city"])
        response = jsonify(result)
        response.status_code = 201
        return response


class getAllUsers(Resource):
    """class for getting all available rides"""
    @classmethod
    @jwt_required
    def get(cls):
        """ a method to view all ride offers """
        obj=UserData()
        result=obj.fetchUsers()
        return jsonify({"result":result})

class OneUser(Resource):
    """class for getting all available rides"""
    @classmethod
    @jwt_required
    def get(cls,_id):
        d=Database()
        result=d.SingleUser(_id)
        return jsonify({"result":result})

class loginUser(Resource):
    @classmethod   
    def post(cls):
        data = request.get_json() 
        obj=UserData() 
        result=obj.login(data["username"],data["password"])
        return result





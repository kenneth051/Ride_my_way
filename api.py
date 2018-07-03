"""API class"""
from flask import request, jsonify
from flask_restful import Api,Resource

from flask_jwt_extended import (create_access_token,jwt_required,get_jwt_identity)
from ride import rides
from request import requestClass
from user import user


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

class createUser(Resource):
    """class where a user creates a ride"""
    @classmethod
    def post(cls):
        """ a user can create a ride here """
        data = request.get_json()
        creating_user = user(data["_id"], data["username"], data["firstname"],
                             data["lastname"], data["password"], data["sex"],
                             data["contact"], data["city"], data["country"])
        result = creating_user.create_user()
        response = jsonify(result)
        response.status_code = 201
        return response


class getAllUsers(Resource):
    """class for getting all available rides"""
    @classmethod
    @jwt_required
    def get(cls):
        """ a method to view all ride offers """
        #current_user = get_jwt_identity()
        result = user.user_list
        return result

class loginUser(Resource):
    @classmethod   
    def post(cls):
        data = request.get_json()  
        result="user doesnt exist,use valid credentials"
        for info in user.user_list:
            if info['username'] == data["username"] and info['password'] ==data["password"]:
                access_token = create_access_token(identity=info['_id'])
                result= jsonify({"access_token":access_token})
        return result





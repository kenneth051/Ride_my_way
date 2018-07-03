"""API class"""
from flask import request, jsonify
from flask_restful import Resource
from user import user


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
    def get(cls):
        """ a method to view all ride offers """
        result = user.user_list
        return result

class loginuser(Resource):
        @classmethod   
        def post(cls):
            data = request.get_json()
            user_login = user.login(data["username"],data["password"])
            return user_login
            

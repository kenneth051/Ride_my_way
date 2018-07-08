"""Initializing API files"""
from flask import Flask,jsonify
from flask_jwt_extended import (JWTManager)
from flask_cors import CORS
from flask_restful import Api
from app.api.app import GetRide, GetAllRides, CreateARide, RequestARide, LoginUser, CreateUser, GetAllUsers, AllRequests, Respond
APP = Flask(__name__)
APP.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(APP)
API = Api(APP)
API.add_resource(GetAllRides, "/API/v1/rides")
API.add_resource(GetRide, "/API/v1/ride/<int:rideId>")
API.add_resource(CreateARide, '/API/v1/users/rides')
API.add_resource(RequestARide, '/API/rides/<rideId>/requests')
API.add_resource(CreateUser, "/API/v1/auth/signup")
API.add_resource(GetAllUsers, "/API/v1/users")
API.add_resource(LoginUser, "/API/v1/auth/login")
API.add_resource(AllRequests, "/API/v1/users/rides/<rideId>/requests")
API.add_resource(Respond,"/users/rides/<rideId>/requests/<requestId>")

@APP.errorhandler(404)
def page_not_found(e):
    result = {"invalid":"PLEASE USE A VALID URL"}
    response = jsonify(result)
    response.status_code = 404
    return response
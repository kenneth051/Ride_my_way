"""Initializing API files"""
from flask import Flask
from flask_jwt_extended import (JWTManager)
from flask_restful import Api
from api import getRide,getAllRides,createARide,requestARide,loginUser,createUser,getAllUsers 
APP = Flask(__name__)

API = Api(APP)
APP.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(APP)

@APP.errorhandler(404)
def page_not_found(e):
    return "use a valid URL", 404

API.add_resource(getAllRides, "/API/v1/rides")
API.add_resource(getRide, "/API/v1/ride/<int:ride_id>")
API.add_resource(createARide, '/API/v1/create_ride')
API.add_resource(requestARide, '/API/v1/ride/<int:_id>/request')
API.add_resource(createUser, "/API/v1/register")
API.add_resource(getAllUsers, "/API/v1/users")
API.add_resource(loginUser, "/API/v1/login")
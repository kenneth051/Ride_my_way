"""Initializing API files"""
from flask import Flask
from flask_restful import Api
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from api.app_api import getRide, getAllRides, createARide, requestARide
APP = Flask(__name__)
API = Api(APP)


@APP.errorhandler(404)
def page_not_found(e):
    return "use a valid URL", 404

API.add_resource(getAllRides, "/API/v1/rides")
API.add_resource(getRide, "/API/v1/ride/<int:ride_id>")
API.add_resource(createARide, '/API/v1/create_ride')
API.add_resource(requestARide, '/API/v1/ride/<int:_id>/request')
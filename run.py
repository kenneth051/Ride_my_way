"""flask run class"""
from flask import Flask
from flask_restful import Api
import subprocess, sys, os
script_path = os.path.dirname(__file__)
src = os.path.join(script_path, '/APP/')
sys.path.append(src)
from app.api.app import Get_A_Ride, Get_All_Rides, Create_A_Ride, Request_A_Ride
APP = Flask(__name__)
API = Api(APP)


@APP.errorhandler(404)
def page_not_found(e):
    return "use a valid URL", 404

API.add_resource(Get_All_Rides, "/v1/rides")
API.add_resource(Get_A_Ride, "/v1/ride/<int:ride_id>")
API.add_resource(Create_A_Ride, '/v1/create_ride')
API.add_resource(Request_A_Ride, '/v1/ride/<int:_id>/request')

if __name__ == '__main__':
    APP.run(debug=True)

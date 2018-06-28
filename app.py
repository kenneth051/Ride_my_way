"""API class"""
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from ride import Rides
APP = Flask(__name__)
API = Api(APP)

class Create_A_Ride(Resource):
    """class where a user creates a ride"""
    @classmethod
    def post(cls):
        """ a user can create a ride here """
        data = request.get_json()
        ride=Rides(int(data["Id"]),data["From"],data["to"],
                    data["time"],data["date"],data["cost"])
        info=ride.creating_ride()
        response = jsonify(info)
        response.status_code = 201
        return response


class Get_All_Rides(Resource):
    """class for getting all available rides"""
    @classmethod
    def get(cls):
        """ a method to view all ride offers """
        result=Rides.display_rides()
        return result
class Get_A_Ride(Resource):
    """class for getting a specific ride"""
    @classmethod
    def get(cls, ride_id):
        """ a user can view info  for a specific ride here """
        result=Rides.getone_ride(ride_id)    
        return jsonify({"result":result})
class Request_A_Ride(Resource):
    """class for requesting a ride"""
    @classmethod
    def post(cls, _id):
        """ a user can request for a specific ride here """
        result = "Invalid id"
        data = request.get_json()
        result=Rides.request_ride(data['Id'])
        return jsonify({"result":result})
        
@APP.errorhandler(404)
def page_not_found(e):
    return "use a valid URL", 404

API.add_resource(Get_All_Rides, "/v1/rides")
API.add_resource(Get_A_Ride, "/v1/ride/<int:ride_id>")
API.add_resource(Create_A_Ride, '/v1/create_ride')
API.add_resource(Request_A_Ride, '/v1/ride/<int:_id>/request')

if __name__ == '__main__':
    APP.run(debug=True)

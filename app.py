"""API class"""
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
APP = Flask(__name__)
API = Api(APP)
global users
global rides
rides = []
users = []
class RegisterUser(Resource):
    """user register or creates an account"""
    @classmethod
    def post(cls):
        """ a user can create an account here """
        data = {}
        register = request.get_json()
        data['firstname'] = register['firstname']
        data['lastname'] = register['lastname']
        data['username'] = register['username']
        data['password'] = register['password']
        data['gender'] = register['gender']
        data["id"] = register["id"]
        for registered_user in users:
            if  registered_user['username'] == register['username']:
                return jsonify({"Error":"You are already registered"})
        users.append(data)
        data = "User has been registered"
        return jsonify({'result':users, "success":data})
class LoginUser(Resource):
    """class where a user logs in"""
    @classmethod
    def post(cls):
        """ a user can login here """
        login = request.get_json()
        username = login['username']
        password = login['password']
        data = "invalid username and password"
        for user_info in users:
            if user_info['username'] == username and user_info['password'] == password:
                data = username, "You are logged in now"
        return jsonify({"information":data})
class CreateARide(Resource):
    """class where a user creates a ride"""
    @classmethod
    def post(cls):
        """ a user can create a ride here """
        data = {}
        created_ride = request.get_json()
        data['From'] = created_ride['From']
        data['To'] = created_ride['To']
        data['Time'] = created_ride['Time']
        data['Date'] = created_ride['Date']
        data['Driver'] = created_ride['Driver']
        data['Cost'] = created_ride['Cost']
        data['rideID'] = created_ride['rideID']
        for ride_info in rides:
            if (ride_info['From'] == created_ride['From'] and
                    ride_info['To'] == created_ride['To']and
                    ride_info['Date'] == created_ride['Date']and
                    ride_info['Driver'] == created_ride['Driver']):
                return jsonify({"Error":"You already created the ride"})
        rides.append(data)
        data = "Ride has been created"
        return jsonify({'result':rides, "success":data})
class GETAllRides(Resource):
    """class for getting all available rides"""
    @classmethod
    def get(cls):
        """ a method view all ride offers """
        return rides
class GETRide(Resource):
    """class for getting a specific ride"""
    @classmethod
    def get(cls, ride_id):
        """ a user can view info  for a specific ride here """
        result = "Invalid id"
        for ride_info in rides:
            if ride_info['rideID'] == ride_id:
                result = ride_info
        return jsonify({"result":result})
class RequestRide(Resource):
    """class for requesting a ride"""
    @classmethod
    def post(cls, _id):
        """ a user can request for a specific ride here """
        result = "Invalid id"
        data = request.get_json()
        ride_id = data["rideID"]
        ride_id = _id
        for ride_info in rides:
            if ride_info['rideID'] == ride_id:
                result = ("you have requested to join the ride from",
                          ride_info['From'], "to", ride_info['To'], "at",
                          ride_info['Time'], "on", ride_info["Date"])
        return jsonify({"result":result})

API.add_resource(GETAllRides, "/v1/rides")
API.add_resource(GETRide, "/v1/ride/<int:ride_id>")
API.add_resource(CreateARide, '/v1/create_ride')
API.add_resource(RequestRide, '/v1/ride/<int:_id>/request')
API.add_resource(RegisterUser, "/v1/register")
API.add_resource(LoginUser, "/v1/login")

if __name__ == '__main__':
    APP.run(debug=True)

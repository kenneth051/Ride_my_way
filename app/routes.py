"""Initializing API files"""
from flask_restful import Api
class Routes():
    """class defining routes"""
    def initialize(self, APP):
        """method intializing the routes"""
        from api import GetRide, GetAllRides, CreateARide, RequestARide,\
        LoginUser, CreateUser, GetAllUsers, AllRequests, Respond
        api = Api(APP)
        api.add_resource(GetAllRides, "/API/v1/rides")
        api.add_resource(GetRide, "/API/v1/ride/<int:rideid>")
        api.add_resource(CreateARide, '/API/v1/users/rides')
        api.add_resource(RequestARide, '/API/rides/<rideid>/requests')
        api.add_resource(CreateUser, "/API/v1/auth/signup")
        api.add_resource(GetAllUsers, "/API/v1/users")
        api.add_resource(LoginUser, "/API/v1/auth/login")
        api.add_resource(AllRequests, "/API/v1/users/rides/<rideId>/requests")
        api.add_resource(Respond, "/users/rides/<rideId>/requests/<requestId>")

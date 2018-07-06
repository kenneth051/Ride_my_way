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
class Routes():
        
    def initialize(self,APP):
            
        from flask_restful import Api
        from app.api.api import getRide, getAllRides, createARide, requestARide, loginUser, createUser, getAllUsers, AllRequests, Respond

        API = Api(APP)

        API.add_resource(getAllRides, "/API/v1/rides")
        API.add_resource(getRide, "/API/v1/ride/<int:rideId>")
        API.add_resource(createARide, '/API/v1/users/rides')
        API.add_resource(requestARide, '/API/rides/<rideId>/requests')
        API.add_resource(createUser, "/API/v1/auth/signup")
        API.add_resource(getAllUsers, "/API/v1/users")
        API.add_resource(loginUser, "/API/v1/auth/login")
        API.add_resource(AllRequests, "/API/v1/users/rides/<rideId>/requests")
        API.add_resource(Respond,"/users/rides/<rideId>/requests/<requestId>")

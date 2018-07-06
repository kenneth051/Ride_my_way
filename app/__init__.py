<<<<<<< HEAD
from flask import Flask, current_app,jsonify
from flask_jwt_extended import (JWTManager)
from flask_restful import Api
from flask_cors import CORS
from one.routes import Routes
=======
from flask import Flask, current_app
from flask_jwt_extended import (JWTManager)
from flask_restful import Api
from flask_cors import CORS
from app.routes import Routes
>>>>>>> 04066aafaee1e0c8b07c1e61922780dcd9aca85d

APP = Flask(__name__)
APP.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(APP)
route=Routes()
route.initialize(APP)
<<<<<<< HEAD


@APP.errorhandler(404)
def page_not_found(e):
    result = {"invalid":"PLEASE USE A VALID URL"}
    response = jsonify(result)
    response.status_code = 404
    return response
=======
@APP.errorhandler(404)
def page_not_found(e):
    return "use a valid URL", 404
>>>>>>> 04066aafaee1e0c8b07c1e61922780dcd9aca85d

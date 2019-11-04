[![Coverage Status](https://coveralls.io/repos/github/kenneth051/Ride_my_way/badge.svg)](https://coveralls.io/github/kenneth051/Ride_my_way)

[![Maintainability](https://api.codeclimate.com/v1/badges/d738db88c1cfa7bd44d8/maintainability)](https://codeclimate.com/github/kenneth051/Ride_my_way/maintainability)

[![Build Status](https://travis-ci.org/kenneth051/Ride_my_way.svg?branch=dev)](https://travis-ci.org/kenneth051/Ride_my_way)


# Ride_my_way
repository for carpooling website
this is a repository about a carpooling website.i have upload the GUIs, API endpoints for challenge 2 and 3.
the feature of this website include

Signing up/ registeration

logging in

users get to create rides

users get to join rides

users get to reject of approve rides


i have so far used html, css and python as well as javascript. python is on the backend while javascript and html are on the front end
the dependencies are in the requirements files, the run filestarts the application.
i have used python 3.6 while developing the APIs strictly OOP
 
**API END POINTS**
 
/API/v1/rides
 
/API/v1/ride/6
 
/API/v1/users/rides
 
/API/rides/4/requests
 
/API/v1/auth/signup
 
/API/v1/users
 
/API/v1/auth/login
 
/users/rides/4/requests/6
 
**RUNNING THE APP**
 
clone the app to your computer, then install the dendencies in "requirements.txt" and then
open the folder, run the start the server by running the  run.py file
The endpoints are available in a folder called "api" and the databases in a folder called "models" 

**Testing**
run the command `pytest --cov` to run the tests with coverage

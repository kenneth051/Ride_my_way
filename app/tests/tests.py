import unittest
<<<<<<< HEAD
import psycopg2
from testing import APP
from ridedb import RidesConnection
from request import RequestClass
from userdata import UserData
import json
from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_identity)

class Testing(unittest.TestCase):
     
       
=======
from flask import json
import psycopg2
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from app import APP
from app.models.Ridedb import RidesConnection
from app.models.request import RequestClass
from app.models.userdata import UserData
from flask_jwt_extended import (create_access_token,jwt_required,get_jwt_identity)


class Testing(unittest.TestCase):
>>>>>>> 04066aafaee1e0c8b07c1e61922780dcd9aca85d
    def setUp(self):
        """Define test variables and initialize app."""
        APP.config['TESTING'] = True
        self.app = APP
<<<<<<< HEAD
        with APP.test_request_context():
            self.access_token=create_access_token("username")
            self.access_header={'Authorization':'Bearer {}'.format(self.access_token)}
       

    

    def test_create_user(self):
        tester=APP.test_client(self)
        response=tester.post('/API/v1/auth/signup',
         data=json.dumps(dict(firstname = "joy",lastname = "williams",username = "joy",
        password="1234567890",gender = "female",contact = "12345678901",country = "uganda",city = "kampala")),content_type="application/json") 
        self.assertEqual(response.status_code,201) 
        self.assertIn(b"you have successfuly registered", response.data)

    def test_duplicate_user(self):
        tester=APP.test_client(self)
        response=tester.post('/API/v1/auth/signup',
        data=json.dumps(dict(firstname = "joy",lastname = "williams",username = "joy",
        password="1234567890",gender = "female",contact = "12345678901",country = "uganda",city = "kampala")),content_type="application/json") 
        self.assertEqual(response.status_code,409) 
        self.assertIn(b"username is  already in used, create a unique one", response.data)
        
    def test_login(self):  
        tester = APP.test_client(self)
        res = tester.post('http://127.0.0.1:5000/API/v1/auth/login',data = json.dumps(dict(username = "joy",password = "1234567890")),
        content_type = "application/json") 
        self.assertEqual(res.status_code,201) 
        self.assertIn(res.data)
        print(res.data)

    def test_login_no_data(self):  
        tester = APP.test_client(self)
        res = tester.post('http://127.0.0.1:5000/API/v1/auth/login',data = "",
        content_type = "application/json") 
        self.assertEqual(res.status_code,400)    
=======



    def test_for_get_api(self):
        """test for all get a requests"""
        tester = self.app.test_client(self)
        response = tester.get('/API/v1/users',
                              content_type="application/json")
        self.assertEqual(response.status_code, 401)


    def test_get_all_rides(self):
        tester = APP.test_client(self)
        res = tester.get("/API/v1/rides")
        self.assertEqual(res.status_code,200)
>>>>>>> 04066aafaee1e0c8b07c1e61922780dcd9aca85d

    def test_wrong_url(self):
        tester = APP.test_client(self)
        res = tester.get("/API/v1/boy")
        self.assertEqual(res.status_code,404)
<<<<<<< HEAD

    def test_get_A_Ride_data(self):
        tester = APP.test_client(self)
        response = tester.post('/API/v1/users/rides',data = json.dumps(dict(ride_from = "mbuya",
        ride_to="naakawa",ride_date="3/2/2018",ride_time="3pm",cost="20000",driver_id = "1")),headers=self.access_header,content_type = "application/json")
        self.assertEqual(response.status_code,201) 

    def test_Requests(self):
        tester = APP.test_client(self)
        response = tester.get('API/v1/users/rides/6/requests',headers=self.access_header)
        self.assertEqual(response.status_code, 200)  

    def test_get_all_rides(self):
        tester = APP.test_client(self)
        res = tester.get("/API/v1/rides",headers=self.access_header)
        self.assertEqual(res.status_code,200)   

    def test_get_requests(self):
        tester = APP.test_client(self)
        res = tester.post("/API/v1/users/rides/6/requests",headers=self.access_header)
        self.assertEqual(res.status_code,405)    

    def test_get_single_ride(self):
        tester = APP.test_client(self)
        res = tester.get("/API/v1/ride/6",headers=self.access_header)
        self.assertEqual(res.status_code,200)    


    def test_get_A_Ride_data(self):
        tester = APP.test_client(self)
        response = tester.post('/API/rides/5/requests',data = json.dumps(dict(ride_id = "3",
        pasenger_id="3",driver_id = "1")),headers=self.access_header,content_type = "application/json")
        self.assertEqual(response.status_code,201)       












    def tearDown(self):
        sql_commands = (
            """DROP TABLE IF EXISTS "Users" CASCADE;""",
            """DROP TABLE IF EXISTS "rides" CASCADE;""",
            """DROP TABLE IF EXISTS "requests" CASCADE;""")
        conn = None
        try:
            con = psycopg2.connect( host ="localhost",user = "postgres",password = "chaos",dbname = "testdatabase")   
            cur = con.cursor()
            for sql_command in sql_commands:
                cur.execute(sql_command)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)     
=======
        self.assertIn(b"use a valid URL", res.data)


    def test_Create_get_a_ride_wrong_data(self):
        tester = APP.test_client(self)
        response = tester.get('/API/v1/ride/8',
                               content_type="application/json")
        self.assertEqual(response.status_code, 200)
        return response.data
        
    def test_get_A_Ride_data(self):
        tester = APP.test_client(self)
        response = tester.post('/API/v1/users/rides',data = json.dumps(dict(ride_from = "mbuya",
        ride_to="naakawa",ride_date="3/2/2018",ride_time="3pm",cost="20000",driver_id = "1")),content_type = "application/json")
        self.assertEqual(response.status_code, 201) 

    def test_login(self):  
        tester = APP.test_client(self)
        response = tester.post('/API/v1/auth/login',data = json.dumps(dict(username = "username",password = "password")),
        content_type = "application/json") 
        self.assertEqual(response.status_code,201) 
        print(response.data) 

    def test_Requests(self):
        tester = APP.test_client(self)
        response = tester.get('API/v1/users/rides/6/requests')
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        tester=APP.test_client(self)
        response=tester.post('/API/v1/auth/signup',
         data=json.dumps(dict(firstname = "firstname",lastname = "lastname",username = "username",
        password="password",gender = "gender",contact = "contact",country = "country",city = "city")),content_type="application/json") 
        self.assertEqual(response.status_code,201) 
        self.assertIn(b"username is  already in used, create a unique one", response.data) 

    def test_create_user_no_info(self):
        tester = APP.test_client(self)
        response=tester.post('/API/v1/auth/signup',
         data=" ",content_type = "application/json") 
        self.assertEqual(response.status_code,400) 
        print(response.data)  

    def test_login_no_info(self):  
        tester = APP.test_client(self)
        response=tester.post('/API/v1/auth/login',data = json.dumps(dict(username = "username22",password="password")),
        content_type = "application/json") 
        self.assertEqual(response.status_code,201) 
        #self.assertIn(b"invalid username or password", response.data)
        self.assertIn(b"login failure contact ADMIN", response.data) 
      
>>>>>>> 04066aafaee1e0c8b07c1e61922780dcd9aca85d






        
if __name__ == '__main__':
    unittest.main()    


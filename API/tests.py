"""API test page"""
import unittest
import json
from app import APP
class FlaskTestCase(unittest.TestCase):
    """class to test our api"""
#test to get all rides api
    def test_rides_page_loads(self):
        """test to get all rides api"""
        tester = APP.test_client(self)
        response = tester.get('http://localhost:5000/v1/rides', content_type="application/json")
        self.assertEqual(response.status_code, 200)
  #test to get a ride api
    def test_if_ride_page_works(self):
        """test to get a ride api"""
        tester = APP.test_client(self)
        response = tester.get('http://localhost:5000/v1/ride/4', content_type="application/json")
        self.assertEqual(response.status_code, 200)
     #test to create a ride
    def test_create_a_ride(self):
        """test to create a ride"""
        tester = APP.test_client(self)
        info = dict(From="mukono", To="kampala", Time="4:00pm", Date="4/4/2018",
                    Driver="john", Cost="4000", rideID=4)
        response = tester.post('/v1/create_ride', data=json.dumps(info),
                               content_type="application/json")
        self.assertEqual(response.status_code, 200)
         #test to request a ride
    def test_request_a_ride(self):
        """test to create a ride"""
        tester = APP.test_client(self)
        info = dict(rideID=4)
        response = tester.post('/v1/ride/4/request', data=json.dumps(info),
                               content_type="application/json")
        self.assertEqual(response.status_code, 200)
#test registration api
    def test_valid_user_registration(self):
        """test registration api"""
        tester = APP.test_client(self)
        info = dict(firstname="john", lastname="Smith", username="john",
                    password="johnsmith", gender="male", id=4)
        response = tester.post('/v1/register', data=json.dumps(info),
                               content_type="application/json")
        self.assertEqual(response.status_code, 200)
#test login api
    def test_valid_user_login(self):
        """ test login api """
        tester = APP.test_client(self)
        info = dict(username="john", password="johnsmith")
        response = tester.post('/v1/login', data=json.dumps(info), content_type="application/json")
        self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    unittest.main()

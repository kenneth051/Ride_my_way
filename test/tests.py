"""API test page"""
import unittest
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from run import APP


class FlaskTestCase(unittest.TestCase):
    """class to test our api routes"""

    def setUp(self):
        self.app = APP
        self.client = self.app.test_client

    def test_for_get_apis(self):
        """test for all get a requests"""
        tester = APP.test_client(self)
        response = tester.get('http://localhost:5000/v1/rides',
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)
        res = self.client().get('/v1/rides/er')
        self.assertEqual(res.status_code, 404)

    def test_Creating_A_Ride(self):
        """test to create a ride"""
        tester = APP.test_client(self)
        res = tester.post('/v1/create_ride', data=json.dumps(
            dict(From="masaka", to="kampala", time="3pm", date="4/8/2018",
                 Id=1, cost="3000")), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn(b"Ride has been created", res.data)

    def test_Creat_A_Ride(self):
        tester = APP.test_client(self)
        response = tester.post('/v1/create_ride', data="data",
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_get_ride(self):
        tester = APP.test_client(self)
        response = tester.get('v1/ride/1')
        self.assertEqual(response.status_code, 200)
        res = tester.get('/v1/ride/u')
        self.assertEqual(res.status_code, 404)
        self.assertIn(b"use a valid URL", res.data)

    def test_Returned_data(self):
        tester = APP.test_client(self)
        response = tester.get('/v1/ride/3/request')
        self.assertEqual(response.status_code, 405)
        res = tester.post('/v1/ride/3/request',
                          content_type="application/json")
        self.assertEqual(res.status_code, 400)

        res = tester.post('/v1/ride/u/request', data={"Id": 7},
                          content_type="application/json")
        self.assertEqual(res.status_code, 404)
        self.assertIn(b"use a valid URL", res.data)
        res = tester.post('/v1/ride/2/request', data=json.dumps(dict(Id=2)),
                          content_type="application/json")
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()

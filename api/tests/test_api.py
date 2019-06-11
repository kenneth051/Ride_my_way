"""API test page"""
import unittest
import json
from api import APP


class FlaskTestCase(unittest.TestCase):
    """class to test our api routes"""

    def test_for_get_api(self):
        """test for all get a requests"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/rides',
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_for_get_api_invalid_url(self):
        tester = APP.test_client(self)
        res = tester.get('/API/v1/rides/er')
        self.assertEqual(res.status_code, 404)

    def test_Creating_A_Ride(self):
        """test to create a ride"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/create_ride', data=json.dumps(
            dict(from_where="mbuya", to="kampala", time="3pm", date="4/8/2018",
                 ride_id=1, cost="3000")), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn(b"Ride has been created", res.data)

    def test_Create_A_Ride_wrong_data(self):
        tester = APP.test_client(self)
        response = tester.post('/API/v1/create_ride', data="data",
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_get_ride(self):
        tester = APP.test_client(self)
        response = tester.get('/API/v1/ride/1')
        self.assertEqual(response.status_code, 200)

    def test_get_ride_bad_id(self):
        tester = APP.test_client(self)
        res = tester.get('/API/v1/ride/u')
        self.assertEqual(res.status_code, 404)
        self.assertIn(b"use a valid URL", res.data)

    def test_Request_as_get(self):
        tester = APP.test_client(self)
        response = tester.get('/API/v1/ride/3/request')
        self.assertEqual(response.status_code, 405)

    def test_Request_without_sendingdata(self):
        tester = APP.test_client(self)
        res = tester.post('/API/v1/ride/3/request',
                          content_type="application/json")
        self.assertEqual(res.status_code, 400)

    def test_request_with_wrong_url_info(self):
        tester = APP.test_client(self)
        res = tester.post('/API/v1/ride/u/request', data={"ride_id": 7},
                          content_type="application/json")
        self.assertEqual(res.status_code, 404)
        self.assertIn(b"use a valid URL", res.data)

    def test_good_request(self):
        tester = APP.test_client(self)
        res = tester.post('/API/v1/ride/2/request',
                          data=json.dumps(dict(ride_id=2)),
                          content_type="application/json")
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()

"""class to validate rides being created"""
class Validate:
    @classmethod
    def validate_ride(cls, rides, created_ride):
        """method to check for duplicate ride"""
        for ride_info in rides:
            if (ride_info['From'] == created_ride['From'] and
                    ride_info['to'] == created_ride['to']and
                    ride_info['date'] == created_ride['date']and
                    ride_info['time'] == created_ride['time']):
                return True
    @classmethod
    def validate_id(cls, rides, ride_id):
        """method to check if Id has been used"""
        for  ride_info in rides:
            if ride_info['Id'] == ride_id:
                return True

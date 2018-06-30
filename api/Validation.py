"""class to validate rides being created"""


class validate:

    @classmethod
    def validate_ride(cls, rides, created_ride):
        """method to check for duplicate ride"""
        for ride_info in rides:
            if (ride_info['from_where'] == created_ride.from_where and
                    ride_info['to'] == created_ride.to and
                    ride_info['date'] == created_ride.date and
                    ride_info['time'] == created_ride.time ):
                return True

    @classmethod
    def validate_id(cls, rides, _id):
        """method to check if Id has been used"""
        for ride_info in rides:
            if ride_info['ride_id'] == _id:
                return True

    @classmethod
    def validate_empty(cls,create_ride):
        if(create_ride.from_where == "" or 
               create_ride.to == ""or
               create_ride.date == ""or
               create_ride.time == "" or 
               create_ride.ride_id == ""or
               create_ride.cost == ""):
            return True
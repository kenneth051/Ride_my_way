class Validate:
    @classmethod
    def Validate_Ride(cls,rides,created_ride):
        for ride_info in rides:
            if (ride_info['From'] == created_ride['From'] and
                ride_info['to'] == created_ride['to']and
                ride_info['date'] == created_ride['date']and
                ride_info['time'] == created_ride['time']):
                    return True

    @classmethod
    def Validate_Ride_Id(self,rides,ride_id):
               pass

from ride import rides


class requestClass():
    requested_rides=[]
    def __init__(self, ride_id,):
        self.ride_id = ride_id        
    
    def request_ride(self):
        """method for requesting a ride offer"""
        result = "Invalid id"
        for ride_info in rides.all_rides:
            if ride_info['ride_id'] == self.ride_id:
                result ={"success": ("you have requested to join the ride from",
                          ride_info['from_where'], "to", ride_info["to"],
                           "on", ride_info["date"])}
                requestClass.requested_rides.append(result)          

        return result

        
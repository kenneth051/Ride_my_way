class ValidateRides():
    """valiation class for my user inputs"""
    def __init__(self, ride_from1, ride_to1, ride_date1, ride_time1, cost1, driver_id):
        self.ride_from1 = ride_from1
        self.ride_to1 = ride_to1
        self.ride_date1= ride_date1
        self.ride_time1 = ride_time1
        self.cost1 = cost1
        self.driver_id = driver_id
    def validate_empty(self):
        result=""
        """method to validate my input registeration files"""
        if (self.ride_from1 == "" or self.ride_to1 == "" or self.ride_date1 == ""
            or self.ride_time1 == "" or self.cost1 == "" or self.driver_id == ""):
             return"INPUTS CANNOT BE EMPTY FILL IN ALL FIELDS PLEASE"
        elif (type(self.ride_from1) != str or type(self.ride_time1) != str or 
              type(self.driver_id) != str or type(self.ride_to1) != str
              or type(self.cost1) != str  or type(self.ride_date1) != str):
            return"CHECK INPUT TYPE AND TRY, USE VALID DATA FOR EACH FIELD"
        else:
            result= True
        return result     


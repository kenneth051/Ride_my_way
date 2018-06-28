from Validation import Validate
class Rides():
    
    All_rides =[]

    def __init__(self,Id,From,to,time,date):
       self.create_ride={}
       self.Id=Id
       self.From=From
       self.to=to
       self.time=time
       self.date=date

    def Create_Ride(self):
        self.create_ride["From"]=self.From
        self.create_ride["Id"]=self.Id
        self.create_ride["to"]=self.to
        self.create_ride["time"]=self.time
        self.create_ride["date"]=self.date
        if Validate.Validate_Ride(Rides.All_rides,self.create_ride):
            return "Ride was already created"
        else:    
            Rides.All_rides.append(self.create_ride)
            self.create_ride={}
            return"Ride has been created"

    @classmethod
    def DisplayRides(cls):
         return Rides.All_rides
    @classmethod
    def  GetOne_Ride(cls,data):
        result="Invalid ID, use a valid one"
        for ride_info in Rides.All_rides:
            if ride_info['Id'] == data:
                result = ride_info 
        return result 

    @classmethod
    def Request_Ride(cls, data):
        result = "Invalid id"
        for ride_info in Rides.All_rides:
           if ride_info["Id"] == data:
               result = ("you have requested to join the ride from",
                          ride_info['From'], "to", ride_info["to"], "at",ride_info['time'], "on", ride_info["date"])
        return result
        

one=Rides(2,"kampala","mbale","3:PM","4/8/2018")
one.Create_Ride()
one=Rides(1,"entebbe","kawempe","5PM","7/3/2018")
one.Create_Ride()

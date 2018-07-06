from app.models.database import Database

class RequestClass(Database):
    def __init__(self):
        Database.__init__(self)
    
    def create_table(self):
        try: 
            cur=self.con.cursor()
            cur.execute("""create table Requests (id serial primary key not null,ride_id int references Rides(id),
            passenger_id int not null, driver_id int not null, status text)""", )
            self.con.commit()
            print("request table created")
        except:
            print("table request already created or error creating it")    

    def create_request(self, ride_id1, passenger_id1, driver_id1):
        req=RequestClass()
        req.create_table()
        try:
            cur=self.con.cursor()                   
            cur.execute("SELECT * FROM Requests where ride_id = %s and passenger_id = %s\
                        and driver_id = %s", (ride_id1, passenger_id1, driver_id1))
            self.con.commit()
            result=cur.rowcount
            if result>0:
                print("request has been created previously no duplicates allowed")
            else:   
                cur.execute("INSERT INTO Requests(ride_id, passenger_id, driver_id)VALUES\
                (%s, %s, %s)",(ride_id1, passenger_id1, driver_id1))      
                self.con.commit()
                print("Request has been created successfully")
        except:
            return "Request cannot be created, contact ADMIN Error 500"
            
    def getdriver(self,driver):
        cur=self.con.cursor()                   
        cur.execute("SELECT driver_id FROM Rides where id = %s ", (driver,))
        result=cur.rowcount
        if result==1:
            data=cur.fetchone()
            return data
    def create_requests(self,ride_id1,passenger_id1,driver_id1):
        try:
            cur=self.con.cursor()
            cur.execute("SELECT * FROM Requests where ride_id = %s and passenger_id = %s and driver_id = %s ",(ride_id1,passenger_id1,driver_id1))
            self.con.commit()
            result=cur.rowcount
            if result>0:
                return "Request has been created previously! no duplicate allowed"
            else:   
                cur.execute("INSERT INTO Requests(ride_id, passenger_id, driver_id)VALUES\
                (%s,%s,%s)",(ride_id1,passenger_id1,driver_id1))      
                self.con.commit()
                return"Request has been created successfully"
        except:
            return "Request cannot be created, Check your ride id"    

    def single_ride(self,_id):
        cur=self.con.cursor()
        cur.execute("SELECT * FROM Rides where ride_id = %s ", (_id,));
        affected=cur.rowcount
        result=cur.fetchall()
        if affected >0: 
            data = {}
            lst = []
            for row in result:
                data["ride_id"] = row[0]
                data["ride_from"] = row[1]
                data["ride_to"] = row[2]
                data["ride_date"] = row[3]
                data["ride_time"] = row[4]
                data["cost"] = row[5]
                data["driver_id"] = row[6]
                lst.append(data)
            return lst
        else:
            return "invalid ride Id " 

    def get_requests(self, rideId):
        cur=self.con.cursor()
        cur.execute("SELECT id,ride_id, passenger_id, driver_id, status FROM Requests WHERE ride_id = %s", (rideId,))
        affected=cur.rowcount
        if affected > 0: 
            result=cur.fetchall()
            lst=[]
            for row in result:
                data={}
                data[" id"] = row[0]
                data["ride_id"] = row[1]
                data["passenger_id"] = row[3]
                data["driver_id"] = row[2]
                data["status"] = row[4]
                lst.append(data)
            return lst
        else:
            return "No rides created yet"
    def request_status(self, status1, _id):
        cur=self.con.cursor()
        cur.execute("UPDATE Requests SET status= %s WHERE id = %s", (status1, _id))
        if self.con.commit():
            return "You have responded to a ride request"
        else:
            return "responding to Request failed"   
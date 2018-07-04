
from ride import rides
from database import Database


class RequestClass(Database):
    requested_rides=[]
    def __init__(self):
        Database.__init__(self)
 
        
    def createTable(self):
        try: 
            cur=self.con.cursor()
            cur.execute("""create table Requests (id serial primary key not null,ride_id int references Rides(id),
            passenger_id int not null, driver_id int not null,status int)""",)
            self.con.commit()
            print("request table created")
        except:
            print("table request already created or error creating it")    

    def createRequest(self,ride_id1,passenger_id1,driver_id1):
        try:
            cur=self.con.cursor()                   
            cur.execute("SELECT * FROM Requests where ride_id = %s and passenger_id = %s and driver_id = %s",(ride_id1,passenger_id1,driver_id1))
            self.con.commit()
            result=cur.rowcount
            if result>0:
                print("request has been created previously no duplicates allowed")
            else:   
                cur.execute("INSERT INTO Requests(ride_id,passenger_id,driver_id)VALUES\
                (%s,%s,%s)",(ride_id1,passenger_id1,driver_id1))      
                self.con.commit()
                print("Request has been created successfully")
        except:
            return "Request cannot be created, contact ADMIN Error 500"              
                        
    '''def fetch_rides(self):
        cur=self.con.cursor()
        cur.execute("SELECT * FROM  Requests",);
        affected=cur.rowcount
        if affected >0: 
            result=cur.fetchall()
            lst=[]
            for row in result:
                data={}
                data["ride_id"]= row[0]
                data["ride_from"]=row[1]
                data["ride_to"]=row[2]
                data["ride_date"]=row[3]
                data["ride_time"]=row[4]
                data["cost"]=row[5]
                data["driver_id"]=row[6]
                lst.append(data)
            #data=result.__dict__
            return lst
        else:
            return "No rides created yet"
'''
    def single_ride(self,_id):
        cur=self.con.cursor()
        cur.execute("SELECT * FROM Rides where ride_id = %s ",(_id,));
        affected=cur.rowcount
        result=cur.fetchall()
        if affected >0: 
            data={}
            lst=[]
            for row in result:
                data["ride_id"]= row[0]
                data["ride_from"]=row[1]
                data["ride_to"]=row[2]
                data["ride_date"]=row[3]
                data["ride_time"]=row[4]
                data["cost"]=row[5]
                data["driver_id"]=row[6]
                lst.append(data)
            #data=result.__dict__
            return lst
        else:
            return "invalid ride Id " 

req=RequestClass()
#req.createTable()
req.createRequest("5","6","7")
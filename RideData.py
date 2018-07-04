import psycopg2
from database import Database
class RidesConnection(Database):  
   
    def __init__(self):
         Database.__init__(self)

    def createTable(self):
        try: 
            cur=self.con.cursor()
            cur.execute("""create table Rides (id serial primary key not null,ride_from text not null,
            ride_to text not null, ride_date text not null,ride_time text not null,
            cost text not null,driver_id int references Users(id))""",)
            self.con.commit()
            print("table created")
            self.con.close()
        except:
            print("table already created or error creating it")    

    def createRide(self,ride_from1,ride_to1,ride_date1,ride_time1,cost1,driver_id1):
        try:
            cur=self.con.cursor()                   
            cur.execute("SELECT * FROM Rides where ride_from = %s and ride_to = %s and ride_date = %s and driver_id = %s",(ride_from1,ride_to1,ride_date1,driver_id1))
            self.con.commit()
            result=cur.rowcount
            if result>0:
                return "ride has been created previously no duplicate allowed"
            else:   
                cur.execute("INSERT INTO Rides(ride_from,ride_to,ride_date,ride_time,cost,driver_id)VALUES\
                (%s,%s,%s,%s,%s,%s)",(ride_from1,ride_to1,ride_date1,ride_time1,cost1,driver_id1))      
                self.con.commit()
                return "Ride has been created successfully"
        except:
            return "Ride cannot be created, contact ADMIN Error 500"                
                        
    def fetch_rides(self):
        cur=self.con.cursor()
        cur.execute("SELECT * FROM  Rides",);
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
            return lst
        else:
            return "No rides created yet"

    def single_ride(self,_id):
        cur=self.con.cursor()
        cur.execute("SELECT * FROM Rides where id = %s ",(_id,));
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
            return lst
        else:
            return "invalid ride Id "    
        

   
#d=RidesConnection()
#d.login("kenneth051","kenneth")

#d.createTable()
#d.createRide("jinja","kampala","2/4/2012","12:42am","2000","13")
#d.fetch_rides()
#d.singleUsers(31)
#self,firstname1,lastname1,username1,password1,gender1,contact1,country1,city1
#"joy","williams","joy4","12345","female","99999","usa","carlifornia"
""" a request page"""
from flask import jsonify
from database import Database

class RequestClass(Database):
    """ a request class """
    def __init__(self):
        Database.__init__(self)
    def create_table(self):
        """ a method to create a table """
        try:
            cur = self.con.cursor()
            cur.execute("""create table IF NOT EXISTS Requests (req_id serial primary key not null, ride_id int references Rides(id),
            passenger_id int, driver_id int, status text)""", )
            self.con.commit()
        except:
            pass
    def create_requests(self, ride_id1, passenger_id1, driver_id1):
        """ a method to create a ride"""
        try:
            cur = self.con.cursor()                   
            cur.execute("SELECT * FROM Requests where ride_id = %s and passenger_id = %s and driver_id = %s", (ride_id1, passenger_id1, driver_id1))
            self.con.commit()
            result = cur.rowcount
            if result > 0:
                return jsonify({"result":"request has been created previously no duplicates allowed"})
            else:
                cur.execute("INSERT INTO Requests(ride_id,passenger_id,driver_id)values(%s,%s,%s)", (ride_id1, passenger_id1, driver_id1))      
                self.con.commit()
                return "Request has been created successfully"
        except:
            return jsonify({"result":"Request cannot be created, contact ADMIN Error 500"})
            
    def getdriver(self,driver):
        """ a method to get driver data"""
        cur=self.con.cursor()           
        cur.execute("SELECT driver_id FROM Rides where id = %s ", (driver, ))
        result = cur.rowcount
        if result == 1:
            data = cur.fetchone()
            return data

   
    def get_requests(self, rideId):
        """ a method to get a request"""
        cur = self.con.cursor()
        cur.execute("SELECT req_id,ride_id, passenger_id, driver_id, status FROM Requests WHERE ride_id = %s", (rideId,))
        affected = cur.rowcount
        if affected > 0: 
            result = cur.fetchall()
            lst = []
            for row in result:
                data = {}
                data[" id"] = row[0]
                data["ride_id"] = row[1]
                data["passenger_id"] = row[3]
                data["driver_id"] = row[2]
                data["status"] = row[4]
                lst.append(data)
            return lst
        else:
            response = jsonify({"message":"no request presents"})
            response.status_code = 200
            return response
    def request_status(self, status1, _id):
        """ a method to get requests """        
        cur=self.con.cursor()
        cur.execute("UPDATE Requests SET status = %s WHERE req_id = %s", (status1, _id))
        if self.con.commit():
            response = jsonify({"message":"You have responded to a ride request"})
            response.status_code =201
            return response
        else:
            response = jsonify({"message":"responding to Request failed"})
            response.status_code = 201
            return response
TABLE=RequestClass()
TABLE.create_table()

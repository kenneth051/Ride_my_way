import psycopg2
class Database:

    def __init__(self):
            self.con = psycopg2.connect( host ="localhost",user = "postgres",password = "chaos",dbname = "Ride_my_way")  
            if self.con:
                print("database connected to")
            else:
                print("cannot connect to database")    
            
    def closedb(self):
            self.con.close()
    def droptable(self):
              
        try:
            cur=self.con.cursor()                   
            cur.execute("DROP TABLE Rides, Requests, Rides")
            self.con.commit()
            print("table has been deleted")
        except:
            print("rides table cannot be deleted")    

en=Database()
en.droptable()            
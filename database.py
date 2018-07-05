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
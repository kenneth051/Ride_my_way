import psycopg2
<<<<<<< HEAD
from testing import APP
=======
from app import APP
>>>>>>> 04066aafaee1e0c8b07c1e61922780dcd9aca85d



class Database:
    def __init__(self):
            if not APP.config['TESTING']:
                self.con = psycopg2.connect( host ="localhost",user = "postgres",password = "chaos",dbname = "Ride_my_way")    
<<<<<<< HEAD
=======
                if self.con:
                    print("database connected to")
                else:
                    print("cannot connect to database") 
>>>>>>> 04066aafaee1e0c8b07c1e61922780dcd9aca85d
            else:
                self.con = psycopg2.connect( host ="localhost",user = "postgres",password = "chaos",dbname = "testdatabase")   
                if self.con:
                    cur=self.con.cursor()
                    cur.execute("""create table IF NOT EXISTS Users (id serial primary key not null,firstname text not null,
                    lastname text not null, username text not null,password text not null,
                    gender text not null,contact text not null,country text,city text)""",)
                    self.con.commit()
<<<<<<< HEAD
                    cur=self.con.cursor()
=======
>>>>>>> 04066aafaee1e0c8b07c1e61922780dcd9aca85d
                    cur.execute("""create table IF NOT EXISTS Rides  (id serial primary key not null,ride_from text not null,
                    ride_to text not null, ride_date text not null,ride_time text not null,
                    cost text not null,driver_id int references Users(user_id))""",)
                    self.con.commit()
                    cur=self.con.cursor()
                    cur.execute("""create table IF NOT EXISTS Requests (id serial primary key not null,ride_id int references Rides(id),
                    passenger_id int not null, driver_id int not null,status text)""",)
                    self.con.commit()
                   
<<<<<<< HEAD
                else:
                    pass
                   
    def closedb(self):
            self.con.close()  

d = Database()                     
=======
                    print("database connected to")
                else:
                    print("cannot connect to database")            
                
    def closedb(self):
            self.con.close()  

d=Database()                     
>>>>>>> 04066aafaee1e0c8b07c1e61922780dcd9aca85d

import psycopg2

class Database:  
    con = psycopg2.connect( host ="localhost",user = "postgres",
        password = "chaos",dbname = "Ride_my_way") 
    
    def __init__(self):
        if Database.con:
            print("database connected to")
        else:
            print("cannot connect to database")    
        
    @classmethod
    def closedb(self):
        Database.con.close()
    @classmethod 
    def createTable(self):
        cur=Database.con.cursor()
        cur.execute("""create table Users (user_id serial primary key not null,firstname text not null,
        lastname text not null, username text not null,password text not null,
        gender text not null,contact text not null,country text,city text)""",)
        Database.con.commit()
        Database.closedb()
    @classmethod
    def insertIntoUsers(self,firstname1,lastname1,username1,password1,gender1,contact1,country1,city1):
        try:
            cur=Database.con.cursor()
            cur.execute("INSERT INTO Users(firstname,lastname,username,password,gender,contact,country,city)VALUES\
(%s,%s,%s,%s,%s,%s,%s,%s)",(firstname1,lastname1,username1,password1,gender1,contact1,country1,city1))      
            Database.con.commit()
            result="you have successfuly registered"
            #Database.closedb()
            print(result)
        except:
            print("user not registered")        
                

    @classmethod        
    def fetchUsers(self):
        cur=Database.con.cursor()
        cur.execute("SELECT * FROM Users",);
        result=cur.fetchall()
        Database.closedb()
        print(result)
d=Database()
#Database.createTable()
Database.insertIntoUsers("joy","williams","joy4","12345","female","99999","usa","carlifornia")
#Database.fetchUsers()
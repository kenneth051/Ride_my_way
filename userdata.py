import psycopg2
from flask_jwt_extended import (create_access_token,jwt_required,get_jwt_identity)
class Database:  
    '''con = psycopg2.connect( host ="localhost",user = "postgres",
        password = "chaos",dbname = "Ride_my_way") '''
    
    def __init__(self):
        self.con = psycopg2.connect( host ="localhost",user = "postgres",password = "chaos",dbname = "Ride_my_way")  
        if self.con:
            print("database connected to")
        else:
            print("cannot connect to database")    
        
    def closedb(self):
        self.con.close()
     
    def createTable(self):
        try: 
            cur=self.con.cursor()
            cur.execute("""create table Users (user_id serial primary key not null,firstname text not null,
            lastname text not null, username text not null,password text not null,
            gender text not null,contact text not null,country text,city text)""",)
            self.con.commit()
            self.con.close()
        except:
            print("table already created or error creating it")    
    def insertIntoUsers(self,firstname1,lastname1,username1,password1,gender1,contact1,country1,city1):
        try:
            cur=self.con.cursor()                   
            cur.execute("SELECT username FROM Users where username = %s ",(username1,))
            self.con.commit()
            result=cur.rowcount
            if result>0:
                return "username is  already in used, create a unique one"
            else:   
                cur.execute("INSERT INTO Users(firstname,lastname,username,password,gender,contact,country,city)VALUES\
                (%s,%s,%s,%s,%s,%s,%s,%s)",(firstname1,lastname1,username1,password1,gender1,contact1,country1,city1))      
                self.con.commit()
                return"you have successfuly registered"
                #Database.closedb()
        except:
            return "user cannot be registered, contact ADMIN"                
                        
    def fetchUsers(self):
        cur=self.con.cursor()
        cur.execute("SELECT * FROM Users",);
        result=cur.fetchall()
        lst=[]
        for row in result:
            data={}
            data["user_id"]= row[0]
            data["firstname"]=row[1]
            data["lastname"]=row[2]
            data["username"]=row[3]
            data["password"]=row[4]
            data["gender"]=row[5]
            data["contact"]=row[6]
            data["country"]=row[7]
            data["city"]=row[8]
            lst.append(data)
        #data=result.__dict__
        return lst

    def SingleUser(self,_id):
        cur=self.con.cursor()
        cur.execute("SELECT * FROM Users where user_id = %s ",(_id,));
        affected=cur.rowcount
        result=cur.fetchall()
        if affected >0: 
            data={}
            lst=[]
            for row in result:
                data["user_id"]= row[0]
                data["firstname"]=row[1]
                data["lastname"]=row[2]
                data["username"]=row[3]
                data["password"]=row[4]
                data["gender"]=row[5]
                data["contact"]=row[6]
                data["country"]=row[7]
                data["city"]=row[8]
                lst.append(data)
            #data=result.__dict__
            return lst
        else:
            return "invalid user ID use a valid one"    
        

    def login(self,username1,password1):
        try:
            cur=self.con.cursor()
            cur.execute("SELECT user_id FROM  Users where username = %s AND password = %s",(username1,password1))      
            self.con.commit()
            count=cur.rowcount
            result=cur.fetchone()
            if count > 0:
                access_token = create_access_token(identity=result)
                return access_token 
            else:
                return "invalid username or password"  
            #Database.closedb()
            
        except:
            return "login failure contact ADMIN"        
                    
d=Database()
#d.login("kenneth051","kenneth")

#d.createTable()
#d.insertIntoUsers("joy","williams","joy2","12345","female","99999","usa","carlifornia")
#d.fetchUsers()
#d.singleUsers(31)
#self,firstname1,lastname1,username1,password1,gender1,contact1,country1,city1
#"joy","williams","joy4","12345","female","99999","usa","carlifornia"
"""Userdata dataase class"""
from app.models.database import Database
from flask import request, jsonify
from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_identity)

class UserData(Database):  
    
    def __init__(self):
         Database.__init__(self)
     
    def create_table(self):
        try: 
            cur = self.con.cursor()
            cur.execute("""create table Users (user_id serial primary key not null,firstname text not null,
            lastname text not null, username text not null,password text not null,
            gender text not null,contact text not null,country text,city text)""", )
            self.con.commit()
            self.con.close()
        except:
           pass

    def insert_into_users(self, firstname1, lastname1, username1, password1, gender1, contact1, country1, city1):
        try:
            cur = self.con.cursor()                   
            cur.execute("SELECT username FROM Users where username =%s ", (username1, ))
            self.con.commit()
            result = cur.rowcount
            if result > 0:
                response = jsonify({"message":"username is  already in used, create a unique one"})
                response.status_code = 409
                return response
                
            else: 
                cur.execute("INSERT INTO Users(firstname, lastname, username, password,\
                gender, contact, country,city)VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (firstname1, lastname1, username1, password1, gender1, contact1, country1, city1))    
                self.con.commit()
                response = jsonify({"message":"you have successfuly registered"})
                response.status_code =201
                return response
        except:
            response = jsonify({"message":"user cannot be registered, contact ADMIN"})
            response.status_code =400
            return response               
                        
    def fetch_users(self):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM Users", )
        result = cur.fetchall()
        lst = []
        for row in result:
            data = {}
            data["user_id"] = row[0]
            data["firstname"] = row[1]
            data["lastname"] = row[2]
            data["username"] = row[3]
            data["password"] = row[4]
            data["gender"] = row[5]
            data["contact"] = row[6]
            data["country"] = row[7]
            data["city"] = row[8]
            lst.append(data)
        return lst

    def login(self, username1, password1):
        try:
            cur = self.con.cursor()
            cur.execute("SELECT id FROM  Users where username = %s AND password = %s", (username1, password1))   
            self.con.commit()
            count = cur.rowcount
            result = cur.fetchone()
            if count > 0:
                access_token = create_access_token(identity=result)
                response = jsonify({"token":access_token})
                response.status_code = 201
                return response  
            else:
                response = jsonify({"message":"Invalid username or password"})
                response.status_code = 403
                return response  
        except:
            return "login failure contact ADMIN"
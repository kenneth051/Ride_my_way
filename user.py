from flask import jsonify
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)
class user:
    user_list=[]
    def __init__(self,_id,username,firstname,lastname,password,sex,contact,city,country):
        self._id=_id
        self.username=username
        self.firstname=firstname
        self.lastname=lastname
        self.password=password
        self.sex=sex
        self.contact=contact
        self.city=city
        self.country=country

    def create_user(self):
        created_user={}
        data=user(self._id,self.username,self.firstname,self.lastname,
                  self.password,self.sex,self.contact,self.city,
                  self.country)
        created_user=data.__dict__
        user.user_list.append(created_user)
        return "User has been created"

    @classmethod
    def show_users(self):
        return user.user_list

    @classmethod   
    def login(self,username,password):
        result="user doesnt exist,use valid credentials"
        for info in user.user_list:
                if info['username'] == username and info['password'] == password:
                     result= jsonify({"access_token":access_token})
        return result

              

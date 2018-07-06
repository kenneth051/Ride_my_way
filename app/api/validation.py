class ValidateUsers():
    """valiation class for my user inputs"""
    def __init__(self, firstname, lastname, username, password, gender, contact, city, country):
        self.username = username
        self.lastname = lastname
        self.firstname = firstname
        self.password = password
        self.gender = gender
        self.contact = contact
        self.city = city
        self.country = country
 
    def validate_empty(self):
        result=""
        """method to validate my input registeration files"""
        if (self.username == "" or self.lastname == "" or self.firstname == ""
            or self.password == "" or self.gender == "" or self.contact == ""
            or self.city == "" or self.country == ""):
             result="INPUTS CANNOT BE EMPTY FILL IN ALL FIELDS PLEASE"
        elif (type(self.username) != str or type(self.firstname) != str or 
              type(self.lastname) != str or type(self.password) != str
              or type(self.gender) != str  or type(self.contact) != str  or
              type(self.city) != str or type(self.country) != str):
             result="CHECK INPUT TYPE AND TRY, USE VALID DATA FOR EACH FIELD"
        elif len(self.contact) <= 10 or  len(self.contact) > 14:
             result="PHONE NUMBER NOT VALID"
        elif len(self.password) < 8:
             result= "PASSWORD MUST BE 8 CHARACTERS"    
        else:
             result= True
        return result     

data = ValidateUsers("ken", "joseph", "dumba", "123456", "", "werrttt", "kla", "ug")
if(data.validate_empty()):
        print("yes")
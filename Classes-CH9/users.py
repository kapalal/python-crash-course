class User(object):
    
    def __init__(self,first_name,last_name,age,email_address):
        
        self.fname= first_name
        self.last_name= last_name
        self.age = age
        self.email_address = email_address
        self.login_attempts = 0
    def describe_user(self):
        
        print("----------------------------")
        print("User: " + self.fname )
        print("Last Name: " + self.last_name)
        print("Age: " + str(self.age))
        print("Email: " + self.email_address)
    def greet_user(self):
        print("Hello " + self.fname + "!")
    def increment_login_attempts(self,increments):
        self.login_attempts += increments
    def reset_login_attempts(self,login=0):
        self.login_attempts = login




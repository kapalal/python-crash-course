 # Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166). 
 # Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
 # Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
 # Make an instance of the User class and call increment_login_attempts() several times. 
 # Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
 # Print login_attempts again to make sure it was reset to 0.

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
        
mihai = User('mihai','kurikov',29,'mkurivo@gmail.com')
mihai.increment_login_attempts(3)
print mihai.login_attempts       
mihai.increment_login_attempts(3)
print mihai.login_attempts
mihai.increment_login_attempts(3)
print mihai.login_attempts
mihai.reset_login_attempts()
print mihai.login_attempts
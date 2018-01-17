#Admin: An administrator is a special kind of user.
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171). 
# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 
# Write a method called show_privileges() that lists the administrator’s set of privileges. 
# Create an instance of Admin, and call your method.

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



class Admin(User):
    def __init__(self,first_name,last_name,age,email_address):

        super(Admin,self).__init__(first_name,last_name,age,email_address)
        self.privileges = Privileges()
    

#Privileges: Write a separate Privileges class. 
# The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
# Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.


class Privileges(object):
    def __init__(self):
        self.privilegess = ['can add post','can delete post','can lke post']
    def funcname(self):
        print self.privilegess
    

nkapalala = Admin('Ivan','Kapalala',27,'ivan@inva.com')
nkapalala.privileges.funcname()
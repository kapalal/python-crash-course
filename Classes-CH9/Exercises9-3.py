#9-3. Users: Make a class called User. 
# Create two attributes called first_name and last_name, 
# and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user.
#Create several instances representing different users, and call both methods for each user.


class User(object):
    def __init__(self,first_name,last_name,age,email_address):
      self.fname= first_name
      self.last_name= last_name
      self.age = age
      self.email_address = email_address
    
    def describe_user(self):
          print("----------------------------")
          print("User: " + self.fname )
          print("Last Name: " + self.last_name)
          print("Age: " + str(self.age))
          print("Email: " + self.email_address)

    def greet_user(self):
          print("Hello " + self.fname + "!")
          



ripper12 = User('Gianni','Gambalunga',13,'gglunga@gmail.com')
kraken14 = User('Karlos','Riviera',24,'krivera@gmail.com')
rooney43 = User('Renato','Fonseca',43,'renseca@gmail.com')

users = [ripper12,kraken14,rooney43]
for u in users:
      u.describe_user()
      u.greet_user()


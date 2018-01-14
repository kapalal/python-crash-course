#9-1. Restaurant: Make a class called Restaurant. 
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(self.name.title() + " is here!" )
        print( "The cuisine type is : " + self.cuisine.title())

    def open_restaurant(self):
        print("The " + self.name.title() + " has opended!")
    
  
my_restaurant = Restaurant('RoseBlue','Afro-Jappo')
print my_restaurant.name
print my_restaurant.cuisine
print ("\n------------------------------")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
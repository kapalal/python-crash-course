# Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). 
# Either version of the class will work; just pick the one you like better. 
# Add an attribute called flavors that stores a list of ice cream flavors. 
# Write a method that displays these flavors. 
# Create an instance of IceCreamStand, and call this method.

class Restaurant(object):
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(self.name.title() + " is here!" )
        print( "The cuisine type is : " + self.cuisine.title())

    def open_restaurant(self):
        print("The " + self.name.title() + " has opended!")


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super(IceCreamStand,self).__init__(restaurant_name,cuisine_type)
        self.flavors = ['fragola','lemoni','arancia']
        
    def display_flava(self):
        print self.flavors

gelato1 = IceCreamStand('Maga Gel','Gelateria')
gelato1.display_flava()
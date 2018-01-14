#9-2. Three Restaurants: Start with your class from Exercise 9-1. 
# Create three different instances from the class, 
# and call describe_restaurant() for each instance.

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(self.name.title() + " is here!" )
        print( "The cuisine type is : " + self.cuisine.title())

    def open_restaurant(self):
        print("The " + self.name.title() + " has opended!")
    
jupiter= Restaurant('Jupiter','Irish')
melograno= Restaurant('Melograno','Sardo')
da_giggi= Restaurant('Da Giggi','Italian')

risto = [jupiter,melograno,da_giggi]

for r in risto:
    r.describe_restaurant()


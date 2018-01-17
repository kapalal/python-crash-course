class Restaurant(object):
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(self.name.title() + " is here!" )
        print( "The cuisine type is : " + self.cuisine.title())

    def open_restaurant(self):
        print("The " + self.name.title() + " has opended!")


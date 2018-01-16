#9-4. Number Served: Start with your program from Exercise 9-1 (page 166). 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name.title() + " is here!" )
        print( "The cuisine type is : " + self.cuisine.title())

    def open_restaurant(self):
        print("The " + self.name.title() + " has opended!")

    def set_number_served(self,num):
        self.number_served = num

    def increment_number_served(self,incnum):
        self.number_served += incnum
                

risto1 = Restaurant('Le cicogne','Arab')
print risto1.number_served
risto1.set_number_served(2)
print risto1.number_served
risto1.increment_number_served(30) 
print risto1.number_served   
#7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['big','tasty','cheesy','apple','pastrami','pastrami','pastrami']
finished_sandwiches = []

print("Sorry we've run out of Pastrami!")

while "pastrami" in sandwich_orders:
    
    orders= sandwich_orders.remove('pastrami')
    

print("These are the sandwich available: ")

while sandwich_orders:
    orders= sandwich_orders.pop()
    finished_sandwiches.append(orders)


for orders in finished_sandwiches:
    print("The " + orders + " is available")


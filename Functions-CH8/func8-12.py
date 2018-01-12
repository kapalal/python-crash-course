#8-12. 
# Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that is being ordered. 
# Call the function three times, using a different number of arguments each time.

def make_sanwitch(*ingredients):
    print ingredients

make_sanwitch('potatoes','salade')
make_sanwitch('pasta')
make_sanwitch('cabbages','mayo','ketchup','guacamole')

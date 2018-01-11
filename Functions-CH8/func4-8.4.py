#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.


def make_tshirt(size="large",msg="I love Python"):
    print("The choosen size is: "+ size + " and the chosen message is " + msg)




make_tshirt()
make_tshirt(size="medium")
make_tshirt("any","I love potates")
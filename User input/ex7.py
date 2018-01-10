
prompt= ("\nPlease enter you topping!")

prompt+= ("\n( Press enter quit to quit.) Topping: ")


while True:
    topping = input(prompt)
    if topping == 'quit':
        print("Thanks for choosing us Good bye!")
        break
    else:
        print ("Some " + topping + " will be added to the pizza")

#hh
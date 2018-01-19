#10-4. Guest Book: Write a while loop that prompts users for their name. 
# When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.

gbook ='guestbook.txt'


while True:
    
    with open(gbook,'a') as obj:
        name = input("Please enter Your Name: ")
        obj.write("Name: " + name+ "\n")
        check = input("Name registered, enter X to exit ")
        if check == "X":
            break
        else:
            continue

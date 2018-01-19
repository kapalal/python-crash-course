#10-3. Guest: Write a program that prompts the user for their name. 
# When they respond, write their name to a file called guest.txt.


filename = "guest.txt"

username = input("Please enter your username: ")

with open(filename,'a') as obj:
    obj.write("Username: " + username+"\n")
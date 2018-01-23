# 10-11. Favorite Number: Write a program that prompts for the user’s favorite number. 
# Use json.dump() to store this number in a file. 
# Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s _____.”

import json

filename = 'usernum.json'

usernum = input("Whats your fav number?: ")
with open(filename,'a') as obj:
    json.dump(usernum,obj)
    print("Your fav num has been saved!")

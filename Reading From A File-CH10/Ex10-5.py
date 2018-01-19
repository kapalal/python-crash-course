# 10-5. Programming Poll: Write a while loop that asks people why they like programming. 
# Each time someone enters a reason, add their reason to a file that stores all the responses.

responses = 'responses.txt'

while True:
    with open(responses,'a') as obj:
        name= input("Please enter your name: ")
        reason =input("Why you like programming?: ")
        obj.write("User: " + name + "\n")
        obj.write("Reason: " + reason + "\n")
        obj.write("----------------------\n")
        check =input("Press X to quit the poll")
        if check == "X":
            break
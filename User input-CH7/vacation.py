#7-10. 
# Dream Vacation: Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll.

response = {}

polling_state= 'on' 

while polling_state == 'on': 
    user= input("Please enter your username: ")
    question= input("If you could visit one place in the world, where would you go? ")

    response[user]=question

    repeat= input("Would like to let someone else take the poll?? ")
    if repeat =='no':
        polling_state= 'off'
        continue
print("\n--- Poll Results---")
for user,question in response.items():
    print("The user: " + user + " answered " + question)    


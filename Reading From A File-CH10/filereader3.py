filename = '/etc/hosts'

with open(filename) as file:
    lines= file.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

#print(pi_string)
#print(len(pi_string))


birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
    print(birthday)
else:
    print("Your birthday does not appear in the first million igits")
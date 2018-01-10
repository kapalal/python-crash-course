
age = input("Whats your age?")

poll_flag = 'on'

while poll_flag == 'on':
    polled_age= int(age)
    if polled_age < 3:
        print("Its free")
        poll_flag= 'off'
    elif polled_age >= 3 and polled_age <=12:
        print("the ticket is 10$")
        poll_flag= 'off'
    else:
        print("The ticke is 15$")
        poll_flag= 'off'

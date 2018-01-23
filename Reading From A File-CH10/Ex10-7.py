# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue 
# entering numbers even if they make a mistake and enter text instead of a number.


num1 = input("Enter a number: ")

num2 = input("Enter the second number: ")

while True:
    
    try:

        sum = int(num1) + int(num2)
    except ValueError:

        print("Sorry you can enter only a number")
    else:
        print(sum)
# 10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. 
# When you try to convert the input to an int, you’ll get a ValueError. 
# Write a program that prompts for two numbers. Add them together and print the result. 
# Catch the ValueError if either input value is not a number, and print a friendly error message. 
# Test your program by entering two numbers and then by entering some text instead of a numbe



num1 = input("Enter a number: ")

num2 = input("Enter the second number: ")

try:

    sum = int(num1) + int(num2)
except ValueError:

    print("Sorry you can enter only a number")
print(sum)
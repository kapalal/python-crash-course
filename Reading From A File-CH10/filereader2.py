filename = 'pi_digits.txt'

with open(filename) as file:
    for line in file:
        print(line.rstrip())
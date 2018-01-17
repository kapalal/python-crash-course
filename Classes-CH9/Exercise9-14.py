# 9-14. Dice: The module random contains functions that generate random numbers in a variety of ways. 
# The function randint() returns an integer in the range you provide. 
# The following code returns a number between 1 and 6:from random import randintx = randint(1, 6)Make a class Die with one attribute called sides, 
# which has a default value of 6. 
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times.Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die (object):
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self,count=1):
        #rolled = randint(1,self.sides)
        self.count = count
        if count > 1:
            for x in range(1,count):
                rolled = randint(1,self.sides)
                print("The dice with " + str(self.sides) + " sides"+ " rolled a : " + str(rolled))
        rolled = randint(1,self.sides)
        print("The dice with " + str(self.sides) + " sides"+ " rolled a : " + str(rolled))


dice = Die()
dice.roll_die(10)

dice2 = Die(10)
dice2.roll_die(10)            

dice3 = Die(20)
dice3.roll_die(10)
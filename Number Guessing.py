#random = to generate any random values
#math= mathametical functions under the module

import random
import math
# Taking Inputs
lower = int(input("Enter Lower number:- "))
 
# Taking Inputs
upper = int(input("Enter Upper number:- "))
 
# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
       round(math.log(upper - lower)),
      " chances to guess the integer!\n")
 
# Initializing the number of guesses.
count = 0
 
# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower):
    count += 1
 
    # taking guessing number as input
    guess = int(input("Guess a number:- "))
 
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
 
# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower):
    print("The number is ",x)
    print("Better Luck Next time!")
    
    

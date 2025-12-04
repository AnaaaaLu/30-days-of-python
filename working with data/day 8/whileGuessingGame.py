# Write a short guessing game program using a while loop. The user should 
# be prompted to guess a number between 1 and 100, and you should tell 
# them whether their guess was too high or too low after each guess. The 
# loop should keeping running until the user guesses the number correctly.

import random 

targetNumber = random.randint(1, 100)

guess = int(input("Enter a number beetween 1 and 100: "))

while guess != targetNumber:
    if guess > targetNumber:
        print("Too high!")
    else: 
        print("Too Low!")
    
    guess = int(input("Try Again!"))

print("You guessed correctly!")
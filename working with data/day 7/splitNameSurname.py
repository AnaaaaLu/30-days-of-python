# Ask the user to enter their given name and surname in response to a 
# single prompt. Use split to extract the names, and then assign each 
# name to a different variable. For this exercise, you can assume that 
# the user has a single given name and a single surname.

names = input("Please enter your full name: ").split()

name = names[0]
surname = names[1]

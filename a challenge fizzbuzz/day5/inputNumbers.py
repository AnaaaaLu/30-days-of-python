#3) Ask the user to enter a number. Tell the user whether the number 
# is positive, negative, or zero.

number = float(input("Please write a number: "))

if number == 0:
    print("Your number equals to zero")

elif number > 0:
    print("Your number is positive")

else:
    print("Your number is negative")
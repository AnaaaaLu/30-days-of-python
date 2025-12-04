# Using one of the examples from earlier — or a solution entirely of your 
# own—create a program that prints out every prime number between 1 and 
# 100.

dividend = int(input("Please enter a number: "))

for divisor in range(2, dividend):
    if dividend% divisor == 0:
        print(f"{dividend} is not prime!")
        break
else: 
    print(f"{dividend} is prime!")
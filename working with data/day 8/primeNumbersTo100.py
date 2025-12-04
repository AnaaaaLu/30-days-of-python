# Using one of the examples from earlier — or a solution entirely of your 
# own—create a program that prints out every prime number between 1 and 
# 100.

primes = []

for dividend in range(2,101):
    for divisor in range(2, dividend):
        if dividend % divisor ==0:
            break
    else: 
        primes.append(str(dividend))

print(", ".join(primes))
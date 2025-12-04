# Use a loop and the continue keyword to print out every character in the 
# string "Python", except the "o".

# Remember that strings are collections, and they are iterable, so you 
# can iterate over the string, which will yield one character at a time.

string = "Python"

for character in string:
    if character == "o":
        continue

    print(character)
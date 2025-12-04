# Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using 
# the join method. Remember that you can only join collections of strings, 
# so you’re going to need to do some initial processing of the list of 
# numbers.

numbers = [1, 2, 3, 4, 5]
formattedNumbers = []

for number in numbers:
    formattedNumbers.append(str(number))

print(" | ".join(formattedNumbers))
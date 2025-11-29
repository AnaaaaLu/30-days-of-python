#2) Try to use the is operator or the id function to investigate the 
# difference between this:

#   numbers = [1, 2, 3, 4]
#   new_numbers = numbers + [5]

#And this:

#   numbers = [1, 2, 3, 4]
#   numbers.append(5)

#Are new_numbers and numbers the same thing? What about numbers 
# before and after we append 5?

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

print(id(numbers) == id(new_numbers))

numbers2 = [1, 2, 3, 4]
numbers2.append(5)
print(id(numbers2) == id(numbers2))

#running the code we can se that the id numbers are different in the 
# first code, because you are creating a new collection not just 
# appending the code, as in the second one
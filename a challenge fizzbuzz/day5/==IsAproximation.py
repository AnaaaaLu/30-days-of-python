#1) Try to approximate the behaviour of the is operator using ==. 
# Remember we have the id function for finding the memory address 
# for a given value, and we can compare memory addresses to check 
# for identity.

list_1 = [1, 2, 3, 4, 5]
list_2 = list_1

print(id(list_1) == id(list_2)) 
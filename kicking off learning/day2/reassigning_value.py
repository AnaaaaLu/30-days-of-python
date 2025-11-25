#Investigate what happens when you try to assign a value to a variable 
# that you’ve already defined. Try printing the variable before and after 
# you reuse the name.

name = input("Please write your name: ")
age = input("Plese write your age: ")
print("Are those values correct? " + name + ", " + age)

name = input("Please write a different name: ")
age = input("Plese write another age: ")
print("Are those values correct? " + name + ", " + age)
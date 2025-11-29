#For the employees above, print out those who are earning an hourly wage 
# above average.

#Hint: you can use a for loop and two variables to keep track of the total 
# wage and the number of employees. Then, use the two variables to calculate the average. Finally, add another loop that goes through the employees list again and prints out only those who have an hourly wage above the calculated average.

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

total = 0
count = 0

for employee in employees:
    total += employee[2]

average_wage = total / len(employees)

for employee in employees: 
    if employee[2] > average_wage:
        print (f"{employee[0]} earns more than average")
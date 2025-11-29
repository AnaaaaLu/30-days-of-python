#Write a program to determine whether an employee is owed any 
# overtime. You should ask the user how many hours the employee 
# worked this week, as well as the hourly wage for this employee.
#
#If the employee worked more than 40 hours, you should print a 
# message which says the employee is due some additional pay, as 
# well as the amount due. The additional amount owed is 10% of the 
# employees hourly wage for each hour worked over the 40 hours. In 
# effect, the employees get paid 110% of their hourly wage for any 
# overtime.

name = input(f"Please enter your employee's name: ").strip().title()
hourly_wage = float(input(f"What is {name} hourly wage? "))
hours_worked = float(input(f"How many hours {name} worked in this week? "))

if hours_worked > 40:
    regular_pay = float(40 * hourly_wage)
    overtime_pay = float((hours_worked - 40) * hourly_wage * 1.1)
    earnings = float(regular_pay + overtime_pay)

    print(f"{name} is owed ${earnings:.2f} this week")
else:
    earnings = float(hourly_wage) * float(hours_worked)
    
    print(f"{name} earned ${earnings:.2f} this week.")

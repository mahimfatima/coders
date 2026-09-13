hours = float(input("Enter hours worked: "))
rate = float(input("Enter rate per hour: "))

if hours <= 40:
    salary = hours * rate
else:
    normal_salary = 40 * rate
    overtime_hours = hours - 40
    overtime_salary = overtime_hours * rate * 1.5

    salary = normal_salary + overtime_salary

print("Salary =", salary)
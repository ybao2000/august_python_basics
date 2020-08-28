# Exercise 3.1: Rewrite your pay computation to give the employee 1.5 times 
# the hourly rate for hours worked above 40 hours
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0 <= 40 * 10 + 5 * 10 *1.5, 45 * 10 + 5 * 10 * (1.5-1)
strHours = input("Enter Hours: ")
strRate = input("Enter Rate: ")
hours = float(strHours)
rate = float(strRate)

# if hours <= 40: # less than or equal to 40
#   pay = hours * rate
# else: # over 40, split your hours into 40 + (hours-40) = hours
#   # pay = 40 * rate + (hours-40) * rate * 1.5
#   pay = hours * rate + (hours -40) * rate * 0.5
pay = hours * rate # regular pay
if hours > 40:
  pay = pay + (hours - 40) * rate * 0.5
print("Pay:", pay)
# Exercise 3.2: Rewrite your pay program using try and except 
# so that your program handles non-numeric input gracefully 
# by printing a message and exiting the program. 
# The following shows two executions of the program
# Enter Hours: 45
# Enter Rate: ten
# Error! Please enter numeric input
# EnterHours: fifty
# Error! Please enter numeric input
try:
  strHours = input("Enter Hours: ")
  hours = float(strHours)
  strRate = input("Enter Rate: ")   
  rate = float(strRate)
  
  pay = hours * rate # regular pay
  if hours > 40:
    pay = pay + (hours - 40) * rate * 0.5
  print("Pay:", pay)
except:
  print("Error! Please enter numeric input")
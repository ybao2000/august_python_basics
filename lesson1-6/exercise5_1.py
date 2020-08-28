# Write a program which repeatedly reads numbers 
# until the user enters “end”. Once “end” is entered, 
# print out the total, count, and average of the numbers. 
# If the user enter anything other than a number, 
# detect their mistake using try and except 
# and print an error message and skip to read the next number.
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: end
# 16 3 5.333333333333333
total = 0
count = 0
while True:   # infinite loop
  val = input("Enter a number: ")
  if val == "end":
    break # jump out of the while loop
  try:
    ival = int(val)
    total = total + ival  # sum up
    count = count + 1   # increase by 1
  except:
    print("Invalid input")

average = 0
if count > 0:
  average = total/count
print(total, count, average)    
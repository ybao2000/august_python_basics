# write a program that prompts 
# for a list of numbers (as exercise 1) 
# and at the end prints out both the maximum 
# and minimum of the numbers instead of the average.
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: end
# 7 4
imax = None
imin = None
while True:   # infinite loop
  val = input("Enter a number: ")
  if val == "end":
    break # jump out of the while loop
  try:
    ival = int(val)
    # this is to update the imax
    if imax == None or ival > imax: # if imax is None (not initialize) or ival > imax
      imax = ival
    # update the imin
    if imin == None or ival < imin:
      imin = ival
  except:
    print("Invalid input")

print(imax, imin)
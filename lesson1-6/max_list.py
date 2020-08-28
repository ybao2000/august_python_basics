mylist = [1, 3, 5, 10, 21, 33, 100, 222, 33, 3, 32, 43, 5]
# mylist = [-1, -3, -2, -4, -5]
# mylist = []
# use for loop to get maximum
# max = mylist[0] # this means getting the fist number in the list
max = None
for num in mylist:
  # compare num with max
  # if num > max, then replace max
  # if max is None:
  #   max = num
  # if num > max:
  #   max = num
  if max == None or num > max:
    max = num
print("Max: ", max)
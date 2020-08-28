mylist = [1, 3, 5, 10, 21, 33, -1, 100, 222, 33, 3, 32, 43, 5]
# find the min for the list
min = None
for num in mylist:
  if min == None or num < min:
    min = num
print("Min: ", min)
# range function

# for num in range(1000): # this is exactly the same as [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ..., 999]
#   print(num)

# what is I want a range from 1000, 2000?
# for num in range(1000, 2001):
#   print(num)

# what is I want 100, 99, ..., 1?
# for num in range(100, 0, -1): # 100 is the starting number, 0 is the stop number (excluded), -1 means decrease
#   print(num)

# what if I want 1, 3, 5, ..., 99 (odd numbers)
# for num in range(1, 100, 2):
#   print(num)

# what if I want 99, 97, 95, ..., 1 
for num in range(99, 0, -2):
  print(num)

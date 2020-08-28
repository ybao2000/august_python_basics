val = input("Enter a number: ")
n = int(val)

while n >= 0: # this expresssion returns a bool, and if True, go inside the loop, otherwise( False), skip the loop
  print(n)
  n = n -1
  if n == 5:
    break # break means get out of the loop

print()
print(n)
print("End")
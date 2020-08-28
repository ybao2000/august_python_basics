val = input("please enter a number: ")
try:
  x = int(val)
  if x < 2:
    print('Below 2')
  elif x < 20:
    print('Below 20')
  else:
    print('Something else')    
except:
  print("invalid number")

print("Done")
grade = int(input("Please enter your grade: "))

if grade == 0:
  print("you are in pre-school")
elif grade <= 6:
  print("you are in elementary school")
elif grade <= 9:
  print("you are in junior high school")
elif grade <= 12:
  print("you are in senior high school")
# else:
#   print("you are in senior high school")
print("Done")
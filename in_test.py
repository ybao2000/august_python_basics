# in is a reserved word, which is check if one string is inside another another

a = "apple bee"
b = "beet"
res = b in a  # this one is to check if b is in a
print(res)

# difference between True and true
# not is another reseved word, which is to revert the result
res2 = b not in a
print(res2)

if b in a:
  print("'"+b+"'", "is in", "'"+a+"'")  # what is the result
  print(f"'{b}' is in '{a}'")  # f-string, string with format, {variable} will be replaced by the value of the variable
else:
  print("'"+b+"'", "is not in", "'"+a+"'")
  print(f"'{b}' is not in '{a}'")
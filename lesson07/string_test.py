f = "apple"
g = "banana"
print(f+g)  # this + means put two string together, concatenate
a = "123"
b = 4
# print(a+b)
# exercise: how to concatenate a and b
# I want "1234" from a and b
print(a + str(b)) # you have to convert b first

# sometime you want "123" + 4 => 127
print(int(a) + b)

# use * to make duplicates of string
print(f*5)
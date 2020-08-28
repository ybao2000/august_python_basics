a1 = "apple"
a2 = "APPLE"
a3 = "Apple"

amax = max(a1, a2, a3)
amin = min(a1, a2, a3)

print("max", amax, "min", amin)

# print(a1.__dir__())

# replace, split, join, capitalize, count, lower, upper, startswith, endswith, isascii, islower, isupper, isdecimal, isdigit, isnumeric
a = "Hello World"
a = a.replace("o", "#") # all methods of string will return a new string
print(a)

a = a.split()
print(a)

a = "***".join(a) # this is going to join all items in the list together, with the " " as the separator
print(a)

n = a.count('l')
print(n)

a = a.lower().upper()
print(a)

r = a.startswith("HELL")
print(r)

a = "123"
print(a.isalpha())
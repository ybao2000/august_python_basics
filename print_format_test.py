# I want to print some a = ?, b = ?, c = ? and b = ?
a = 1
b = "Frank"
c = True
d = 1.4

# 1: int, "Frank": str, True: bool, 1.4: float
print(a, b, c, d)
print(1, ": int", b, ": str", c, ": bool", d, ": float")

# in this situation, it's better to use format 
# (certainly in python 3.8, we have better way to do it)
# {0}, {1}, {1}, {2}... these are called placeholder
print('{0}: int, "{1}": str, {2}: bool, {3}: float'.format(a, b, c, d))

# f-string is best way to do format (format)
# and this is only avaible after python 3.6
print(f'{a}: int, "{b}": str, {c}: bool, {d}: float')

print('{a}: int, "{b}": str, {c}: bool, {d}: float')

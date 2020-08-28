t = type(99/1)  # / always return float, no matter what is the input
print(t)

t = 99/2
print(type(t), t)

t = round(99/2)
print(type(t), t)

a = 3.1415
b = str(a)
print(type(a), a)
print(type(b), b)

a = "3.15"
b = float(a)

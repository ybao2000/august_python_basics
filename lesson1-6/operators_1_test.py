# a = 3

# # 3 = a
# b = 3 + 4
# c = 3 - 4
# d = 3 * 4
# e = 3/4

# print(a, b, c, d, e)

# f = 5 % 4  # modula, remainder
# print(f)

# g = 5 ** 5 # 5 * 5 * 5 * 5 *5
# print(g)

# h = 7 // 4 # write some comment
# print(h)

# print(4>3, 4<3, type(4), type(4.0), 4==4.0) # be CAREFUL when you compare floats!

a1 = 0.9
a2 = 0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1

print(a1, a2, a1==a2, a1 != a2, a1 >= a2 and a1 <= a2)


# def tolerance
tol = 1e-8 # this means 0.00000001, 10^-8
print(not abs(a1-a2) < tol)


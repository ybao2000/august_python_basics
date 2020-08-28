fruits = ["apple", "banana", "peach", "pear", "cherry", "watermelon"]

# print(fruits.__dir__())

# useful methods
# clear, append, insert, extend, pop, remove, index, reverse, sort

# fruits.clear()
# print(fruits)

# fruits.append("orange")
# print(fruits)

# fruits.insert(1, "honeydew")
# print(fruits)

a = [1, 3, 4, 5]
b = [2, 3, 4, 10, 22, 3, 10, 20]
# a.extend(b) # this ones is different from +
# c = a + b # expression changes nothing, it just return a new list, but you didn't assign the new list to any object
# a.extend(b)
# print(c == a, c is a) # if you don't understand is, it's fine, but you have to understand ==
# elem = a.pop()
# print(a)
# print(elem)
# b.remove(5) # don't ever remove an element which is not in the list
# print(b)
# i = b.index(11)
# print(i)

# how to check if a value is in the list??
# res = 5 in b
# print(res)
# if 5 in b:
#   b.remove(5)
# b.reverse()
# print(b)

b.sort()
print(b)
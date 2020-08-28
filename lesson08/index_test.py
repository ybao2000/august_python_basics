sub = [2, [7, 20]]
numbers = [1, 5, sub, 13, 59, 28, 30]
l = len(numbers)
print(l)

s = numbers[l-5]
print(s)

# index - exact the same meaning in string
# index is a integer, starting is 0, increases sequentially

# list is mutable, that means, you can directly use [index]
numbers[2] = 3
print(numbers)
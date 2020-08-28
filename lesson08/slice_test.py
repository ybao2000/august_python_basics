weird_num = [2, [7, 20]]
numbers = [1, 5, weird_num, 13, 59, 28, 30, 30, 31, 32, 34]

# slice: first number is starting index, 
# second is ending index
sub = numbers[0:7]  
print(sub)

sub2 = numbers[2:100]
print(sub2)

sub3 = numbers[:8]
print(sub3)


sub4 = numbers[5:]
print(sub4)

sub5 = numbers[:]
print(sub5)

sub6 = numbers
print(sub6)

# list ==, is what is the difference ???
print(sub5 == sub6, sub5 is sub6, sub6 is numbers)

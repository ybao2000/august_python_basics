text = "Hello world"

# be careful: the ending index is not included
sub = text[0:7]  # slice: 0 is the starting index, 7 is the ended index (excluded)
print(sub)

# the good thing is, if the ending index is out of range, it's ok (it will just stop at the end)
sub2 = text[2:100]
print(sub2)

# if starting index is 0, it can be omitted
sub3 = text[:8]
print(sub3)

# if you want from starting index to end, you don't have to provide ending index
sub4 = text[5:]
print(sub4)

sub5 = text[:]  # this is meaningless
sub6 = text
text = "another text"
print(sub5, sub6) # so what is the difference between sub5 and sub6???

# is and ==, what is the difference???

print(sub5 == sub6, sub5 is sub6)
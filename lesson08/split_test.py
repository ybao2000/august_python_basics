notation = "Funny Cat Garfield Dressed As Easter Bunny"
l = notation.split()  # this one is to convert the string into list
# print(l)
# create another list
l2 = []
for note in l:  # iterate throught the element
  # print(note[0], end='')  # pritn the first letter of the element, end='' means no new lines
  l2.append(note[0])
# this one is the famouse FCGDAEB (music circle of 5th)

print(l2)

str2 = "-".join(l2)  # this means join all elements in l2 together, with separator of something ""
print(str2)
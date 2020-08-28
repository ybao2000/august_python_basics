text = "Hallo world"
l = len(text)
print(l)
c = text[l-5] # we use [index] to get the character at the index position
print(c)

# learned index
# index is a integer, starting from 0, and increase sequentially

# string is immutable, means, cannot be changed
# text[1] = 'o'
# i really want a string from text, with char in index 1 as o
# "Hollo world"

# this is the trick to replace a character at a certain position
position = 2
another = text[:position] + "o" + text[position+1:]   
print(another)

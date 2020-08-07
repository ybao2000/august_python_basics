name1 = "Frank's computer"  # in here, " is the deliiter, ' is a character
name2 = '"War and Peace"'   # in here ' is the delimiter, " is a character
height = '''5'3"'''          # if a string contains both ' and ",  you can use triple single quote
# or you can use triple double quote
height = """5'3"""
print(name1, name2, height)


# triple single quote, triple double quote usually is for multi-line string
poem = """Twinkle Twinle Little Start
How I wonder what you are?
Up above the world so high
Like a diamond in the sky"""
print(poem)


# if you want want single quote/double quote for 5'3"
# escape \', \"
height = '5\'3"'
height2 = "5'3\""
print(height, height2)
# escape \n - this means, new line
poem2 = 'Twinkle Twinle Little Start\nHow I wonder what you are?\nUp above the world so high\nLike a diamond in the sky'
print(poem2)

a = 7
astr = str(7)
print(a, astr, type(a), type(astr))


# r-string (raw-string) don't do any conversion, keep the original string
poem3 = r'Twinkle Twinle Little Start\nHow I wonder what you are?\nUp above the world so high\nLike a diamond in the sky'
print(poem3)

info = "My name is {name}. I am {age} year’s old, {height} tall. I am a {gender}."
print(info)
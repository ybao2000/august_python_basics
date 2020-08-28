# Given the following string
# str1 = <span class="Trsdu(0.3s) Fw(500)" data-reactid="37">82.56'

# Use find and string slicing to extract the portion of the string after the > character 
# and then use the float function to convert the extracted string into a floating point number

# python could be use as web crawlers - a tool to collect information from www websites

str1 = """<span class="Trsdu(0.3s) Fw(500)" data-reactid="37">82.56333'"""
# print(str1)
# strip the 82.56 from str1

# step 1: find the index of >
index = 0
while index < len(str1):
  if str1[index] == ">":
    break
  index = index + 1

# use slice [start:end]
word = str1[index+1:].replace("'", "")
print(word)
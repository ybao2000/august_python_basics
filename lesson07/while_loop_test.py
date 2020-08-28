text = "Hello world"

# exercise:use while loop to print the same thing as in for_loop_test.py
# index, len() to get the length

# while three thing
# step 1: initialize iterate variable
# step 2: while a condition which is related to the iterate variable
# step 3: inside the block, modify the iterate variable
# length = len(text)
index = 0
while index < len(text):
  print(text[index])
  index = index + 1

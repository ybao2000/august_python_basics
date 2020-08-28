# Print test with name, age, height, gender:
#  def print_info(name, age, height, gender):

#  Test case:
#  print_info("Sam", 9, '''5'3"''', "girl")
#  Output:
# My name is Sam. I am 9 year’s old, 5'3" tall. I am a girl.

def print_info(name, age, height, gender):
  print(f"My name is {name}. I am {age} year’s old, {height} tall. I am a {gender}.")


name = "Rebecca"
age = 12
height = '''5'5"'''
gender = "lady"
print_info(name, age, height, gender)

def max_of_three(num1, num2, num3):
  # n2 = max_of_two(num1, num2)
  # return max_of_two(n2, num3)
  # return max_of_two(max_of_two(num1, num2), num3)
  return max(num1, num2, num3)

def max_of_two(num1, num2):   # colon after function
  # always indent inside function
  # always put colon after if condiction:
  if num1 >= num2:   
    return num1
  else:   # colon after else
    return num2

print(max_of_three(1, 3, 5))
# Write a function called compute_price function 
# that takes a quantity and returns the 
# price according to the following price break:
# 	below 10: 		2.99/each
# 	below 100:     		2.59/each
# 	below 1000:   		1.99/each
# 	1000 and above: 	1.59/each
strQty = input("Enter quantity: ")
qty = float(strQty)

def compute_price(qty): # function behaves as a template
  if qty < 10:
    unit_price = 2.99
  elif qty < 100:
    unit_price = 2.59
  elif qty < 1000:
    unit_price = 1.99
  else:
    unit_price = 1.59
  return unit_price * qty

# call it 
price = compute_price(qty)
print("Total Price: ", price)
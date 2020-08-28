# Rewrite your price computation with a function 
# called compute_price which takes two parameters (qty, unit_price)

# Enter quantity: 15
# Enter unit price: 1.99
# Total Price: 26.865

# Enter quantity: 13.6
# Enter unit price: 0.99
# Total Price: 12.1176
strQty = input("Enter quantity: ")
strUnitPrice = input("Enter unit price: ")

qty = float(strQty)
unit_price = float(strUnitPrice)

# this is the defintion of the function
def compute_price(qty, unit_price):
  if qty <= 10:
    p = qty * unit_price  # this price is a local price (inside the function)
  else:
    p = qty * unit_price * 0.9
  return p

# here we call the function
price = compute_price(qty, unit_price)  # this price is global price 
print("Total Price: ", price)
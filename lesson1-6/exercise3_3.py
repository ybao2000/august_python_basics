# Rewrite your price computation to give 
# the customer 10% off if the quantity is above 10

strQty = input("Enter quantity: ")
strUnitPrice = input("Enter unit price: ")

qty = float(strQty)
unit_price = float(strUnitPrice)

if qty <= 10:
  price = qty * unit_price
else:
  price = qty * unit_price * 0.9

print("Total Price: ", price)

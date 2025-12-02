# A grocery store wants to calculate the final bill for a customer. The store has 3 products: rice, sugar, and oil. Each product has a fixed price per kilogram:
# Rice: ?45 per kg
# Sugar: ?40 per kg
# Oil: ?130 per kg
# Assume a customer bought:
# 3 kg of rice
# 2.5 kg of sugar
# 1.8 kg of oil
# Your task:
# Use variables to store the prices and quantities.
# Use appropriate data types.
# Calculate and print the total price for each item and the final total bill.
# Show the total bill as an integer and also as a string.
# Convert the float values where needed using explicit conversion.
# Use random number generation to add a random ?5–?10 delivery charge.
# Show the final bill amount including delivery charge.


rice_price=45
sugar_price=40
oil_price=130

rice_qty=3
sugar_qty=2.5
oil_qty=1.8

total_rice_price=rice_price*rice_qty
total_sugar_price=sugar_price*sugar_qty
total_oil_price=oil_price*oil_qty

print("Total rice price: ",total_rice_price)
print("Total sugar price: ",total_sugar_price)
print("Total oil price: ",total_oil_price)

total_bill=total_rice_price+total_sugar_price+total_oil_price
print("Total Bill: ",total_bill)

total_bill_int=int(total_bill)
print("Total bill in integer: ",total_bill_int)

total_bill_str=str(total_bill)
print("Total bill is ",total_bill_str," rupees")

import random
delivery_charge=random.randint(5,10)

total_bill_dlvry=total_bill+delivery_charge

print("Delivery Charge: ",delivery_charge)
print("Total bill with delivery charge: ",total_bill_dlvry)
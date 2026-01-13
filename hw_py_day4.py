# You are managing a small grocery store. You keep lists of items sold in three sections: fruits, vegetables, and beverages.
# Create separate lists for each section with at least 3 items.
# Add a new item to the fruits list.
# Insert a new item at the second position of the vegetables list.
# Remove the last item from the beverages list.
# Combine all three lists into a nested list called inventory.
# Use slicing to print only the first two fruits.
# Use negative indexing to access the last item from the vegetables list.
# Create a list of lengths of all items in the fruits list using list comprehension.
# Check if "Water" is in the beverages list.
# Finally, create a tuple of the first item from each section.




fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Potato", "Spinach"]
beverages = ["Juice", "Soda", "Water"]


fruits.append("Mango")


vegetables.insert(1, "Tomato")  


beverages.pop()


inventory = [fruits, vegetables, beverages]


print("First two fruits:", fruits[:2])


print("Last vegetable:", vegetables[-1])

fruit_name_lengths = [len(item) for item in fruits]
print("Lengths of fruit names:", fruit_name_lengths)


print("Is 'Water' in beverages?", "Water" in beverages)


first_items_tuple = (fruits[0], vegetables[0], beverages[0])
print("Tuple of first items:", first_items_tuple)


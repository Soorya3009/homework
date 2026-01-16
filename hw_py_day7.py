# You are helping a small pet store keep track of their pet supplies for a daily report. 
# The store wants a simple Python program to list the names of items in stock and show how many items they have. 
# Your task is to create a complete application that does the following steps in order:

# Create the Empty List:
#     The program starts with an empty list inventory = [] to hold the names of pet supplies as strings, making it simple for beginners.
# Add Items with add_item Function:
#     The add_item(item) function takes one item name (a string) and adds it to the inventory list using append().
#     In the main() function, it adds "dog food", "cat toy", "bird cage", and "fish tank" by calling add_item four times.
# Count Items with count_items Function:
#   The count_items(items) function uses recursion to count the number of items in the list.
# Base Case: If the list is empty (not items), return 0.
# Recursive Step: Count 1 for the current item and add the result of calling count_items on the rest of the list (items[1:]).
#           This is called in main() to get the total number of items.
# Display Items with Lambda Function:
#      A lambda function show_item = lambda item: print(f"Item in Stock: {item}") formats each item with the prefix "Item in Stock: ".
#       A for loop in main() iterates over the inventory list to display each item using the lambda function.
# Main Function and Running the Program:
#     The main() function puts all steps together:
#     Adds the four items using add_item.
#     Displays the items using the lambda function in a loop.
#     Counts and displays the total number of items using count_items.
#     The program ends with a direct main() call, keeping it simple for students.

inventory=[]

def add_item(item):
    inventory.append(item)

def count_items(items,index=0):
    if not items:
        return 0
    return 1+ count_items(items[1:])
show_item = lambda item: print(f"Item in Stock: {item}")


add_item("dog food")
add_item("cat toy")
add_item("bird cage")
add_item("fish tank")
print ("Items in the inventory list")
for x in inventory:
    show_item(x)
total = count_items(inventory)
print("\nTotal items in stock:", total)

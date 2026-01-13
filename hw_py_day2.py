# Write a Python program that does the following:
# Store a short paragraph about a Python course using a multiline string.
# Display the length of the paragraph (number of characters).
# Display the first and last characters in the paragraph.
# Slice and print a short preview: the first 50 characters.
# Replace all occurrences of the word "Python" with "PYTHON" (in all caps).
# Convert the entire paragraph to lowercase.
# Remove any extra whitespaces from the start or end.
# Split the paragraph into individual words and print the list.
# Check if the word "course" exists in the paragraph. Print a message if found.
# Display the final message:
# "The course description is {} characters long and has {} words." using the format() method.

para="""Python is  powerfull language. Python is object-oriented programming language."""

print("\nLength of paragraph:",len(para))

print("\nFirst Character:",para[0])
print("Last Character:",para[-1])

print("\nPreview:",para[:50])

paragraph = "Python"
print(paragraph.replace("Python", "\nPYTHON"))


print("\nLowercase: ",para.lower())

print(para.strip())

print("\nList of word:",para.split())

a="\nCourse" in para
print(a)

message="The course descripition is {} character long and has {} word."
print("\nLength of message:",len(message))
"""wap to convert all the characters into uppercase and lowercase and climinate duplicate letters 
from a given sequence.Use map() function"""

# Program to convert characters into uppercase and lowercase
# and eliminate duplicate letters using map()

sequence = ['a', 'b', 'c', 'a', 'B', 'c', 'd']

# Remove duplicate letters
unique = list(dict.fromkeys(sequence))

# Convert characters to uppercase
uppercase = list(map(lambda x: x.upper(), unique))

# Convert characters to lowercase
lowercase = list(map(lambda x: x.lower(), unique))

print("Original sequence:", sequence)
print("After removing duplicates:", unique)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

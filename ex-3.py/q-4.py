# string is symmetrical or palindrome

s = input("Enter a string")
mid = len(s) // 2

if len(s) % 2 == 0:
    first = s[:mid]
    second = s[mid:]
else:
    first = s[:mid]
    second = s[mid+1:]

if first == second:
    print("The string is Symmetrical")
else:
    print("The string is not Symmetrical")

if s == s[::-1]:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")

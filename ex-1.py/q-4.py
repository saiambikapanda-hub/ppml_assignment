import math

# Enter coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
d = b**2 - 4*a*c

# Find roots
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are:", root1, "and", root2)

elif d == 0:
    root = -b / (2*a)
    print("Both roots are equal:", root)

else:
    print("Roots are imaginary")
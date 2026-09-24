import math

try:
	a = float(input("Enter first side: "))
	b = float(input("Enter second side: "))
	c = float(input("Enter third side: "))

	if a <= 0 or b <= 0 or c <= 0:
		raise ValueError("Side lengths must be positive.")
	if a + b <= c or a + c <= b or b + c <= a:
		raise ValueError("These side lengths cannot form a triangle.")

	s = (a + b + c) / 2
	area = math.sqrt(s * (s - a) * (s - b) * (s - c))
	print("Area of the triangle =", area)
except ValueError as error:
	print("Error:", error)
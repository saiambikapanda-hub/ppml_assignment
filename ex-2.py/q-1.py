percentage  = float(input("Enter a percentage"))
if percentage >= 90 and percentage <= 100:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B+")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
elif percentage >= 0:
    print("Grade: F")
else:
    print("Invalid percentage!")

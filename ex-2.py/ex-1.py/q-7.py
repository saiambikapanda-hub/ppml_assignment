# Enter time in minutes
minutes = int(input("Enter time in minutes: "))

# Convert into hours and remaining minutes
hours = minutes // 60
remaining_minutes = minutes % 60

print("Time =", hours, "hours", remaining_minutes, "minutes")
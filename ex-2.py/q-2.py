num = int(input("Enter a 5 digits number:"))

d1 = num // 10000
d2 = (num // 1000)%10
d3 = (num // 100)%10
d4 = (num // 10)%10
d5 = num%10

print("Digits at odd locatins are:")
print(d1)
print(d3)
print(d5)

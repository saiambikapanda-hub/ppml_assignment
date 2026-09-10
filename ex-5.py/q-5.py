"""wap to enter two sets and perform all the set operation on it """

def set_operations(s1, s2):
    print("Union:", s1 | s2)
    print("Intersection:", s1 & s2)
    print("Difference (S1 - S2):", s1 - s2)
    print("Difference (S2 - S1):", s2 - s1)
    print("Symmetric Difference:", s1 ^ s2)


s1 = eval(input("Enter first set: "))
s2 = eval(input("Enter second set: "))

set_operations(s1, s2)

#List of 20 elements increase the odd value elemnts by 5


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
       11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


for i in range(len(lst)):
    if lst[i] % 2 != 0:
        lst[i] = lst[i] + 5

print("Updated list:", lst)

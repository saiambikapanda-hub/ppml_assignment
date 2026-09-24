
def even_values(lst):
    even_list = []
    
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
    
    return even_list


numbers = [10, 15, 22, 31, 40, 53, 64, 71, 80, 91]

new_list = even_values(numbers)

print("Original list:", numbers)
print("Even values:", new_list)

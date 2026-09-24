#second largest and second smallest element in list of 10 integer without using sort function

numbers = [10, 25, 5, 40, 15, 30, 8, 50, 20, 35]

smallest = float('inf')
second_smallest = float('inf')

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:

    
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
        
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)

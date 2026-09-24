#create two list and print both lists one element from each list combined at a time


list1 = [10, 20, 30, 40, 50]


list2 = ["Apple", "Banana", "Mango", "Orange", "Grapes"]


for num, word in zip(list1, list2):
    print(num, word)

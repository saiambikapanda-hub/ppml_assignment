#Even length words in a string

s = input("Enter a string")
words = s.splits()

print("Even length words are:")
for word in words:
    if len(word) % 2 == 0:
        print(word)

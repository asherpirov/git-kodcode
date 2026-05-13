user_input = input("enter a string: ")
count = 0
for i in user_input:
    if i == "a" or i == "e" or i == "u" or i == "i" or i == "o":
        count += 1
print(f"the count of vowels is: {count}")
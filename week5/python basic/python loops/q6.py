accumulator = ""

user_input = input("enter a string: ")

for i in range(len(user_input) - 1, -1, -1):
    accumulator += user_input[i]

print(accumulator)
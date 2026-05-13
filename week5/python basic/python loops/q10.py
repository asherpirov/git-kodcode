string = input("enter a string: ")
flag = True
for char in string:
    if not char.isalnum():
        flag = False
        break
print(flag)



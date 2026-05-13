high_num = 0
while True:
    number = int(input("enter a number: "))
    if number == 0:
        break
    elif number > high_num:
        high_num = number

print(f"the highest number is {high_num}")

number = int(input("enter a number: "))
count = 0

while number > 0:
    last_digit = number % 10
    if last_digit % 2 == 0:
        count += 1
    number = number // 10

print(f"you have {count} even digits ")
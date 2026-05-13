number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))
number3 = int(input("enter the third number: "))

positive_count = (number1 > 0) + (number2 > 0) + (number3 > 0)

print("Number of positive numbers:", positive_count)
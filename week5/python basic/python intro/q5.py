number = float(input("enter float number: "))

integer_part = int(number)

fraction_part = number - integer_part

print("Integer part:", integer_part)
print("Fractional part:", round(fraction_part, 2))
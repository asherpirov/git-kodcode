age = int(input("enter your age: "))
if 0 > age < 120:
    print("Invalid")
elif 0 < age < 12:
    print("Child")
elif 13 < age < 17:
    print("Teen")
else:
    print("Adult")
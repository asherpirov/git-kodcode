PASSWORD = "abc123456"
password = input("enter password: ")

if password == PASSWORD:
    print("Access Granted")
elif password != PASSWORD and len(password) < 8:
    print("Too short")
else:
    print("Wrong password")

y = float(input("enter coordinate(y): "))
x = float(input("enter coordinate(x): "))

if (10 < x < 50) and (20 < y < 80):
    print("Inside the rectangle")
elif (10 <= x <= 50) and (20 <= y <= 80):
    print("On the edge")
else:
    print("Outside the rectangle")
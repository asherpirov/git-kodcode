age = int(input("Enter your age: "))
vip_input = input("Do you have a VIP card? (yes/no): ")

VIP_card = vip_input == "yes"

if age < 16:
    print("Rejected")

elif (age > 18 and VIP_card) or (age in [19, 20, 21]):
    print("Allowed")

else:
    print("Rejected")


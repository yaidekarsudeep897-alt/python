
rent=int(input("Enter the room rent : "))
food=int(input("Enter the amount of food ordered : "))
electricity_spend=int(input("Enter the total electricity spend : "))
bill_per_unit=int(input("Enter the charge per unit : "))
persons=int(input("Enter the persons living in room : "))

total_bill=electricity_spend*bill_per_unit

output=(rent + food + total_bill)// persons

print(output)


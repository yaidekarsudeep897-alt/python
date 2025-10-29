#Write a program to check if someone is eligible for a bus pass. 
# If they are below 5 years, the bus pass is free. If they are 60 years or older,
#  they get a senior citizen discount. Otherwise, they pay the full price.

name=input("Enter the name :")
gender=input("Enter the gender :")
age=int(input("Enter the age :"))

if gender=="female":
    print("The bus pass is free")
else:
    if age<5:
        print("Bus pass is free")
    elif age>=60:
        print("senior citizen discount")
    else:
        print("pay the full price")

    
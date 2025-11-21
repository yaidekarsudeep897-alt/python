import random

while True:
    choice=input("Rolling the Dice?(yes/no):").lower()
    if choice=="yes":
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"({die1},{die2})")
    elif choice=="no":
        print("Thank for Playing")
        break
    else:
        print("Invalid Choice! Try again")
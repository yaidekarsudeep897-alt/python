def menu():
    print("### Banking SyStem ###")
    print("1, Check Balance")
    print("2, Deposit")
    print("3, Withdraw")
    print("4, Exit")

balance=0

while True:
    choice=int(input("Enter yor choice(1-4):"))
    if choice==1:
        print("Balance:",balance)
    elif choice==2:
        amount=int(input("Enter the amount of Deposit:"))
        balance+=amount
    elif choice==3:
        amount=int(input("Enter amount to Withdraw:"))
        balance-=amount
    elif choice==4:
        print("Thank you for using my banking system")
        break
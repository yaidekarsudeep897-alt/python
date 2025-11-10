class Account:
    def __init__(self,id,holder_name):
        self.id=id
        self.holder_name=holder_name
        self._balance=0

    def check_balance(self):
        print(f"Balance:{self._balance}")
    def deposit (self,amount):
        self._balance+=amount
        print(f"Deposit successful. Update Balance:{self._balance}")
    def withdraw (self,amount):
        if self._balance>=amount:
            self._balance-=amount
            print(f"Withdraw successful. Update Balance:{self._balance}")
        else:
            print("Balance is less than ask")
    
class SavingAccount(Account):
    def calculate_interest(self):
        INTEREST_RATE=0.06 #6%
        interest=self._balance*INTEREST_RATE
        print(f"Interest:{interest}")
    
class CurrentAccount(Account):
    def withdraw (self,amount):
        OVERDRAFT_LIMIT=1000
        if self._balance+OVERDRAFT_LIMIT>=amount:
            self._balance-=amount
            print(f"Withdraw successful. Update Balance:{self._balance}")
        else:
         print("Ask is over limit")
class Bank:
    def __init__(self,name, city):
        self.name=name
        self.city=city
        self.__accounts={}

    def create_account(self, id, holder_name, acc_type):
        if acc_type == "savings":
            new_account = SavingAccount(id, holder_name)
        elif acc_type == "current":
            new_account = CurrentAccount(id, holder_name)
        else:
            print("Invalid account type.")
            return None

        self.__accounts[id] = new_account
        print("Account creation successful.")
        return new_account

    def get_account(self,id):
        if id not in self.__accounts:
            print("Account is not found")
            return None
        else:
            account=self.__accounts[id]
            print(f"\nID:{account.id}\nHolder_name:{account.holder_name}")
            return account
        
sbk=Bank("Canara Bank","HP Halli")
s1=sbk.create_account("1","Sudeep","savings")
c1=sbk.create_account("2","akash","current")

s1.deposit(100)
c1.deposit(350)

s1.withdraw(1500)
c1.withdraw(400)

s1.calculate_interest()



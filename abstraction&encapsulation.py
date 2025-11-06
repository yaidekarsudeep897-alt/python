#Abstraction
class Car:
    def start_engine(self):
        print("Engine is started")
    def accelerate(self):
        print("Car is accelerating")
    def brake(self):
        print("Car is stoping")
car=Car()
car.start_engine()
car.accelerate()
car.brake()

#Encapsulation
class ATM:
    def __init__(self,balance):
        self._balance=balance #private attributes

    def deposite(self,amount):
        self._balance+=amount
        print(f"Deposite:{amount} , New Balance:{self._balance}")

    def withdraw(self,amount):
        if amount<=self._balance:
            print(f"Withdraw:{amount} , New Balance:{self._balance}")
        else:
            print("Insufficient balance")

atm=ATM(10000)
atm.deposite(1000)
atm.withdraw(5000)

#Abstraction and Encapsulation


class Database:
    def __init__(self):
        self.__storage={}

    def write(self,key,value):
        self.__storage[key]=value

    def read(self,key):
        if key in self.__storage:
            print(self.__storage[key])
        else:
            print("DB item is Not available")
db=Database()
db.write("Sudeep_Vaidekar","55 followers")
db.read("Ram")


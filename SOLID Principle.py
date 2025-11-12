# Single Responsibility principle
class Book:
    def __init__(self,title,auther,price):
        self.title=title
        self.auther=auther
        self.price=price

class Bookprinter:
    def print_details(self,book):
        print(f"Title:{book.title}")
        print(f"Auther:{book.auther}")
        print(f"Price:{book.price}")
b1=Book("Python Basics","John doe",499)
printer=Bookprinter()
printer.print_details(b1)


#OPEN/CLOSED PRINCIPLE

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def get_tax(self):
        raise NotImplementedError("subclass must override get_tax")
    
class Food(Product):
    def get_tax(self):
        return self.price*0.05
    
class Electronics(Product):
    def get_tax(self):
        return self.price*0.18
    
class BillingSystem:
    def calculate_final_price(self,product):
        total=product.price+product.get_tax()
        print(f"{product.name} Total Price:{total}")

b=BillingSystem()
b.calculate_final_price(Food("Bread",40))
b.calculate_final_price(Electronics("Headphone",2000))

#LISKOV SUBSTITUTION PRINCIPLE

class Vehicle:
    def movea(self):
        print("Vehicle ids moving....")

class Bike(Vehicle):
    def move(self):
        print("Bike is riding on the road")
class Boat(Vehicle):
    def move(self):
        print("Boat is sailing on water")
def start_journey(Vehicle):
    Vehicle.move()

start_journey(Bike())
start_journey(Boat())

#INTERFACE SEGREGATION PRINCIPLE

class Workable:
    def work(self):
        pass
class Eatable:
    def eat(self):
        pass
class Human(Workable,Eatable):
    def work(self):
        print("Human working")
    def eat(self):
        print("Human is eating")

class Robot(Workable):
    def work(self):
        print("Robot working")
h=Human()
r=Robot()

h.work()
h.eat()

r.work()

#DEPENDENCY INVERSION PRINCIPLE

from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    def turn_off(self):
        pass

class TV(Appliance):
    def turn_on(self):
        print("TV is On")
    def turn_off(self):
        print("TV is OFF")

class AC(Appliance):
    def turn_on(self):
        print("AC is On")
    def turn_off(self):
        print("AC is OFF")

class Remote:
    def __init__(self,appliance:Appliance):
        self.appliance=appliance

    def press_on(self):
        self.appliance.turn_on()

    def press_off(self):
        self.appliance.turn_off()


tv_remote=Remote(TV())
ac_remote=Remote(AC())

tv_remote.press_on()
tv_remote.press_off()

ac_remote.press_on()
ac_remote.press_off()

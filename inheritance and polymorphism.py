#Real world example
class Family:
    def __init__(self,surname):
        self.surname=surname

class Child(Family):
    def __init__(self,surname,name):
        super().__init__(surname)
        self.name=name
child=Child("yaidekar","Sudeep")
print(f"{child.name} {child.surname}")

#Programming example
class user:
    def __init__(self,username,possword):
        self.username=username
        self.possword=possword
    def login(self):
        print(f"{self.username} logged in ")

class HR(user):
    def delete_user(self,user):
        print(f"{self.username} deleted a {user}")

hr=HR("Google HR","vydrshvhlk@6363")
hr.login()
hr.delete_user("user_113")


# polymorphism
#real world example
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
      print("Bark")

class Cat(Animal):
    def make_sound(self):
      print("Meow")

animals=[Dog(),Cat()]
for animal in animals:
   animal.make_sound()
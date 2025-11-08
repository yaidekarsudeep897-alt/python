#example 1
class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Invalid age")

student=Student("Sudeep",19)
print("Name:",student.get_name())
print("Age:",student.get_age())
student.set_age(20)
print("Updated Age:",student.get_age())

#example 2
class Vikas:
    def __init__(self,colour,height):
        self.__colour=colour
        self.__height=height

    def get_colour(self):
        return self.__colour
    def get_height(self):
        return self.__height
    
    def set_height(self,height):
        if height>0:
            self.__height=height
        else:
            print("Invalid heigtht")

vikas=Vikas("Brownie",5.5)
print("NAME: Vikas")
print("COLOUR:",vikas.get_colour())
print("HEIGHT:",vikas.get_height())
vikas.set_height(6)
print("UPDATED HEIGHT:",vikas.get_height())

#Method Overloading

class MathOtr:
    def add(self,a,b,c=0):
        return a+b+c
    
math=MathOtr()
print(math.add(2,7))
print(math.add(8,5,9))
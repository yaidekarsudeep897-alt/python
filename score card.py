class Student:
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
        self.__marks={}
    def get_marks(self):
        return self.__marks

    def add_marks(self,subject,marks):
        self.__marks[subject]=marks

    def calculate_average(self):
        total=0
        for mark in self.__marks.values():
            total+=mark
            average=total/len(self.__marks)
            return average

    def is_passed(self):
        has_passed=all(mark<35 for  mark in self.__marks.values())
        if has_passed:
            print(f"{self.name} has Passed ")
        else:
            print(f"{self.name} has Failed ")

    def calculate_grade(self):
        print("Grade: ",end="")
        percentage=self.calculate_average()*100
        if percentage>=95:
            print("O")
        elif percentage>=85:
            print("A")
        elif percentage>=75:
            print("B")
        else:
            print("C")

class ReportCard:
    @staticmethod
    def generate(student:Student):
        student_marks=student.get_marks()
        print(f"Name:{student.name} \t Roll No. {student.roll_no}")
        print("------Marks------")
        for subject,marks in student_marks.items():
            print(f"{subject} - {marks}")

        print("------------------------")
        print(f"Average:{student.calculate_average()}")
        student.is_passed()
        student.calculate_grade()

a=Student("113","Sudeep")
a.add_marks("Maths",97)
a.add_marks("chem",78)
a.add_marks("pop",90)
a.add_marks("ime",30)

ReportCard.generate(a)



    



        
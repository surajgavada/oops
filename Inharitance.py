"""
Inharitance - it allows one class (child) to reuse property or methods of another class (parent)
"""
#this is parent class
class Student:
    def __init__(self,name,no,parcentage,team):
        self.name = name
        self.r_no = no
        self.parcentage = parcentage
        self.team = team

    def student_details(self): 
        print(f"my name is {self.name} usn {self.r_no} with the {self.parcentage+2}% and i am belongs to {self.team} team")

team1 = "A"
team2 = "B"

std1 = Student("Suraj Gavada","2VD24CI406",78,team1)
std2 = Student("Suraj Desai","2VD24CI407",79,team2)

#child class 
class GratudeStudent(Student):
    def __init__(self,name,no,parcentage,team,stream): # parameters from parent class to child class and new parameters in child class
        super(). __init__(name,no,parcentage,team)# it call parent class init
        self.stream = stream

    def student_details(self):
        super().student_details()# method inharit from parent class
        print(f"Stream is {self.stream}")

grd_std = GratudeStudent("teju","2VD24CI405",80,team1,"BE")
print(grd_std.__dict__)
print(std1.__dict__)
print("\n")
grd_std.student_details()

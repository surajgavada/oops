"""
Polymorphism - that same name method in different class behaves dfferently 
"""

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


class GratudeStudent(Student):
    def __init__(self,name,no,parcentage,team,stream):
        super(). __init__(name,no,parcentage,team)
        self.stream = stream

    def student_details(self):
        print(f"{self.name} and usn is {self.r_no} passed with Stream is {self.stream}") #it gives output according to logic what we have given

#object of Student class
std1 = Student("Suraj Gavada","2VD24CI406",78,team1)
#object of graduate class
grd = GratudeStudent("suraj","2VD24CI406",88,team1,"B.E")

std1.student_details()
grd.student_details()
"""
4 features of oops 
1. abstractaction - hiding unnaccesary details from users throught method or class
2.
"""
class Student:
    def __init__(self,name,no,parcentage,team):
        self.name = name
        self.r_no = no
        self.parcentage = parcentage
        self.team = team

    def student_details(self):#as a example this is also abstraction method 
        print(f"my name is {self.name} usn {self.r_no} with the {self.parcentage+2}% and i am belongs to {self.team} team")

team1 = "A"
team2 = "B"

std1 = Student("Suraj Gavada","2VD24CI406",78,team1)
std2 = Student("Suraj Desai","2VD24CI407",79,team2)
# print (std1.name,std1.r_no,std1.parcentage,std1.team)
# print (std2.name,std2.r_no,std2.parcentage,std2.team)
# print("\n")
# print(std1.__dict__)
# print(std2.__dict__)
# print("\n")
std1.student_details()
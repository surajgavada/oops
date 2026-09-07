"""Encapsulation -Restrict access to certain attributes and methods to protect data
and enforce controlled access.
it makes attributes and methods pravite from user 
"""
class Student:
    def __init__(self,name,no,parcentage,team):
        self.name = name
        self.r_no = no
        self.__parcentage = parcentage #this one is pravite. we user double __ the attribute to make it pravite.
        self.team = team

    def get_percentage(self): #to access the pravite attribute use create separate method 
        return self.__parcentage

    def student_details(self):
        print(f"my name is {self.name} usn {self.r_no} with the {self.parcentage+2}% and i am belongs to {self.team} team")

team1 = "A"
team2 = "B"

std1 = Student("Suraj Gavada","2VD24CI406",78,team1)
std2 = Student("Suraj Desai","2VD24CI407",79,team2)
#if we try to print it, it gives an error
# print(std1.__parcentage)
#this error
""" print(std1.__parcentage)
          ^^^^^^^^^^^^^^^^^
AttributeError: 'Student' object has no attribute '__parcentage'
"""
std1.get_percentage()
#class 
class Student:
    def __init__(self,name,r_no,parcentage,team): #method 
        self.name = name #attribute 
        self.no =r_no
        self.parcentage = parcentage
        self.team = team

    def student_details(self):
        print(f"my name is {self.name} roll no is {self.no} with {self.parcentage}%.")

team1 = "A"
team2 = "B"
# object 
std1 = Student("suraj gavada",67,56,team1)
print(std1.name,std1.no,std1.parcentage)
std2 = Student("teju goankar",66,90,team2)
print(std2.name,std2.no)

print(std1.__dict__)
print(std2.__dict__) #it shows data in the form of dictionary

std1.student_details()
std2.student_details()
#modify object property
print (std1.parcentage)
std1.parcentage = 78
print(std1.parcentage)
print(std1.name,std1.no,std1.parcentage)
# delete values
del std1.parcentage
print(std1.__dict__)
print (std1.team)

#for delete object 
del std1
print(std1)
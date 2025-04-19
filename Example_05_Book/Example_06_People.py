# Create Class People--------------------------------------
from datetime import date

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # One Method Class for Create
    # One Object People from Date of Birth
    @classmethod
    def date_birth(cls, name, year):
        return cls(name, date.today().year - year)

    # Method Static for Verify if is Legal of Age
    @staticmethod
    def isLegal(age):
        return age >= 18

# Test 01
people1 = People('Ventury', 62)
print(people1.name)
print(people1.age)
print(People.isLegal(people1.age))
print()

# Test 02
people2 = People.date_birth('LUG',2013)
print(people2.name)
print (people2.age)
print(People.isLegal(people2.age))
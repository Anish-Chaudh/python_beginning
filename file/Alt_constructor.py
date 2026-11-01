class Employee:
    def __init__(self,name, Salary):
        self.name = name
        self.Salary = Salary

    @classmethod
    def fromStr(cls, String):
        return cls(string.split("-")[0], string.split("-")[1])

e1 = Employee("Anish Chaudhariy", 10000)
print(e1.name)
print(e1.Salary)

string = "Anish-10000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.Salary)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
person = Person.from_string("John,30") 
print(person.name, person.age)       
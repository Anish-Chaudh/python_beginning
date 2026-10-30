#private(name mangling)
class Employee:
    def __init__(self):
        self.__name = "Anish"

a = Employee()
print(a._Employee__name)
print("\n")
#protected"
class Student:
    def __init__(self):
        self._name = "Rohan thakur"

    def _funName(self):
        return"tuppi"

class Subject(Student):
    pass
obj =Student()
obj1=Subject()

print(obj._name)
print(obj._funName())

print(obj1._name)
print(obj1._funName())
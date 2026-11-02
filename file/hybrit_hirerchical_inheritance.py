class BaseClass:
    def display(self):
        print("This is the base class.")    

class DerivedClass1(BaseClass):
    def display(self):
        print("This is the first derived class.")

class DerivedClass2(BaseClass):
    def display(self):
        print("This is the second derived class.")      

class DerivedClass3(DerivedClass1, DerivedClass2):
    def display(self):
        print("This is the third derived class.")

a = DerivedClass3()
a.display()
print("\n")
class BaseClass:
    def display(self):
        print("This is the base class.")

class DerivedClass1(BaseClass):
    def display(self):
        print("This is the first derived class.")

class DerivedClass2(BaseClass):
    def display(self):
        print("This is the second derived class.")
b = DerivedClass2()
b.display()
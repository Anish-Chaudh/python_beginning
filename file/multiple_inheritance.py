class Employee:
    def __init__(self, name,):
        self.name = name

    def show(self):
        print(f"Employee name: {self.name}")

class dancer():
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"Dance style: {self.dance}")

class EmployeeDancer(Employee, dancer):
    def __init__(self, name, dance):
        Employee.__init__(self, name,)
        dancer.__init__(self, dance)

    def show(self):
        print(f"Employee name: {self.name}, Dance style: {self.dance}")

o = Employee("Gurash")
o.show()
d = dancer("Belli")
d.show()
# d.show()
c = EmployeeDancer("Gurash", "Belli")
c.show()
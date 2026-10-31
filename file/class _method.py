class Employee:
    company_name = "Google"
    def showDetails(self):
        print(f"Name of employeee is {self.name} and he/she work at {self.company_name} ")
    @classmethod
    def changeName(cls,NewchangeName):
        cls.company_name = NewchangeName

e = Employee()
e.name ="Anish Chaudhary"
e.showDetails()
e.changeName("NIC")
e.showDetails()
print(Employee.company_name)
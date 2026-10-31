class Employee:
    companyName = "National Innovation Centre" 
    no_of_employee = 0
    def __init__(self,name,):
        self.name = name
        self.raise_amount = 0.1
        Employee.no_of_employee +=1
    def showDetails(self):
        print(f"The name of employee is {self.name},it's number is{self.no_of_employee} and work at {self.companyName} and his raise amount is {self.raise_amount}")

emp1 = Employee("Anish")
emp1.companyName = "Google"
emp1.raise_amount = 0.2
emp1.showDetails()
emp2 =Employee("Rahul")
emp2.showDetails()

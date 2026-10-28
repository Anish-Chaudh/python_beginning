class Person:
    name = "Anish Bakhariya"
    age = 20
    occupation = "Student"
    def info(self):
        print(f"My name is {self.name}. I am {self.age} years old and I am a {self.occupation}.")
a = Person()
b = Person()
b.name = "Devi john"
b.age = 20
b.occupation = "pirate king"
a.info() 
b.info()   
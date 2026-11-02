class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Animal name: {self.name}")
        print(f"species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species="Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Dog breed: {self.breed}")

    def show_details(self):
        Animal.show_details(self)
        print(f"breed: {self.breed}")

class pitbull(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed = "pitbull")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

p = pitbull("Rocky", "Brown")
p.show_details()
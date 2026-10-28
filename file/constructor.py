class Dog:
    def __init__(self, name, species):
        print("I am dog lover")
        self.name = name
        self.species = species

    def info(self):
        print(f"The dog name is {self.name} and the species is {self.species}.")
a = Dog("kris", "Golden Retriever")
b = Dog("Max", "German Shepherd")
a.info()
b.info()

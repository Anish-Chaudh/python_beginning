class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Animal make sound")

class cat(Animal):
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("meow!,meow!......")

c = cat("shuri", "Local")
c.make_sound()
a = Animal("Dog", "German Shepherd")
a.make_sound()



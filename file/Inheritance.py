class Animal:
    def __init__(self, Types, Name, food):
        self.Types = Types
        self.Name = Name
        self.food = food

    def details(self):
        print(f"{self.Name} is a {self.Types} and it eats {self.food}")

class Dog(Animal):
    def sound(self):
        print("it can barks")

a1 = Animal("Cow", "Nandi", "grass")
a1.details()

b1 = Animal("Lion","Simba","flesh")
b1.details()

c1 = Dog("pit Bull","tommy","bone")
c1.details()
c1.sound()


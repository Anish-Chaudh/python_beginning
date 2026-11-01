x = [1,2,3,4,5]
print(dir(x))
print(x.__add__)
print("\n")

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.verson = 1.0
p =person("Anish", 23)
print(p.__dict__)
print("\n")
print(help(person))
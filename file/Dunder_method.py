class employee:
    name = "Anish"
    def __len__(self):
        i = 0
        for c in self.name:
            i += 1
        return i
    
a = employee()
print(a.name)
print(len(a))

class student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"the name of student is {self.name}"

    def __repr__(self):
        return f"student({self.name})"

e = student("Anish")
print(str(e))
print(repr(e))

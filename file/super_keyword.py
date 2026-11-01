class ParentClass:
    def parent_method(self):
        print("This is a method in the ParentClass.")

class childClass(ParentClass):
    def parent_method(self):
        print("my name is anish")
        super().parent_method()
    def child_method(self):
        print("This is a method in the childClass.")
        super().parent_method()
a = childClass()
a.child_method()
a.parent_method()

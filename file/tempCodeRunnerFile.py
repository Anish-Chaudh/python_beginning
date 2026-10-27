print("for list")
a = [1,3,5,8]
b = [1,3,5,8]
print(a is b)
print(a == b)
print("\n")
print("for tuples")
c = (1,3,4,5)
d = (1,3,4,5)
print(c is d)
print(c == d)

print("\n for string/constant value")
e = "Anish" 
f = "Anish"
print(e is f) #check exact location of object in memory

print(e == f)#value
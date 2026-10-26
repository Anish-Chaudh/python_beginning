def apply(func, value):
    return func(value)*2
double = lambda x: x*2
square = lambda x: x*x
avg = lambda x,y,z: (x+y+z)/3
cube = lambda x: x**3
print(double(5))
print(square(5))
print(avg(5,20,18))
print(cube(8))
print(apply(cube, 8))
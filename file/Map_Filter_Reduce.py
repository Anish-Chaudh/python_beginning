def cube(x):
    return x*x*x
print(cube(3))
l=[1,3,4,5,6,8,9]
newl=list(map(cube,l))
print(newl)

# filter
def filter_function(a):
    return a>4
newnewl = list(filter(filter_function, l))
print(newnewl)

# Reduce
from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9,10]
result = reduce(lambda x,y:x+y, numbers)
print(result)
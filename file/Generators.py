def my_generator():
    for i in range(10000):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print("\n")
import time
time.sleep(5)
for j in gen:
    print(j)
from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*8

print(fx(3))
print("done for 3")
print(fx(5))
print("done for 5")
print(fx(8))
print("done for 8")
print("\n")
print(fx(3))
print("done for 3")
print(fx(5))
print("done for 5")
print(fx(8))
print("done for 8")
print(fx(2))
print("done for 2")


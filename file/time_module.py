import time
def usingwhile():
    i = 0
    while i < 50000:
        print(i)
        i += 1

def usingfor():
    for i in range(50000):
        print(i)
init = time.time()
usingwhile()
t1 = time.time() - init
init = time.time()
usingfor()
t2 = time.time() - init
print(t1)
print(t2)
print("\n")

print("Anish is learning python and he is a good learner")
time.sleep(5)
print("5 seconds have been interrupted")
print("\n")

formated_time = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
print(formated_time)
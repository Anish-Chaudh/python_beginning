import threading
import time
# Indicate some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
#normal code
func(3)
func(4)
func(1)
print("\n")
#code using threading
t1 = threading.Thread(target = func, args=[5])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[6])
t1.start()
t2.start()
t3.start()
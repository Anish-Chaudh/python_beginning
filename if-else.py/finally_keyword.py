try:
    x=int(input("enter the number: "))
    print("the squrare of number is :", x*x)
except ValueError:
    print("enter only integer value")
finally:
    print("this block will always execute")
    
num=input("enter the number: ")
print(f"the multiplication table of {num} is:")
try:
    for i in range(1, 11):
        print(f"{num} x {i} = {int(num) * i}")
except ValueError:
    print("Please enter a valid number.")

try:
    a=int(input("enter the number:"))
    b=[2,3,5,8]
    print(b[a])
except ValueError:
    print("enter only integer value")
except IndexError:
    print("index out of range")


try:
    a=int(input("enter the number:"))
    print(a)
except:
    print("enter only integer value")
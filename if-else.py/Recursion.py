# write a program to find the factorial of a number using recursion.
# def factorial(num):
#     if(num==0 or num==1):
#         return 1
#     else:
#         return num*factorial(num-1)
# num=int(input("enter the number: "))
# print(factorial(num))

# write a program to find the fibonacci series up to n terms using recursion.
def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return (fibonacci(num-1)+fibonacci(num-2))
num=int(input("enter the number of terms: "))
print("fibonacci series: ")
for i in range(num):
    print(fibonacci(i), end=" ")
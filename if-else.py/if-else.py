print("welcome to myadi police form")
print("you have to pass below crietia")
age=int(input("please enter your age:"))
if (age<18):
    print("you are not capable for this post.")
elif (age==18):
    print("please enter your birth month")
    month=int(input())
    if (month<3):
        print("please wait for 9 month.")
    elif (month<6):
        print("please wait for 6 months")
    elif (month<9):
        print("please wait for 3 month")
    elif (month<12):
        print("please wait for some month or some day")
    else:
        print("your age is 19 you are capable.")
elif (age>60):
    print("you are old. you are not capable for this post")
else :
    print("you are capable for myadi police ")

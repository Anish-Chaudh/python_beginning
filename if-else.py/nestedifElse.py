num=(int(input("enter the number:")))
if(num > 0):
    print(+num," is positive number ")
    if( num>0 and num<=10):
        print(+num,"lies between 0 to 10")
    elif( num>10 and num<=20):
        print(+num,"lies between 10 to 20" )
    else:
        print(+num," is greater than 20")
elif(num==0):
    print("the number is zero")
else:
    print(+num,"is negative number")
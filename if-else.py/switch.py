A=int(input("enter the value of A:"))
match A:
    case 0:
        print("the value of a is zero")
    case 3:
        print("the value of a is three")
    case _ if A!=8:
        print(A,"the value of a si not 8")


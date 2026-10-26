num=int(input("enter the number:"))
match num:
    case 0:
        print(+num, "is zero")
    case 4:
        print(num,"is four")
    case _ if num!=80:
        print(num, "is not 80 ")
    case _ if num!=90:
        print(num,"is not 90")
    case _:
        print(num)


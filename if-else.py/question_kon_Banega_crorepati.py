import time
print("welcome to kon Banega crorepati....")
current_time=time.strftime("%H:%M:%S")
print("current time is",current_time," Now we will start the game.....\n")
print("you have only 4 option to choose...\n")
print("The question in question no.1 is:\n")
que_1="how many continents are there?"
option='''            1.four
            2.nine
            3.seven
            4.eight'''
print(que_1)
print(option)
option=int(input("choose the correct option:\n"))
i=0
if option==3:
    print("congratulations! you are right")
    i=i+1
    print("your current score is",i,"\n")
else:
    print("sorry! you are wrong")
    print("your current score is",i,"\n")

print("The question in question no.2 is:\n")
que_2="who is the current pm of india?"
option='''            1.bijay thalapathi
            2.narendra modi
            3.khan sir
            4.ram gandi'''
print(que_2)
print(option)
option=int(input("choose the correct option:"))
if option==2:
    print("congratulations! you are right")
    i=i+1
    print("your current score is",i,"\n")
else:
    print("sorry! you are wrong")
    print("your current score is",i,"\n")

print("The question in question no.3 is:")
que_3="how is the know as the king of bollywood?"
option='''            1.salman khan
            2.Ranbir kapoor
            3.amita bachhan
            4.Sharukh khan'''
print(que_3)
print(option)
option=int(input("choose the correct option:\n"))

if option==4:
    print("congratulations! you are right")
    i=i+1
    print("your current score is",i,"\n")
else:
    print("sorry! you are wrong")
    print("your current score is",i,"\n")

print("The question in question no.4 is:\n")
que_4="who is the founder of KBC?"
option='''            1.rohit chadda
            2.Govinda madan
            3.Amitabh bachhan
            4.saru khan'''
print(que_4)
print(option)
option=int(input("choose the correct option:"))
if option==3:
    print("congratulations! you are right")
    i=i+1
    print("your current score is",i,"\n")
else:
    print("sorry! you are wrong")
    print("your current score is",i,"\n")

print("The question in question no.5 is:\n")
que_5="how is the main chairman of kapir sharma show?"
option='''            1.Archana puran singh
            2.kapil Sharma
            3.sunil grover
            4.sidhu paji'''
print(que_5)
print(option)
option=int(input("choose the correct option:"))
if option==4:
    print("congratulations! you are right")
    i=i+1
    print("your current score is",i,"\n")
else:
    print("sorry! you are wrong")
    print("your current score is",i,"\n")

print("The question in question no.6 is:\n")
que_6="who is the founder of facebook"
option='''            1.mark zuckerberg
            2.elon musk
            3.steve jobs
            4.bill gates'''
print(que_6)
print(option)
option_1=int(input("choose the correct option:"))
if option_1==1:
    print("congratulations! you are right")
    i=i+1
    print("your current score is",i,"\n")
else:
    print("sorry! you are wrong")
    print("your current score is",i,"\n")

print("The question in question no.7 is:\n")
que_7="current pm of nepal Balen shah have done master in which field ?"
option='''            1.civil engineering
            2.computer engineering
            3.structural engineering
            4.mechanical engineering'''
print(que_7)
print(option)
option=int(input("choose the correct option:"))
if option==3:
    print("congratulations! you are right")
    i=i+1
    print("your current score is",i,"\n")
else:
    print("sorry! you are wrong")
    print("your current score is",i,"\n")

print("The question in question no.8 is:\n")
que_8="who is the director of famous movie bahubali?"
option='''            1.Amir khan 
            2.s.s. rajamouli
            3.sharukh khan
            4.aakshay kumar'''
print(que_8)
print(option)
option=int(input("choose the correct option:"))
if option==2:
    print("congratulations! you are right")
    i=i+1
    print("your current score is",i,"\n")
else:
    print("sorry! you are wrong")
    print("your current score is",i,"\n")

print("The question in question no.9 is:\n")
que_9="who is know as the king of mimikry world in kapil sharma show?"
option='''            1.Bharati singh
            2.johny lever
            3.sunil grover
            4.kapil sharma'''
print(que_9)
print(option)
option=int(input("choose the correct option:"))
if option==3:
    print("congratulations! you are right")
    i=i+1
    print("your current score is",i,"\n")
else:
    print("sorry! you are wrong")
    print("your current score is",i,"\n")

print("The question in question no.10 is:\n")
que_10="Aadhimanav movie is base on story of ?"
option='''            1.mahabharat
            2.buddhist
            3.cristin
            4.ramayan'''
print(que_10)
print(option)
option=int(input("choose the correct option:"))
if option==4:
    print("congratulations! you are right")
    i=i+1
    print("your current score is",i,"\n")
else:
    print("sorry! you are wrong")
    print("your current score is",i,"\n")

print("The question in question no.11 is:\n")
que_11="who is the main actor of movie dhurandhar?"
option='''            1.parvash
            2.shahid kapoor
            3.Ranveer Singh
            4.salman khan'''
print(que_11)
print(option)
option=int(input("choose the correct option:"))
if option==3:
    print("congratulations! you are right")
    i=i+1
    print("your current score is",i,"\n")
else:
    print("sorry! you are wrong")
    print("your current score is",i,"\n") 

print("The question in question no.12 is:\n")
que_12="who make india free from british rule?"
option='''            1.narendra modi
            2.shyama bahadur thapa
            3.hitlar
            4.mahatma gandhi'''
print(que_12)
print(option)
option=int(input("choose the correct option:"))
if option==4:
    print("congratulations! you are right")
    i=i+1
    print("your current score is",i,"\n")
else:
    print("sorry! you are wrong")
    print("your current score is",i,"\n")

if (i==12):
    print("congratulations!, you have given all the correct answer ")
elif(i==11):
    print("congratulations!, you have given 11 correct answer out of 12")
elif(i==10):
    print("congratulations!, you have given 10 correct answer out of 12")
else:
    print("you have given only",i,"correct answer out of 12,please try next time")
f=open('myfile1.txt','r')
while True:
    line=f.readline()
    print(line)
    if not line:
        break

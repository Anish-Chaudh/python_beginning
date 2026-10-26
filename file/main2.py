f=open('myfile2.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"marks of student {i} in math is: {m1}")
    print(f"marks of student {i} in physics is: {m2}")
    print(f"marks of student {i} in chemistry is: {m3}")
    print(line)


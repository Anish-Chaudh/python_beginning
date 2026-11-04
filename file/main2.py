f=open('myfile.txt','r')
print(f)
text=f.read()
print(text)
f.close()

f=open('myfile.txt','w')
f.write('I am munna bhai\n')
f.close()

with open('myfile.txt','a') as f:
    f.write('hey i am inside with block')
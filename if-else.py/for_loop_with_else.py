for i in range(5):
    print(i)
else:
    print("Loop is over")

#else will only execute if the loop is not terminated by a break statement. If there is a break statement in the loop, the else block will not execute.
#example:
for i in range(8):
    print(i)
    if i == 4:
        break 
else:
    print("loop is over")
print("\n")

i=0
while i<5:
    print(i)
    i=i+1
else:
    print('Loop is over')
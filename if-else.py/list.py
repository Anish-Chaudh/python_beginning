list=[1,2,3,5,8,93,9,"Anish","True",3]
print(len(list))
print(list)
print(type(list))
print(list[0])
print(list[7])
print(list[-3])
print(len(list)-3)
print(list[3:9])
print(list[1:10:3])
if "Anish" in list:
    print("Anish is present in the list")
else:
    print("Anish is not present in the list")

lst=[i for i in range(10)]
print(lst)
lst=[i*i for i in range(10) if i%2==0]
print(lst)
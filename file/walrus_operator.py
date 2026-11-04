a = True
print(a:=False)
print("\n")

numbers = [1,2,3,4,5,7]
while(n := len(numbers))>0:
    print(numbers.pop())
print("\n")

#without walrus operator
foods = list()
while True:
    food = input("what food do you like? ")
    if food == "quit":
        break
    foods.append(food)
print("\n")

#with walrus operator
foods = list()
while (food := input("what food do you like?"))!="quit":
    foods.append(food)
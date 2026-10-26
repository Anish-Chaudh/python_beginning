dic={
    "name":"Anish chaudhary",
    "age": 20,
    "city":"Pokhara"
    
}
print(dic)
print(dic["city"])
print(dic.keys())
print(dic.items())
for key in dic:
    print(f"the value corresponding to the key {key} is {dic[key]}")
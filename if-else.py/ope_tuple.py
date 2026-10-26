countries=("germany","japan","korea","italy","Nepal","china","america")
print(countries)
temp=list(countries)
print(temp)
temp[4]="astralia"
temp.append("coratia")
temp.pop(3)
countries=tuple(temp)
print(countries)

countries2=("spain","dubai","kuwait","poland")
countries3=countries+countries2
print(countries3)
cities={"new york","kathmandu","pokhara","paris","london","tokyo"}
cities2={"delhi","sukovia","wakanda","kathmandu","pokhara","bejing"}
print(cities.union(cities2))
print(cities.update(cities2))
print(cities)
print(cities.intersection(cities2))
print(cities.intersection_update(cities2))
print(cities)
print(cities.symmetric_difference(cities2))
print(cities.difference(cities2))

print(cities.isdisjoint(cities2))
cities3={"dhaka","dubai","sydney"}
print(cities.issuperset(cities3))
print(cities.issubset(cities2))
cities3.add("nepalgunj")
print(cities3)
cities3.remove("dhaka")
print(cities3)
print(cities3.discard("tokyo"))
item=cities3.pop()
print(item)
# del cities3
# print(cities3)
cities.clear()
print(cities)

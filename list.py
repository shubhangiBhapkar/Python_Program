#List
cities=["pune","mumbai","Nagpur","delhi","Hydrabad"]
print(cities)
print(type(cities))
print(len(cities))
print(cities[0])
#print(dir(cities))
cities.append("Sangamner")

city_abbr=["pun","mum","nag"]
cities.extend(city_abbr)
print(cities)
print(city_abbr)
print(cities.index("Nagpur"))

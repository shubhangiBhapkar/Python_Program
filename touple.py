#touple
city_tup=("nagpur","Delhi","pune","mumbai")
print(city_tup)
print(type(city_tup))
print(city_tup.count("Delhi"))
#city_tup[2]="Sangamner"
city=list(city_tup)
city[2]="sangamner"
new_tup=tuple(city)
print(new_tup)




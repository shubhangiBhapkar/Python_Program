my_dict={"city":"Sangamner",
"temperature":25,
"carbon_foootprint":500.75,
"is_sustainable":False}

print(my_dict)
print(type(my_dict))
print(my_dict["temperature"])
print(my_dict["is_sustainable"])

#Changing value of key

my_dict["temperature"]=28
#print(my_dict)
print(my_dict.get("city"))
print(my_dict.keys())
print(my_dict.items())

#Empty Dictionary
empty_dict={}
print(type(empty_dict))

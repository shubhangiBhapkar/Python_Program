climate_data=[
    {"city":"city A", "temperature" :25 ,"carbon_footprint":500},
    {"city":"city B", "temperature" : 30,"carbon_footprint":350 },
    {"city":"city C", "temperature" :22,"carbon_footprint": 600},
    {"city":"city D", "temperature" :15 ,"carbon_footprint": 200},
    {"city":"city E", "temperature" :28,"carbon_footprint": 450}
]

temp_threashold=26
high_temp_cities = {city for city in climate_data if city ['temperature'] >temp_threashold}
print(high_temp_cities)
for city in high_temp_cities:
    print(f"{city:['city']}:{city:['temperature']}")
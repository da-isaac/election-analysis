counties = ["Arapahoe", "Denver", "Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso is not in the list of counties")

# county is a variable that is declared and assigned a variable in this line
for county in counties:
    print(county)

# python function that allows you to iterate through a for loop x amount of times
for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# getting keys of a dictionary
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

#getting values of a dictionary
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

#getting key-value pairs of a dictionary
for county, voters in counties_dict.items():
    print(county, voters)
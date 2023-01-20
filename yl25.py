"""me = {
    "first_name": "Oskar",
    "last_name": "Kallas",
    "birth_year": 2006,
    "place_of_living": "Leisi",
    "dessert": "Kommid",
}

print(me.get("place_of_living"))
print(me["place_of_living"])

me["dessert"] = "Jäätis"

for k, v in me.items():
    print(k, v)
"""



person = {
    "first_name": "Oskar",
    "last_name": "Kallas",
    "birth_year": 2006,
    "location": "Leisi",
    "favorite_dessert": "Jäätis"
}

print(person.get("location"))
print(person["location"])

person["favorite_dessert"] = "Kook"

for key in person:
    print(key)

for value in person.values():
    print(value)

if "isikukood" in person:
    print("Isikukood on olemas")
else:
    print("Isikukoodi ei ole")

print(len(person))

person["height"] = "189cm"
del person["birth_year"]

person.clear()


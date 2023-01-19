me = {
    "first_name": "Oskar",
    "last_name": "Kallas",
    "birth_year": 2006,
    "place_of_living": "Leisi",
    "dessert": "Kommid",
}

#print(me.get("place_of_living"))
#print(me["place_of_living"])

me["dessert"] = "Jäätis"

for k, v in me.items():
    print(k, v)
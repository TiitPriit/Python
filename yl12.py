fruits = ["Õun", "Mango", "Pirn"]

print(fruits)

print("Esimene puuvili:", fruits[0])

fruits.append("Ploom")
print("Viimane puuvili:", fruits[len(fruits)-1])

fruits[1] = "Viinamarjad"
print(fruits)

if "Õun" in fruits:
    print("Õun on olemas.")
else:
    print("Õuna pole olemas.")

print("Listis on:", len(fruits),)

fruits.remove("Pirn")
print(fruits)

fruits.reverse()
fruits.sort()
print(fruits)
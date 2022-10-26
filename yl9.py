print("Sisesta kolmnurga külgede pikkused: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Võrdkülgne kolmnurk")
elif (x + y < z) or (x + z < y) or (z + y < x):
    print("pole võimalik")
elif x==y or y==z or z==x:
	print("Võrdhaarne kolmnurk")
else: 
	print("Erikülgne kolmnurk")
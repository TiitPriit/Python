print("Sisesta kolmnurga külgede pikkused: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Võrdkülgne kolmnurk")
elif (x <= 0) or (y <= 0) or (z <= 0):
    print("pole võimalik")
elif x==y or y==z or z==x:
	print("Võrdhaarne kolmnurk")
else: 
	print("Erikülgne kolmnurk")

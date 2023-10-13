
A = float(input("Sisesta A väärtus: "))
B = float(input("Sisesta B väärtus: "))
C = float(input("Sisesta C väärtus: "))
D = float(input("Sisesta D väärtus: "))

A, B, C, D = map(float, input().split())

keep_warm_energy = C * 60  

cooling_energy = 0
time_to_cool = 0

while time_to_cool < 60:
    cooling_energy += D * (60 - time_to_cool)  
    time_to_cool += B  
    if time_to_cool < 60:
        cooling_energy += (60 - time_to_cool) * A  
        time_to_cool += 60  

print(round(keep_warm_energy, 2))
print(round(cooling_energy, 2))

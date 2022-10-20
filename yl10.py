name = input("Mis su nimi on?: ")

print("Tervist",name,)

elukoht = input("Kus sa elad?: ")

if elukoht == "Saaremaal":
    print("Saaremaa parim saar!")

age = int(input("Kui vana sa oled?: "))

if age < 18:
    print("Liiga tatt, et autot juhtida.")
elif age == 18:
    print("Õnnitlused täisealiseks saamisel!")
elif age > 18:
    print("Võid autot juhtida.")
pituus = int(input("Anna pituutesi: "))
paino = float(input("Anna painosi:"))

#Muuttuja jossa lasku suoritetaan

bmi= paino/(pituus/100)**2

print("Pituus-paino-indeksi", bmi)
print(f"Pituus-paino-indeksi{bmi: .2f}")
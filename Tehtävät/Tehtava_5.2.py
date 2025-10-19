#luodaan lukujono lista
lukujono=[]
#pyydetään luku
luku= input("Anna luku:")
#toistetaan kyselyä kunnes syöte on "tyhjä"
while luku !="":
    #Laitetaan syötä listalle
    lukujono.append(luku)
    luku= input("Anna luku:")

print(f"Annoit lukujonon {lukujono}")
#lukujonon laitto suuruuns järjestykseen
lukujono.sort(reverse=True)
#lukujonon tulostus
print(f"lukujono suuruus järjestyksessä{lukujono}")
#Tulostetaan listan 5 ensimmäistä lukua
print(lukujono[0:5])
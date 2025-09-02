#Lukune syöttö
a= float(input("Anna leiviskät:"))
b= float(input("Anna naulat:"))
c= float(input("Anna luodit:"))
#Laskenta ja tulostus
#laskenta
paino=float((a*20*32*13.3)+(b*32*13.3)+(c*13.3))
#kilogramma ja gramma laskenta
kg=int(paino/1000)
grammat=float(paino-(kg*1000))
#Tulostus ja desimaali rajaus
print(f"{kg}kilogrammaa ja {grammat:.2f}grammaa")
#print(f"Massa nykymittojen mukaan:", str(((a*20*32*13.3)+(b*32*13.3)+(c*13.3))),"grammaa")
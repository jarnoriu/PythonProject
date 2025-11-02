
#Luodaan funktio, joka heittää noppaa annettuu silmälukuun
def muunnos(i):
    litrat = i * 3.785
    return litrat

#Pääohjelma
#Kysytään litramäärä
while True:
    gallonat= float(input("Anna bensiinin määrä gallonoina"))
    if gallonat <0:
        print("Ohjelma lopetetaan")
        break
    else:
        tulos=muunnos(gallonat)
        print(tulos)

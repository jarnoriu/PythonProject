
#Luodaan funktio, joka heittää noppaa annettuu silmälukuun
def muunnos(funktionapumuuttuja):
    valivarasto = funktionapumuuttuja * 3.785
    return valivarasto

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

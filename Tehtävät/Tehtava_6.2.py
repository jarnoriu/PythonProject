import random

#Luodaan funktio, joka heittää noppaa annettuu silmälukuun
def nopanheitto(i):
    silmaluku=random.randint(1,i)
    return silmaluku

#Pääohjelma
#Kysytään sivujen määrä
tahkot= int(input("Anna tahkojen määrä"))
tulos=0
while tulos != tahkot:
        tulos=nopanheitto(tahkot)
        print(tulos)
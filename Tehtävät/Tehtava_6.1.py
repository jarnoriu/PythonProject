import random

#Luodaan funktio, joka heittää noppaa
def nopanheitto():
    silmaluku=random.randint(1,6)
    return silmaluku

#Pääohjelma
tulos=nopanheitto()
print(tulos)
while tulos != 6:
        tulos=nopanheitto()
        print(tulos)
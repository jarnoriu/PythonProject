
#import random
from random import randint
#luodaan muuttuja montako noppaa
nopat= int(input("Anna noppien määrä"))


summa=0
#arvotaan noppan näyttämä
for noppa in range(nopat):
    numero=randint(1,6)
    print(numero)
    #lasketaan numerot yhteen
    summa += numero
#tulostetaan silmäluvut
print(f"noppien summa on {summa}")
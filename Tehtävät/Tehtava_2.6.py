import random
#random tuonti

#laskenta 3 digit
tulos1 = ""
for i in range (3):
 a=random.randint(0,9)
 tulos1 = tulos1 + str(a)

print(tulos1)

#laskenta ja numero rajaus, 4 digit
tulos1 = ""
for i in range (4):
 a=random.randint(1,6)
 tulos1 = tulos1 + str(a)

print(tulos1)

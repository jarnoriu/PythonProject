#Lukune syöttö
a= float(input("Anna tuumat:"))

#laskentaan muunnosta kunnes a pienempi kuin 0
while a > 0:
    pituus=float(a*2.54)
    print(pituus)
    a= float(input("Anna tuumat:"))

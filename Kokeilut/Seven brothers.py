
def seven_brothers(lista):
    lista.sort()
    print (lista)

    for nimi in lista:
        print(nimi)
    return

# Pääohjelma
veljekset = ["Eero", "Juhani", "Simeoni", "Tuomas", "Timo", "Aapo", "Lauri"]
seven_brothers(veljekset)
aakkosjarjestyksessa = sorted(veljekset)

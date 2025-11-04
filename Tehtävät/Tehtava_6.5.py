
def karsi_parittomat(luvut):
    parilliset=[]
    for item in luvut:
        if item % 2 == 0:
            parilliset.append(item)
    return parilliset





#Pääohjema
lista=[]
while True:
    #Kysy luku
    syote = input("Anna luku tai lopeta painamalla enter")
    # Jos painetaan enter lopeta
    if syote =="":
        print("Kiitos")
        break
    #Jos luku on numero lisää se listaan
    else:
        luvuksi=int(syote)
        lista.append(luvuksi)

muistipaikka=karsi_parittomat(lista)
print(lista)
print(muistipaikka)


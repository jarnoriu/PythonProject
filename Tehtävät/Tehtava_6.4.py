
def summa(luvut):
    laskenta = 0
    for item in luvut:
        laskenta = item + laskenta
    return laskenta





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

muistipaikka=summa(lista)
print(muistipaikka)




#kutsu funktiota, joka laskee summan

# Tulosta summa
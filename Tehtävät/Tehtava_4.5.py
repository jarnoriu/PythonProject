from operator import truediv

laskuri = int (1)
kauttajatunnus = "python"
salasana = "rules"

syota_tunnus = input("Anna tunnus:")
syota_salasana = input("Anna salasana:")

while laskuri <= 4:
    if syota_tunnus == kauttajatunnus:
        if syota_salasana == salasana:
            print("Tervetuloa")
            break
        else:
            print ("Salasana on väärin")
            laskuri+=1
    elif kauttajatunnus != syota_tunnus:
        print ("Käyttäjätunnus on väärin")
        laskuri+=1
    syota_tunnus = input("Anna tunnus:")
    syota_salasana = input("Anna salasana:")
if laskuri > 4:
 print ("Pääsy evätty")

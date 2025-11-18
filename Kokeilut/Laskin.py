

#Yhteenlasku
def summa(num1, num2):
    print("Yhteenlaskun tulos on:"num1 + num2)
    return

#Vähennyslasku
def vahennus(num1, num2):
    print ("Vähennys laskun tulos on:"num1 - num2)

#Kertolasku
def kerto(num1,num2):
    print("Kertolaskun tulos on:"num1 * num2)

#Jakolasku
def jako(num1,num2):
    if b!=0:
        print("Jakook tulos on:", num1 / num2)
    else:
        print("Nollalla ei voi jakaa!")
    return

#Pääohjelma
    print("-----Tervetuloa käyttämään laskinta!-----")

while True:
    print("Valitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku \n C: Kertolasku \n D: Jakolasku")

    valinta= input("valintasi (A-D), Q lopettaa ").upper()

    #while loopin katkaisu
    if valinta == "Q":
        print("Ohjelma lopetetaan, Kiitos Hei!")
        break

    a= float(input("Anna ensimmäinen luku:"))
    b= float(input("Anna toinen luku:"))

    if valinta == "A":
        summa(a,b)
    elif valinta == "B":
        vahennus(a,b)
    elif valinta == "C":
        kerto(a,b)
    elif valinta == "D":
        jako(a,b)
    else:
        print("Valintasi on virheellinen")
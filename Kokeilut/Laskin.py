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
        print("Yhteenlasku", a+b)
    elif valinta == "B":
        print("Vähennyslasku", a-b)
    elif valinta == "C":
        print("Kertolasku", a * b)
    elif valinta == "D":
        print("Jakolasku", a / b)
    else:
        print("Valintasi on virheellinen")
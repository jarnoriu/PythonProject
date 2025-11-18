from http.server import HTTPServer

lentoasemat= {"EFHK" : "Helsinki"}

while True:
    Valinta= input("Haluatko syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa? Lisää, Hae, Lopeta")
    Valinta= Valinta.upper()
    if Valinta == "LOPETA":
        print("Lopetetaan")
        break
    elif Valinta == "HAE":
        haku= input("Anna aseman ICAO-koodi")
        if haku in lentoasemat:
            print(f"Aseman {haku} on {lentoasemat[haku]}")
        continue
    elif Valinta == "LISÄÄ":
        ICAO= input("Anna aseman ICAO-koodi")
        nimi= input("Anna aseman nimi")
        lentoasemat[ICAO]= nimi
        print("Lisätään")
        continue
    else:
        print("Anna oikea komento, Lisää, Hae, Lopeta")
        continue
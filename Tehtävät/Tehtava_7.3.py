while True:
    Valinta= input("Haluatko syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa? Lisää, Hae, Lopeta")
    Valinta= Valinta.upper()
    if Valinta == "LOPETA":
        print("Lopetetaan")
        break
    elif Valinta == "HAE":
        print("Haetaan")
        continue
    elif Valinta == "LISÄÄ":
        print("Lisätään")
        continue
    else:
        print("Anna oikea komento, Lisää, Hae, Lopeta")
        continue
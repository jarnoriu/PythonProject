#Kirjoita funktio, jossa käyttäjältä kysytään kurssi, jonka osallistujamäärän hän haluaa tarkistaa.
#Funktio laskee ja tulostaa kyseiselle kurssille ilmoittautuneiden oppilaiden määrän sanakirjan perusteella.

kurssit= {"Matikka":["Pentti", "Risto", "Olli", "Kalle"],
          "Phyton" : ["Koodi","Code",]}


kys_kurssi = input("Kurssi jonka osallistuja määrän haluat tietää?")

print(len(kurssit))

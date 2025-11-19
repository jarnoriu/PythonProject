# Luo sanakirja oppilaista ja kursseista, joille he ovat ilmoittautuneet.
# Sanakirjassa avain on oppilaan nimi ja arvo on lista kursseista, joilla oppilas on. Luo sanakirja, jossa on valmiiksi ainakin 3 oppilasta kursseineen.
# Tulosta koko sanakirja arvoineen allekkaisille riveille.
from operator import truediv

oppilaat = {"Risto" : ["Ruotsi", "Englanti", "Saksa"],
            "Matti" : ["Laskento", "Uskonto"],
            "Tapani" : ["Aidinkieli", "Kuvis"]}

for item in oppilaat:
    print(f"Oppilas {item} on kursseilla {oppilaat[item]}")

#Kysy käyttäjältä uusi oppilas kursseineen lisättäväksi sanakirjaan.
# Kysy käyttäjältä kursseja, kunnes käyttäjä syöttää tyhjän.
# Tulosta uudelleen koko sanakirja, jotta näet että oppilas on lisätty.

uusi= input("Anna uuden oppilaan nimi?")
kurssit= []
print ("Anna seuraavaksi oppilaan kurssi?")

while True:
    kurssi = input("Anna seuraava kurssi?")
    if kurssi == "":
        break
    kurssit.append(kurssi)

    for itemz in oppilaat.items():
        print(itemz)


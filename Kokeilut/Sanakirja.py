#Hedelmä hinnasto sanakirjana
hedelmat = {"Ananas": "3.5",
           "Appelsiini":"7.5",
           "Banaani":"3","Kiivi":"5"
           }

h=input("Anna hedelmän jonka hinnan haluat tietää")
if h in hedelmat:
    print(f"{h}hinta on {hedelmat[h]}")
else:
    print(f"'{h} ei ole hintaa")
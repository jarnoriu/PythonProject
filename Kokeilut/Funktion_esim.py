# Funktion määritteleminen

def terve(tervehdys, kerrat):
    for k in range (kerrat):
        print(tervehdys)
    return

def yhteenlasku(_luku1, _luku2,_luku3):
    _summa = luku1 + luku2
    return _summa


# Pääohjelma


luku1 = int(input("Anna eka luku:"))
luku2 = int(input("Anna toinen luku:"))
luku3 = int(input("Anna kolmas luku:"))

summa= yhteenlasku (luku1, luku2, luku3)
print("Lukujen summa on", summa)

print("Uusi päivä alkaa tervehdyksellä:")
terve("Moikka!",3)
print("Jatketaan eteenpäin")
terve(" Hei! hei!", 5)





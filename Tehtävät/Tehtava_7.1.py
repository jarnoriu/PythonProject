#Luodaan tuple vuodenajat
vuodenajat= ("Talvi", "Kevät", "Kesä", "Syksy")

kuukausi = int(input("Anna kuukauden numero"))
if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
     print(f"{vuodenajat[0]}")
elif kuukausi == 3 or kuukausi == 4 or kuukausi == 5:
    print(f"{vuodenajat[1]}")
elif kuukausi == 6 or kuukausi == 7 or kuukausi == 8:
    print(f"{vuodenajat[2]}")
elif kuukausi == 9 or kuukausi == 10 or kuukausi == 11:
    print(f"{vuodenajat[3]}")
else:
    print("Ei ole kuukausi")

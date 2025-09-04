sukupuoli= input("Mikä on biologinen sukupuolesi?").upper()
hemo= int(input("Mikä on hemoglobiiniarvosi (g/l)?"))

if sukupuoli == "NAINEN":
    if hemo <117:
        print("Hemoglobiinisi on alhainen")
    elif hemo >= 117 and hemo <= 175:
        print("Hemoglobiinisi on normaali")
    elif hemo > 175:
        print("Hemoglobiinisi on korkea")
elif sukupuoli == "MIES":
    if hemo <134:
        print("Hemoglobiinisi on alhainen")
    elif hemo >= 134 and hemo <=195:
        print("Hemoglobiinisi on normaali")
    elif hemo > 195:
        print("Hemoglobiinisi on korkea")

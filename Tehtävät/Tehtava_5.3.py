
luku=int(input("Anna luku:"))

jaollisuus= 0
for i in range(1,luku+1):
    if luku % i == 0:
        jaollisuus +=1

if jaollisuus > 2:
    print (f"Luku ei ole alkuluku")
else:
    print (f"Luku on alkuluku")
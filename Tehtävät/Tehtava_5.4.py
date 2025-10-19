#Kysytään kaupungit

kaupungit= []

for i in range(5):
    kaupunki= input ("Anna kaupungin nimi: ")
    kaupungit.append(kaupunki)


#Tulostetaan taulukot

for i in range(len(kaupungit)):
    print(kaupungit[i])
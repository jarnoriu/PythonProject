import random
#random tuonti

a=random.randint(1,10)
print(a)

while True:
    arvaus = int(input("Arvaa luku:"))
    if arvaus == a:
        print("Oikein")
        break
    elif arvaus < a:
        print ("Liian pieni arvaus")
        continue
    elif arvaus > a:
        print ("Liian suuri arvaus")
        continue
    else:
        print(arvaus)
        continue

vuosi=int(input("Anna vuosiluku?"))

if vuosi >0:
    if vuosi % 4 == 0:
        print("Annettu vuosi on karkausvuosi")
    elif vuosi % 100 == 0 and vuosi % 400 == 0:
        print("Annettu vuosi on karkausi")




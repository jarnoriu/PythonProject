n= int(input("Anna kokonaisluku: "))

if n>0:
    if n % 3 == 0 and n % 5 == 0:
        print("BoomBuzz")
    else:
        if n % 3 == 0:
            print("Boom")
        if n % 5 == 0:
            print("Buzz")


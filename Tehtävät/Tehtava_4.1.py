#luodaan muuttuja number, joka on integer luku (kokonaisluku) 1
number= int(1)

#Toista kunnes numero on 1000
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number+=1

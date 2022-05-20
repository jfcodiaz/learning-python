import random

number = random.randint(0,100)

userNumber = -1
tries = 0

while(number != userNumber):
    print("Estoy pensando un numero entre 0 y 100, Que numero estoy pensando?")
    userNumber = int(input())
    if(userNumber != number):
        tries += 1
        print('Intenta de nuevo')
        if(userNumber > number):
            print('Estoy pensado un numero menor')
        else:
            print('Estoy pensando un numero mayor')
    else:
        print('Exacto ', userNumber, ' es mi numero, lo intentastes ', tries, 'Veces')

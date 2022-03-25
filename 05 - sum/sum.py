cadenaMensaje = 'Escribe un numero';
print(cadenaMensaje)


numero1 = int(input())
print('Escribe otro numero')

numero2EnCadena = input()
numero2Entero = int(numero2EnCadena)

resultado = numero1 + numero2Entero

print(str(numero1) + ' + ' + str(numero2Entero) + ' = ' + str(resultado))

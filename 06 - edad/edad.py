print('En que anio estamos?')
anioActual = int(input())

if anioActual > 2022 :
  print("No estamos en el futuro")
  quit()

print('En que mes estamos (numero)')
mesActual = int(input())

print('En que anio naciste?')
anioNaciomiento = int(input())

print('En que mes naciste?')
mesNacimiento = int(input())

edad = anioActual - anioNaciomiento

if mesActual < mesNacimiento :
  edad = edad - 1

print('Tu edad es ', edad)
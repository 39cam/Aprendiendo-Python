print('*** Identificar la estación del año ***')

numero = int(input('Ingresa el número para identificar la estación del año: '))

if numero == 1 or numero == 2 or numero == 12:
    print('Te encuentras en la estación de invierno ♦')
elif numero == 3 or numero == 4 or numero == 5:
    print('Te encuentras en la estación de primavera ♣')
elif numero == 6 or numero == 7 or numero == 8:
    print('Te encuentras en la estación de verano ♥')
elif numero == 9 or numero == 10 or numero == 11:
    print('Te encuentras en la estación de otoño ♠')
else:
    print('Estación desconocida')
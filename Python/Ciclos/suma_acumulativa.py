print('*** Suma acumulativa ***')

# Sumar los primeros 5 números

MAXIMO = 5
numero = 1
acumulador_suma = 0

while numero <= MAXIMO:
    acumulador_suma += numero
    numero += 1
    print(acumulador_suma, end=' ')

print(f'\nResultado de la suma acumulada: {acumulador_suma}')
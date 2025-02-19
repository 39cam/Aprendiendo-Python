# Generar valores aleatorios con la función rand int (valores numericos)

from random import *

entero_random = randint(0,10)
print(f"El número aleatorio es: {entero_random}") # Esto ya me está generando un valor aleatorio en el rango de números que le di (0 y 10)
# Esta función incluye los numeros en el parametro

#otra forma de indicar el módulo de una función es dado = random.randint(1,6)

# Simular dado de 6 caras
dado = randint(1,6)
print(f"El resultado del dado es: {dado}")




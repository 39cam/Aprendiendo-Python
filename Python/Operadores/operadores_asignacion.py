# Operador de asignación: se trata del más sencillo de usar

# Únicamente es el que utilizo al dar un valor a una variable (=)

print(f"*** Operadores de asignación ***")
numero = 5
print(f"\nValor del número 1: {numero}")

numero = 10
print(f"\nValor del número 1 modificado: {numero}")

cadena = "Saludos desde Python"
print(f"\nValor de la cadena: {cadena}")

# Como se puede ver, puedo asignar nuevos valores a una variable ya existente, todo con el fin de dar un valor a esta misma

# -------------------------------------------------- Asignación múltiple

# Yo puedo dar valores a distintas variables dentro de una misma línea de código, solo tengo que separar por comas

numero, numero2, cadena = 15, 18.2, 'queloque' # De esta manera dentro de una misma línea cambio los valores de algunas variables
# e incluso creo una en la misma línea de código

x,y,z = 5, 'Hola', -9.15

print(f"\n\nEl valor de la variable x es: {x}\nEl valor de y es: {y}\nEl valor de z es: {z}")

# -------------------------------------------------- Asignación encadenada

# Podemos definir varias variables y de esta manera puedo dar el mismo valor a todas estas

a = b = c = 10

print(f"\n\nEl valor de la variable a es: {a}\nEl valor de b es: {b}\nEl valor de c es: {c}")
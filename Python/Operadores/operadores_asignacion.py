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

# -------------------------------------------------- Intercambio de valores de una variable sin utilizar variables temporales

x, y = 5,10
print(f"\n\nValores iniciales x: {x}, y: {y}")
# Aplicando el concepto de asignación multiple, intercambiamos valores

x, y = y,x
print(f"Valores cambiados: x ahora con valor y: {x}, y ahora con valor x: {y}")


# Recibir multiples valores de la entrada del usuario
nombre, apellido = input("\n\nIngresa tu nombre y apellido separados por coma: ").split(",") # Sin este split me generaría un error grande, no se separarían las variables
print(f"El nombre es: {nombre.strip()} y el apellido es: {apellido.strip()}")

print("*** Evaluando un número entero ***")

num = int(input("Ingresa el número a evaluar"))

if num > 0:
    print(f'El número {num} es positivo')
elif num < 0:
    print(f"El número {num} es negativo")
else:
    print(f'El número es igual a cero')
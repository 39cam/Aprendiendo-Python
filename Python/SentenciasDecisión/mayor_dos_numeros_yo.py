# Programa para realizar comparación entre dos números, cuál es mayor y cuál es menor

print('*** Programa de evaluación de números ***')
num1 = int(input('Ingresa el número 1: '))
num2 = int(input('Ingresa el número 2: '))

if num1 > num2:
    print(f'El número 1 es mayor al número 2: {num1} > {num2}')
elif num1 == num2:
    print(f'Los números ingresados son iguales, vuelve a intentar con números distintos')
else:
    print(f'El número 2 es mayor al número 1: {num2} > {num1}')
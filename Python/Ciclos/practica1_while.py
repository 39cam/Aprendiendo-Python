# Código para contar números desde n hasta 1

n = int(input('Ingresa el número n que quieres que se utilice para el conteo: '))
m = n

while n > 0:
    print(f'El número es: {n}\n')
    n-=1

print(f'\n\nEl número inicial ingresado fue: {m} y lo anterior fue el conteo respectivo')
    
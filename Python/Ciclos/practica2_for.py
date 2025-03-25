# Sucesión de Fibonacci hasta 10 en un for en python

a, b = 0,1

for i in range(10):
    print(f'{a}')
    a,b = b, a+b

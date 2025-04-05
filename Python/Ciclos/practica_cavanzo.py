# Serie de Taylor para la función f(x)= exp(x^2)cos(x), realizando la integral

# Inicialmente, hago la serie para cada término para luego multiplicarles

import math

n = 10 # Será la cantidad de iteraciones que haré

def factorial(a):
    if a == 0:
        return 1
    resul = a
    for i in range(a -1, 0, -1):
        resul *= i
    return resul

def funexpo(x):

    funcion1 = 0

    for i in range (0,n):
        funcion1 += (x**(2*i))/factorial(i)

    return funcion1

def funcoseno(x):

    funcion2 = 0

    for i in range (0,n):
        funcion2 += (((-1)**i)*(x**(2*i)))/factorial(2*i)

    return funcion2

print('''\nAndrés Camilo Ocampo Castillo - 20222578098 - Métodos numéricos ☻
Prueba de funcionamiento de la serie de Taylor en total normalidad: ''')

print(f'''\n\n• El valor de la serie de Taylor para la función exponencial ^ (x^2) evaluada en 2 es igual a: {funexpo(2):.15f}
• El valor real es: {math.exp(2**2)}
• El valor de error por truncamiento es: {(math.exp(2**2) - funexpo(2)):.15f} 
• Y el porcentaje de error es {((math.exp(2**2) - funexpo(2))/(math.exp(2**2)) * 100):.5f}%''')

print(f'''\n\nEl valor de la serie de Taylor para la función coseno(x) evaluada en 2 es igual a: {funcoseno(2):.15f}
• El valor real es: {math.cos(2)}
• El valor de error por truncamiento es: {(math.cos(2)-funcoseno(2)):.15f} 
• Y el porcentaje de error es {(((math.cos(2)-funcoseno(2))/math.cos(2))*100):.5f}%''')

print('\n\n')

# Ahora hago la multiplicación de estas series antes de integrarlas
# Pero inicialmente pasaré la función a otro formato basado en sus coeficientes y exponentes para poder multiplicarles

nn = n

def coef_exp():

    print('Exponentes y coeficientes de la función e^(x^2)')
    coef = [0] * (2 * nn) # Su nombre bien lo indica, se trata de su coeficiente, dado en un vector
    # Ese (2 * nn) me indica el tamaño que le estoy dando a mi vector, dejando espacios vacios para lo q vaya a meter

    for i in range(nn):
        coef[2*i] = 1 / factorial(i)
        print(f'Índice {2 * i} - Coeficiente = {coef[2 * i]:.10f}')

    print('\n')
    return coef

def coef_cos():

    print('Exponentes y coeficientes de la función cos(x)')
    coef = [0] * (2 * nn)

    for i in range(nn):
        coef [2*i] = ((-1)**i) / factorial(2*i)
        print(f'Índice {2 * i} - Coeficiente = {coef[2 * i]:.10f}')
    print('\n')
    return coef

def multiplicar_polinomios(a, b):
    grado_max = len(a) + len(b) - 1
    resultado = [0] * grado_max
    for i in range(len(a)):
        for j in range(len(b)):
            resultado[i + j] += a[i] * b[j]
            print(f'Exponente x^{i + j}: Coeficiente = {resultado[i + j]:.10f}')
    return resultado

def integrar_y_evaluar(coef, x): # El x q mando por parametro ahora me permite realizar la integración para cambiar los valores correspondientes
    resultado = 0
    for i in range(len(coef)):
        nuevo_exponente = i + 1
        nuevo_coeficiente = coef[i] / nuevo_exponente
        resultado += nuevo_coeficiente * (x ** nuevo_exponente)
        print(f'∫x^{i} dx → Coeficiente: {nuevo_coeficiente:.10f}, Termino evaluado: {nuevo_coeficiente * (x ** nuevo_exponente):.10f}')
    return resultado

cosa1 = coef_exp()
cosa2 = coef_cos()
a_integrar = multiplicar_polinomios(cosa1,cosa2)

print('\n--------------------------------------------------------')

coef_exp()
coef_cos()

print('--------------------------------------------------------')
print('Ahora procedo a multiplicar dichas funciones para obtener mi polinómio y luego integrar\n')

multiplicar_polinomios(cosa1,cosa2)

print('\n--------------------------------------------------------\n')

print(f'\nValor de la integral definida con el valor 0\n')
valor1 = integrar_y_evaluar(a_integrar,0)
print('\n')

print(f'Valor de la integral definida con el valor 2\n')
valor2 = integrar_y_evaluar(a_integrar,2)
print('\n')

print(f'''\nResultado de la integral definida de f(x) = e^(x²)cos(x) entre 0 y 2:
∫₀² f(x) dx ≈ {valor2 - valor1:.10f} ☻''')
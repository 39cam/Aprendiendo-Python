print("*** Sistema de verificación: un número dentro de un rango ***")

MINIMO = 0
MAXIMO = 5

numero_evaluado = int(input("Ingresa el número a evaluar: "))

esta_en_rango = MINIMO <= numero_evaluado <= MAXIMO

print(f"El número ingresado \"{numero_evaluado}\" se encuentra dentro del rango ({MINIMO} - {MAXIMO})?: {esta_en_rango}")

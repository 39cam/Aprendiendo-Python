# Ejercicio hecho en el curso

print("*** Valor dentro de rango ***")

MINIMO = 0
MAXIMO = 5

# Solicitar un valor entre 0 y 5
dato = int(input(f"Proporciona un dato entre {MINIMO} y {MAXIMO}: "))

# Verificamos si el dato se encuentra dentro del rago
esta_dentro_rango = dato >= MINIMO and dato <= MAXIMO # Lo hace caso por caso, a diferencia de
                                                      # como lo hice yo
# Luego lo "simplifican" y lo hacen como yo
esta_dentro_rango = MINIMO <= dato <= MAXIMO

print(f"El valor está dentro de rango?: {esta_dentro_rango}")

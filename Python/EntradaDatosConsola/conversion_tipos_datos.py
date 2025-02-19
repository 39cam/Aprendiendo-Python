# Conversion de tipos de datos

# Convertir de cadena a número
numero_cadena = "10"
numero_entero = int(numero_cadena)
print(f"\nEl valor es: {numero_cadena} como cadena\nMientras que el valor númerico es: {numero_entero}\n")


# Convertir de cadena a flotante
numero_cadena = "3.1416"
numero_flotante = float(numero_cadena)
print(f"\nEl valor es: {numero_cadena} como cadena\nMientras que el valor númerico es: {numero_flotante}\n")

# Convertir de número a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f"\nEl valor es: {numero_entero} como número\nMientras que el valor en cadena ahora es: {numero_cadena}\n")

# Convertir a Booleano
# En Python es False en los siguientes casos: el valor es 0, cadena vacía o none: False
# En Python es True en los siguientes casos: el valor es != de 0, distinto a cadena vacía o distinto de none: True
numero_entero = 0 # Con este valor me debe retornar un False al imprimir
booleano = bool(numero_entero)
print(f"\nEl valor es: {numero_entero} como número\nEn algebra de bool es: {booleano}\n")

numero_entero = 39 # Con este valor me debe retornar un True al imprimir
booleano = bool(numero_entero)
print(f"\nEl valor es: {numero_entero} como número\nEn algebra de bool es: {booleano}\n")

cadena = '' # Al estar vacía me debe retornar False, esto tambien incluye el caso de colecciones o listas, si estan vacias, retorna False
booleano = bool(cadena)
print(f"\nEl valor es: \"{cadena}\" como cadena\nEn algebra de bool es: {booleano}\n")

cadena = 'Hola Mundo' # Al estar vacía me debe retornar False, esto tambien incluye el caso de colecciones o listas, si estan vacias, retorna False
booleano = bool(cadena)
print(f"\nEl valor es: \"{cadena}\" como cadena\nEn algebra de bool es: {booleano}\n")

variable = None # El valor None, debe tener la N en mayúsculas
booleano = bool(variable)
print(f"\nEl valor es: \"{variable}\" como valor de variable\nEn algebra de bool es: {booleano}\n")
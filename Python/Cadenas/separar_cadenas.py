# Separar cadenas: Método Split

datos = 'Hola Mundo'
lista = datos.split() # Por defecto me separa cada elemento por espacios en blanco
print(f"\nMi cadena es: {datos} y de allí se generó la lista: {lista}")
print(f"\nPrimer elemento de la lista {lista} es: {lista[0]}")

# Ahora armo una lista pero con un separador, puede ser una coma ","
datos2 = 'Camilo,19,Colombia'
lista = datos2.split(",")
print(f"\nNueva lista: {lista}, generada con la cadena {datos2}, separando por \",\"")
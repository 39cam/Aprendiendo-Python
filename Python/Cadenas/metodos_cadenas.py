# Metodos (algunos) de cadenas Python

cadena1 = 'Hola Mundo'
print(f'Cadena original: {cadena1}')

# Todo en mayusculas manin: metodo upper
mayusculas = cadena1.upper()
print(f'Cadena en mayusculas: {mayusculas}')

# Todo en minusculas manin: el metodo lower
minusculas = cadena1.lower()
print(f'Cadena en minusculas: {minusculas}')

# Quita los espacios al comienzo y fin de una cadena
cadena2 = '   Juanito gamer   '
print(f'La cadena 2 original: {cadena2}')
print(f'La cadena sin espacios al principio y fin: {cadena2.strip()}') # Eliminando los espacios en blanco al principio y al final de la cadena
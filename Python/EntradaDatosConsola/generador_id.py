from random import randint

print("*** Sistema Generador de ID Único")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
anio = input("Ingrese su año de nacimiento: ")

# Normalizar valores
nom_2 = nombre.strip().upper()[0:2] # Esta manera me permite sacar los 2 primeros caracteres, sin necesidad de concatenar
ape_2 = apellido.strip().upper()[0:2]
anio_2 = anio[2:4]

# Generar el valor aleatorio
aleatorio = randint(1000, 9999)
# aleatorio = str(randint(1000,9999)) # Si el id lo generara de la manera comentariada me tocaría parsearlo a string

# Generar el id único
id = f"{nom_2}{ape_2}{anio_2}{aleatorio}"
# id = nom_2 + ape_2 + anio_2 + aleatorio # De lo contrario me arrojaría error, porque lo toma como un valor entero gracias a la función randint

# Imprimir datos
print(f"\nNombre del usuario: {nombre}")
print(f"\nNombre normalizado: {nom_2}")
print(f"\nApellido del usuario: {apellido}")
print(f"\nApellido normalizado: {ape_2}")
print(f"\nAño de nacimiento del usuario: {anio}")
print(f"\nAño de nacimiento normalizado: {anio_2}")
print(f"\nValor aleatorio del 1111 al 9999: {aleatorio}")
print(f"\nId único generado: {id}")


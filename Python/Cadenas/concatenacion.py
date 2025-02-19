# Vamos a concatenar cadenas sin crear variables

cadena1 = "Buenos días"
cadena2 = "Colombia"
cadena3 = "Bogotá"
print("Hola"+ " " + "Mundo")

print("\nHola" + " " + "Mundo" + " " + cadena1)
print("\nSi,",cadena1)

### Clase - Concatenación de cadenas

cadena1 = 'Hola'
cadena2 = 'Mundo'
concatenacion = cadena1 + " " +cadena2 + "\n\n"

print("\n\n"+concatenacion)

# Utilizando el metodo join

concatenacion = ''.join([cadena1, " ", cadena2])
print(concatenacion)
# Completando el código "sentencia_if_else"

print('*** Sentencia if else***')

edad = int(input("Igresa tu edad: "))

if edad >= 18:
    print(f"Eres mayor de edad, tienes {edad} años")
elif 13 <= edad < 18: # Elif se trata de la abreviación de else if, en donde también debo poner una condición
    print(f'Eres un adolescente, tienes {edad} años')
else:
    print(f"Eres menor de edad, tienes {edad} años")





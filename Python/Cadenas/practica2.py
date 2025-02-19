# En este proyecto voy a poner en práctica cada una de las funciones que recuerdo que he visto hasta el momento del módulo de cadenas

cadena1 = "     Hola Mundo     "

largo = len(cadena1) # Función len, para extraer la longitud de la cadena que tengo

cadena2 = cadena1.upper() # Función upper: va a hacer que mi cadena esté en mayúsculas

cadena3 = cadena1.lower() # Función lower: Me es útil para dejar mis caracteres en minúsculas

cadena4 = cadena1.strip() # Función Strip: Le va a quitar los espacios que tiene a comienzo y final de la cadena

caracter2 = cadena1.strip()[1] # Voy a probar esto a ver si función, debería mostrarme la "o"

print(f"En este texto voy a enseñar aquello que he guardado en mis variables, la siguiente es mi cadena1: {cadena1}\n\nEsta de acá es la longitud de la cadena: {largo}\n\n"
      f"Esta es la cadena en mayusculas: {cadena2}\n\nLa cadena en minusculas: {cadena3}\n\nLa cadena sin espacios: {cadena4}\n\nEsto debería decir \"o\" si funcionase: {caracter2}")

cadena5 = "".join([cadena4+caracter2]) # Función join para meter variables en una cadena
print("\n"+cadena5)

cadena6 = "{}: {}".format(cadena4,caracter2) # Función format (es más vieja que la panela, se usa más la f"...")
print(f"\n{cadena6}")

# Duro papi, le metiste con bendición ve
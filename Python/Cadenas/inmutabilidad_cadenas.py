# Inmutabilidad en cadenas en Python
cadena1 = 'Hola Mundo'
# cadena1[0] = 'h' No se pueden modificar ninguno de sus elementos, esto me arroja error
print(cadena1)

cadena2 = cadena1 # Antes de eliminar la info lo guardo en otra variable

cadena1 = 'Adios' # Asigno un nuevo valor y se elimina el anterior valor y espacio de memoria que tenía la variable cadena1

print()
print(cadena2) # Me está enseñando el valor que tenía la variable 1 inicialmente,
# ya que accede al mismo espacio de memoria donde se encontraba cadena1 con la info 'Hola Mundo'
print(cadena1)





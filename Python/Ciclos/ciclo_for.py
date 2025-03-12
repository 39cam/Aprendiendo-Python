print('*** Ciclo for ***')

cadena = 'Hola Mundo'

# Iteramos los caracteres de la cadena
print('Impresión de cadena dividida')
for letra in cadena: # No se trata de que la variable letra almacene a cadena, unicamente divide e itera la cadena y ya
    print(letra, end='  ')
# print(letra) esto no me imprimiría nada

# -------------------------------------------- Otro ejemplo
print('\n')

print('Impresión de la lista de frutas')
frutas = ['Plátano', 'Fresa', 'Mango']
for frutica in frutas: # Defino la variable, sin necesariamente darle tipo, gracias al manejo de los datos en python sin tipado
    # Entonces básicamente la variable que defino acá accede a esa lista y simplemente itera la lista que en este caso es frutas
    print(frutica, end=' ')
print("*** Sistema generador de emails ***")

nombre = input("Cual es tu nombre?: ")
apellidos = input("Cuales son tus apellidos?: ")
empresa = input("Cual es la empresa?: ")
dominio = input("Cual es el dominio?: ")

# Normalización de valores recibidos
nombre =  nombre.strip().lower().replace(" ",".")
apellidos = apellidos.strip().lower().replace(" ", ".")
empresa = empresa.strip().lower().replace(" ","")
dominio = dominio.strip().lower().replace(" ","")

# Email generado
mail = f"{nombre}.{apellidos}@{empresa}{dominio}"

# Imprimir mi email generado
print(f''' El mail generado fue:
{mail}
''')
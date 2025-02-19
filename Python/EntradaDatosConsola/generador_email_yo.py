# Sistema generador de emails

print("*** Sistema generador de emails ***")

nombre = input("Ingrese sus nombre: ")
apellido = input("Ingrese sus apellidos: ")
empresa = input("Ingrese el nombre de la empresa para la que trabaja: ")
dominio_empresa = input("Ingrese el dominio de la empresa")

# Normalización

nom_norm = nombre.strip().lower().replace(" ",".")
apel_norm = apellido.strip().lower().replace(" ",".")
emp_norm = empresa.strip().lower().replace(" ","")

# Generar el email

mail = f"{nom_norm}.{apel_norm}@{emp_norm}{dominio_empresa}"

# Imprimir en pantalla

print(f"\n El correo generado con dicho datos es: {mail}")
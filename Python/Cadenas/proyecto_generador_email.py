# Proyecto de generar dominio de correo electronico a partir de datos como: nombre, empresa y dominio

nombre = "Andrés Camilo Ocampo Castillo"
empresa = "Piscis mob"
dominio = ".com.co"

nombre_minus = nombre.lower() # Nombre con la función lower
empresa_minus = empresa.lower() # Empresa con la función lower
lista_nombre = nombre_minus.split()
lista_empresa = empresa_minus.split()
nombre_normalizado = f"{lista_nombre[0]}.{lista_nombre[1]}.{lista_nombre[2]}"
empresa_normalizada = f'{lista_empresa[0]}{lista_empresa[1]}'
dominio_normalizado = f'@{empresa_normalizada}{dominio}'
email = f'{nombre_normalizado}{dominio_normalizado}'

print(f"\nEl nombre del usuario es: {nombre}\nLa empresa del usuario es: {empresa}\nEl dominio que utiliza la empresa es: {dominio}")
print(f"\nEl nombre del usuario normalizado es: {nombre_normalizado}\nEl dominio de la empresa normalizado es: {dominio_normalizado}\n")

print(f"El email del usuario es: {email}")



print("*** Generador de emails ***")

nombre_completo = " Andrés Camilo Ocampo Castillo"
# Elimino los espacios en blanco, dejo en minusculas y además remplazo los espacios por puntos
nombre_usuario = nombre_completo.strip().lower().replace(" ",".")
print(f"El nombre completo del usuario es: {nombre_completo}\n")
print(f"El nombre del usuario normalizado es: {nombre_usuario}\n")

empresa = "  Piscis mob  "
# Dejo en minusculas y reemplazo valores de espacios en blanco por cadenas vacias
empresa_usuario = empresa.lower().replace(" ","")
print(f"El nombre de la empresa es: {empresa}\n")
print(f"El nombre de la empresa normalizado es: {empresa_usuario}\n")

dominio = ".com.co"
dominio_normalizado = f"@{empresa_usuario}{dominio}"

print(f"El dominio de la empresa normalizado es: {dominio_normalizado}\n")

# Genero el email a partir del nombre de usuario y el dominio de la empresa
email = f"{nombre_usuario}{dominio_normalizado}"
print(f"El correo generado para el usuario es: {email}")
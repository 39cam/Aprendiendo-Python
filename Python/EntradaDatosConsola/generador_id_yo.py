# Sistema generador de Id unico para un usuario

from random import randint

print("*** Sistema generador de Ids por usuario ***")

nombre_usuario = input("Por favor ingrese su nombre: ")
apellido_usuario = input("Por favor ingrese su apellido: ")
año_nacimiento = input("Ingrese su año de nacimiento: ")
valor_aleatorio = str(randint(1000,9999))


nombre_usuario_upper = (nombre_usuario[0] + nombre_usuario[1]).upper()
apellido_usuario_upper = (apellido_usuario[0] + apellido_usuario[1]).upper()
año_nacimiento_final = (año_nacimiento[2] + año_nacimiento[3])

id_usuario = nombre_usuario_upper + apellido_usuario_upper + año_nacimiento_final + valor_aleatorio

print(f"\n\nEl nombre del usuario es: {nombre_usuario}")
print(f"\nEl apellido del usuario es: {apellido_usuario}")
print(f"\nEl año de nacimiento de {nombre_usuario}: {año_nacimiento}")
print(f"\nEl id generado fue: {id_usuario}")

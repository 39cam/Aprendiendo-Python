print("*** Sistema de autenticación ***") # El q yo hice

NOMBRE_USUARIO = 'Admin'
CONTRASENA_USUARIO = 'Admincontra123'

usuario = input("Por favor digita el nombre de usuario: ")
contraseña = input("Por favor digita la contraseña: ")

valido = usuario == NOMBRE_USUARIO and contraseña == CONTRASENA_USUARIO

print(f"Los datos ingresados son validos?: {valido}")

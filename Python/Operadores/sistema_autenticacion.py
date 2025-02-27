print("*** Sistema de autenticación ***")

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario_registrado = input("Cuál es tu usuario?: ")
password_registrado = input("Cuál es tu password?: ")

son_datos_correctos = usuario_registrado.strip() == USUARIO_VALIDO and password_registrado.strip() == PASSWORD_VALIDO

print(f"Los datos son correctos?: {son_datos_correctos}")

# Me quedó literalmente igual ^^


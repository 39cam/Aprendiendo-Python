print('*** Sistema de autenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario = input('Ingresa tu usuario: ')
password = input('Ingresa tu password: ')

if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
    print('Bienvenido al sistema')
elif usuario == USUARIO_VALIDO:
    print('Password incorrecto, por favor corregirlo!')
elif password == PASSWORD_VALIDO:
    print('Usuario incorrecto, por favor corregirlo!')
else:
    print('Usuario y Password incorrectos, por favor corregirlos!')
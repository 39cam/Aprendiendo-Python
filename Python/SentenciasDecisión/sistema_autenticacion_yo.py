print('*** Sistema de validación ***')

usuario = 'Admin'
password = '123456'

usuario_ingresado = input('Ingresa tu nombre de usuario: ')
password_ingresado = input('Ingresa tu contraseña: ')

if usuario_ingresado == usuario and password_ingresado == password:
    print(f'Bienvenid@ {usuario}')
elif usuario_ingresado != usuario and password_ingresado == password:
    print(f'Usuario incorrecto, intenta de nuevo')
elif usuario_ingresado == usuario and password_ingresado != password:
    print(f'Contraseña incorrecta, intenta de nuevo')
else:
    print(f'Usuario y contraseña incorrectos, intenta de nuevo')
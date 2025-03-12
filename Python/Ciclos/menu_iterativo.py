print('*** Sistema de administración de cuentas ***')

salir = False

while not salir:
    print(f'''Menú:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir''')

    opcion = int(input('Escoge tu opción: '))

    if opcion == 1:
        print('Creando cuenta\n')
    elif opcion == 2:
        print('Eliminando cuenta\n')
    elif opcion == 3:
        print('Saliendo del sistema, hasta pronto\n')
        salir = True
    else:
        print('Por favor ingrese una opción válida.\n')
else:
    print('Terminando el sistema de administración de cuentas')
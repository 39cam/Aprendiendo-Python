print('*** Bienvenido al sistema bancario ***')

salir_sistema_txt = input('Deseas salir del sistema? (Si / No): ')
salir_sistema = salir_sistema_txt.strip().lower() == 'si'

if not salir_sistema:
    print(f'Continuamos dentro del sistema: {salir_sistema}')
else:
    print(f'Saliendo del sistema: {salir_sistema}')




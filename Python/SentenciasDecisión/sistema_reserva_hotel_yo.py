print('*** Bienvenido al hotel ***')

# Valores por día
CUARTO_CON_VISTA_MAR = 190.50
CUARTO_SIN_VISTA_MAR = 150.50

# Solicitud de datos
nombre_cliente = input('Ingrese su nombre: ')
dias_estadia = int(input('Cuantos días desea hospedarse?: '))
cuarto_vista_mar = input('Deseas un cuarto con vista al mar? (Si / No): ').strip().lower() == 'si'

# Logica e impresión de datos
if cuarto_vista_mar:
    print(f'Apreciado(a) {nombre_cliente}, el valor de la estadía por {dias_estadia} en un cuarto con vista al mar tendrá un costo de: {(dias_estadia * CUARTO_CON_VISTA_MAR):.2f}')
else:
    print(f'Apreciado(a) {nombre_cliente}, el valor de la estadía por {dias_estadia} en un cuarto sin vista al mar tendrá un costo de: {(dias_estadia * CUARTO_SIN_VISTA_MAR):.2F}')
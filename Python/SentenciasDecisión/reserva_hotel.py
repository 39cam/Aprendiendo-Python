print('*** Sistema de reserva de hotel ***')

# Variables del hotel
tarifa_diaria_sin_vista_mar = 150.50
tarifa_diaria_con_vista_mar = 190.50

# Pedimos la info al usuario
nombre_cliente = input('Nombre del cliente: ')
dias_estadia = int(input('Días de estadía: '))
vista_al_mar_txt = input('Con vista al mar? (Si / No): ')
vista_al_mar = vista_al_mar_txt.strip().lower() == 'si'

# Cálculos del costo total de la estancia
if vista_al_mar:
    costo_total = dias_estadia * tarifa_diaria_con_vista_mar
else:
    costo_total = dias_estadia * tarifa_diaria_sin_vista_mar

# Detalles de la reserva
print(f'''\nDetalles de la reservación
Cliente: {nombre_cliente}
Días de estadía: {dias_estadia}
Costo total: {costo_total:.2f}
Habitación con vista al mar?: {'Si' if vista_al_mar else 'No'}''')

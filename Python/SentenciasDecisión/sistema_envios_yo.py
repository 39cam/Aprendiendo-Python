print('*** Sistema de envíos ***')

tipo_envio = input('Ingresa el tipo de envío (Nacional / Internacional): ')
peso_kg = float(input('Ingresa el peso en kilogramos que tendrá el envío: '))
costo_tarifa = None

if tipo_envio.strip().lower() == 'nacional':
    costo_tarifa = 10 * peso_kg
elif tipo_envio.strip().lower() == 'internacional':
    costo_tarifa = 20 * peso_kg
else:
    print('Tipo de envio desconocido, por favor intenta nuevamente')
    exit()

print(f'Señor usuario, el coste por un envío de tipo {tipo_envio.strip().lower()} con {peso_kg:.2f} kg de peso es de: {costo_tarifa:.1f}')
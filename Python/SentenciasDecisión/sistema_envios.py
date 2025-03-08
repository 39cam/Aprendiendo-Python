print('*** Sistema de envíos ***')

# Definimos las tarifas de envío por kilogramo

TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

# Solicitud de valores de destino

destino = input('Ingresa el destino del paquete (nacional/internacional): ')
peso = float(input('Ingresa el peso del paquete en kg: '))

# Cálculo del envío del paquete
costo_envio = None
destino = destino.strip().lower()

if destino == 'nacional':
    costo_envio = peso * TARIFA_NACIONAL
elif destino == 'internacional':
    costo_envio = peso * TARIFA_INTERNACIONAL
else:
    print(f'Destino: {destino} no valido. Ingresa el valor de nacional o internacional')

# Mostrando costo de envío solo si es un valor valido
if costo_envio is not None:
    print(f'El costo del envío del paquete es: ${costo_envio:.2f}')
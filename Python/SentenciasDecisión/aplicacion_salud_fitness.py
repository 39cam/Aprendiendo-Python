print('*** Aplicación de Salud y Fitness ***')

# Constantes
META_PASOS_DIARIOS = 1000
CALORIAS_POR_PASO = 0.04

# Solicitud de datos
nombre_user = input('Cual es tu nombre?: ')
pasos_diarios= int(input('Cuantos pasos has caminado hoy?: '))

# Verificar si el usuario alcanzó la meta de pasos diaria
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'

# Calorías quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Imprimir info
print(f'\nUsuario: {nombre_user}'
      f'\nCantidad de pasos de hoy: {pasos_diarios}'
      f'\nCalorias quemadas: {calorias_quemadas} kcal'
      f'\nLa meta de pasos diaria fue alcanzada?: {meta_alcanzada_txt}, • tus pasos: {pasos_diarios} • meta establecida: {META_PASOS_DIARIOS}')
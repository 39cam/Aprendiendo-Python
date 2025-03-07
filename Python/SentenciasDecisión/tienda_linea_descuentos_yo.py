print('*** Sistema de venta en linea ***')

MONTO_10 = 1000;
MIEMBRO = 'si'

nombre_usuario = input("Cuál es tu nombre?: ")
es_miembro = input("Eres miembro de la tienda?: ").strip().lower() == MIEMBRO
monto_compra = int(input("Por favor ingresa el monto de tu compra: "))
descuento_monto = 0

if es_miembro and monto_compra > MONTO_10:
    descuento_monto = monto_compra * 0.10
    print(f'''Felicidades señor(a): {nombre_usuario}
    Eres beneficiario del 10% de descuento por ser miembro de la tienda y tener una compra mayor a {MONTO_10}: {monto_compra}
    Tu compra tiene un monto de: {monto_compra}
    Valor del descuento (10%): {descuento_monto}
    Valor final a pagar: {monto_compra - descuento_monto}  
    ''')
elif es_miembro:
    descuento_monto = monto_compra * 0.05
    print(f'''Felicidades señor(a): {nombre_usuario}
    Eres beneficiario del 5% de descuento por ser miembro de la tienda
    Tu compra tiene un monto de: {monto_compra}
    Valor del descuento (5%): {descuento_monto}
    Valor final a pagar: {monto_compra - descuento_monto}  
    ''')
else:
    print(f"Señor(a) {nombre_usuario} su valor a pagar es de: {monto_compra}")


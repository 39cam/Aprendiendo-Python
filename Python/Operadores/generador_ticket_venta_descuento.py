# De base dejo la misma estructura de código que: generador_ticket_venta.py
print("*** Generación de ticket de Venta ***")

precio_leche = float(input("Ingresa el precio de la leche: "))
precio_pan = float(input("Ingrese el precio del pan: "))
precio_lechuga = float(input("Ingrese el precio de la lechuga: "))
precio_platanos = float(input("Ingrese el precio de los platanos: "))
descuento_porcentaja = int(input("Ingrese el porcentaje de descuento a aplicar: "))

# Cálculo del subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Aplicar descuento
descuento = subtotal * (descuento_porcentaja/100)

# Subtotal con descuento
subtotal_descuento = subtotal - descuento

# Cálculo de impuestos (16%)
impuesto = subtotal_descuento * 0.16

# Calculo total de la compra
total = subtotal_descuento + impuesto

# Resultados en pantalla
print(f'''Subtotal: ${subtotal:.2f}
Descuento aplicado al subtotal ({descuento_porcentaja}%): ${descuento:.2f}
Subtotal con descuento: ${subtotal_descuento:.2f}
Valor en impuestos (16%): ${impuesto:.2f}
Valor total de compra: ${total:.2f} ''')
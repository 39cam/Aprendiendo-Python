print("*** Generación de ticket de Venta ***")

precio_leche = float(input("Ingresa el precio de la leche: "))
precio_pan = float(input("Ingrese el precio del pan: "))
precio_lechuga = float(input("Ingrese el precio de la lechuga: "))
precio_platanos = float(input("Ingrese el precio de los platanos: "))

# Cálculo del subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Cálculo de impuestos (16%)
impuesto = subtotal * 0.16

# Calculo total de la compra
total = subtotal + impuesto

# Resultados en pantalla
print(f'''Subtotal: {subtotal:.2f}
Valor en impuestos (16%): {impuesto:.2f}
Valor total de compra: {total:.2f} 
''')
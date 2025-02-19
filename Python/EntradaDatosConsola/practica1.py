# En esta práctica voy a hacer un ejercicio de tipo sistema
from datetime import datetime
from os.path import split

print("\n*** Sistema de venta Koaj ***\n")

fecha = datetime

print(f"Fecha actual: {fecha}")

nombre_empleado = input("\nPor favor registra el nombre del empleado: ")
edad_empleado = int(input(f"\nDigita la edad del empleado {nombre_empleado}: "))

print(f"Bienvenido señor(a) {nombre_empleado}, su edad es {edad_empleado}, prontamente cumplirá {edad_empleado + 1}\n")

nombre_cliente = input("Ingresa el nombre del cliente: ")
edad_cliente = int(input("\nDigita la edad del cliente: "))
correo_cliente = input("\nDigita el correo electrónico del cliente: ")
productos_compra = input(f"Ingresa los productos que acaba de comprar el cliente {nombre_cliente}: ").split(" ")
tota_venta = float(input("Ingresa el total de la venta"))

print(f"\n\n\nDatos de venta:\n")
print(f"\nLa fecha de la venta es {fecha}")
print(f"\nNombre del empleado a cargo de la venta: {nombre_empleado}, tiene una edad de {edad_empleado}")
print(f"\nNombre del cliente comprador: {nombre_cliente}, con una edad de {edad_cliente}")
print(f"\nLos productos que el cliente ha llevado son: {productos_compra}")
print(f"\nEl valor total de la venta es {tota_venta}")







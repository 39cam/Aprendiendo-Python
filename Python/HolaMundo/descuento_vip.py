print(f"\n***Sistema de descuentos VIP ***")

cantidad_productos_descuento = 10
cantidad_productos_dia = int(input("Cuantos productos compraste hoy?: "))
tiene_memebresia = input("Tienes la membresía de la tienda? (Si/No): ")
tiene_memebresia = tiene_memebresia.strip().lower()

es_elegible_descuento = ((cantidad_productos_dia >= cantidad_productos_descuento)
                         and (tiene_memebresia) == 'si')

print(f"\nTienes acceso al descuento VIP?: {es_elegible_descuento}")

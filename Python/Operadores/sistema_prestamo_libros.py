from unittest.mock import NonCallableMock

print("*** Sistema préstamo de libros ***")

DISTANCIA_PERMITIDA_KM = 3
nombre_usuario = input("Ingresa tu nombre: ")
nombre_usuario = nombre_usuario.strip().lower()
tiene_credencial = input("Cuentas con credencial de estudiante? (Si o No): ")
tiene_credencial = tiene_credencial.strip().lower()
distancia_biblioteca_km = int(input("A cuantos kilómetros vives de la biblioteca?: "))

es_elegible_prestamo = ((tiene_credencial == 'si')  or
                        distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM)

print(f'''Señor(a) {nombre_usuario}, según los datos ingresados, es usted beneficiario de prestamo?
{es_elegible_prestamo}''')
# Para diferenciar variables y constantes en Python, debo específicamete para mi constante utilizar mayusculas en su definición
import math

PI = 3.14159
print("El valor de pi es: ",PI)

NOMBRE_BASE_DATOS = "cliente.db"
print("El nombre de la base de datos es:",NOMBRE_BASE_DATOS)

# LO SIGUIENTE NO SE DEBE HACER POR BUENA PRACTICA DE PROGRAMACIÓN EN PYTHON (SI ESTÁ EN MAYUS ES CONSTANTE: SE QUEDA COMO ESTÁ)
print()
NOMBRE_BASE_DATOS = "sistemaventas.db"
print("pao pao, porqué le cambió el valor a una constante???:",NOMBRE_BASE_DATOS)

# Acceso a nuevos temas, por ejemplo pi, no tomandola como constante
print()
print("El valor de pi (Constante) es:", PI)
print("El valor de pi (Librería math) es:", math.pi)
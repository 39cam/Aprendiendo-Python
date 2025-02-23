# Práctica 1 de comparadores

print(f"\n*** Sistema de gestión academica ***")

promedio_clave = 4.0
nombre_alumno = input("\nIngresa tu nombre: ")
nombre_alumno = nombre_alumno.strip().lower()
promedio_alumno = float(input("\nCual es tu promedio actual?: "))
materias_perdidas = int(input("\nCuantas materias perdiste este semestre?: "))

es_beneficiario_alimentacion = (promedio_alumno >= promedio_clave) or (materias_perdidas == 0) # Un promedio mayor o igual o no haber perdido materias
es_joven_en_accion = (promedio_alumno > promedio_clave) and (materias_perdidas == 0) # Tener promedio > al base y no perder materias

print(f'''\n\nSeñor(a): {nombre_alumno}, cuenta con un promedio de {promedio_alumno:.2f}
Usted es beneficiario del bono alimenticio?: {es_beneficiario_alimentacion}
Usted es beneficiario de jovenes en accion?: {es_joven_en_accion}''')
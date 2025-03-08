print('*** Asignación de calificación ***')

nota = int(input('Digita la nota: '))
calificacion = None

if 9<= nota <= 10:
    calificacion = 'A'
elif 8 <= nota < 9:
    calificacion = 'B'
elif 7 <= nota < 8:
    calificacion = 'C'
elif 6 <= nota < 7:
    calificacion = 'D'
elif 0 <= nota < 6:
    calificacion = 'F'
else:
    calificacion = 'Nota desconocida, recuerda ingresar un valor de 0 a 10'

# Imprimir el equivalente en calificación
print(f'La calificación equivalente a la nota {nota} es: {calificacion}')


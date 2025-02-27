# Ejercicio hecho en el curso

print("*** Calculo de area y perimetro de un rectángulo ***")

base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

# Realizamos los calculos
area = base * altura
perimetro = 2 * (base + altura)

print(f'''El área del rectángulo es: {area}
El perimetro del rectángulo es: {perimetro}''')

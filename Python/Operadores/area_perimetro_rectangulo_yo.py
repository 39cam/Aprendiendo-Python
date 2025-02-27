print("*** Sistema para cálculo de área y perimetro de un rectángulo ***")

base = int(input("Por favor digita la base del rectángulo: "))
altura = int(input("Por favor digita la altura del rectángulo: "))

area = base * altura
perimetro = 2*(base + altura)

print(f'''El área del rectángulo es: {area}
El perimetro del rectángulo es: {perimetro}''')

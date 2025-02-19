# Se trata de los operadores que utilizamos al realizar operaciones aritméticas
# Tales como pueden ser

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

#Suma (en donde en principio se tienen dos operandos y un operador (+)), se trata de una operación conmutativa
print(f"\nSuma 1: {num1 + num2}")
print(f"\nSuma 2: {num2 + num1}")

# Resta (2 operandos y un operador (-)) Me pueden dar valores negativos, segun lo que yo estoy restando
print(f"\nResta 1: {num1 - num2}")
print(f"\nResta 2: {num2 - num1}")

# Multiplicación (2 operandos y un operador (*)) la multiplicación es conmutativa
print(f"\nMultiplicación 1: {num1*num2}")
print(f"\nMultiplicación 2: {num2*num1}")

# División para resultado flotante (2 operandos y un operador (/)) este tipo de división me puede devolver un flotante // La división por cero me arroja error
print(f"\nDivisión 1 (flotante): {num1 / num2}")
print(f"\nDivisión 2 (flotante): {num2 / num1}")

print(f"\nDivisión 2 (flotante, solo 2 valores decimales): {(num2 / num1):.2f}") # Acá voy a controlar la cantidad de decimales que enseño en pantalla

# División para resultado entero (2 operandos y 1 operador doble (//) me genera un resultado entero antes del punto decimal, es decir, no redondea)
print(f"\nDivisión 1 (entero): {num1//num2}")
print(f"\nDivisión 2 (entero): {num2//num1}")

# Modulo (%) me regresa el residuo de la división
print(f"\nModulo 1: {num1%num2}")
print(f"\nModulo 2: {num2%num1}")

# Exponente (**) me regresa el valor del primer operando elevado a la potencia del segundo
print(f"\nPotencia 1: {num1**num2}")
print(f"\nPotencia 2: {num2**num1}")
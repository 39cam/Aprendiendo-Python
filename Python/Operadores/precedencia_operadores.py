# 1. Paréntesis (): Los paréntesis tienen la mayor precedencia
# 2. Exponente **: Este operador calcula la potencia de un número.
# 3. Unario +, -: Estos operadores realizan operaciones unarias de positivo y negativo
# 4. Multiplicación *, División /, División entera //, Módulo %
# 5. Suma +, Resta -: Estos operadores realizan operaciones aritméticas.
# 6. Comparaciones (==, !=, >, <, >=, <=)
# 7. Operadores lógicos not, and, or
# 8. Asignación (=, +=, -=, *=, /=, entre otros)

# Ejemplo de precedencia de operadores
# 1. División 12 / 3 = 4
# 2. Multiplicación 2 * 3 = 6
# 3. Suma (4) + (6) = 10
# 4. Resta (10) - 1 = 9
resultado =  12 / 3 + 2 * 3 - 1 # Me da un resultado flotante gracias a que estoy haciendo
# Una división de punto flotante
resultado_entero =  12 // 3 + 2 * 3 - 1 # Me dara como resultado un valor entero gracias
# A la división entera dada en el funcinamiento de Python
print(f"El resultado de la expresión es: {resultado}")
print(f"El resultado de la expresión es: {resultado_entero}")
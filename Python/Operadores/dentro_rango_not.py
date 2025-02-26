# Revisar si una variable se encuentra dentro de un rango entre 1 y 10
dato = int(input("Ingresa un número entero a evaluar: "))

# Revisando si el entero está en rango
esta_dentro_rango = 1 <= dato <= 10
print(f"La variable está dentro de rango?: {esta_dentro_rango}")

# Revisando la lógica inversa: Saber si el entero está fuera de rango
esta_fuera_rango = not(1<= dato <=10)
print(f"La variable está fuera de rango?: {esta_fuera_rango}")

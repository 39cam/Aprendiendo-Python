print("\n*** Operador NOT ***")

condicion1 = True
resultado = not condicion1
print(f"Operador not sobre {condicion1}: {resultado}")

# Revisando si una variable es cadena vacía
nombre = ''
es_cadena_vacia = not nombre # Esto se lee un poco raro para lo que he visto:
# Al aplicar el operador not, no se está igualando la cadena como tal, si no se está revisando si es vacía, es decir
# En el caso de que la cadena "nombre" esté vacía, al aplicar el not se hace verdadero, por decirlo de alguna manera, toma nulo como False
# Al aplicar el not, lo hace True. Ahora bien, si insertamos texto en la cadena, se toma como True, al aplicar Not, se hace False
print(f"La cadena \"{nombre}\" es vacía?: {es_cadena_vacia}")

# Revisar si una variable no tiene ningun valor asignado
variable = None
es_variable_vacia = not variable
print(f"La variable \"{variable}\" es una variable vacía?: {es_variable_vacia}")


# ----------------------- Experimento mío

cadena = 'hola'
resul = bool(cadena)

print(f"\n\n\nLa cadena \"{cadena}\" tiene texto dentro de ella?: {resul}")
print(f"Ahora negamos lo anterior, la cadena \"{cadena}\" tiene texto en ella?: {not resul}")

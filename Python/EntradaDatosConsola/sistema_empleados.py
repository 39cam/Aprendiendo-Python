print("*** Sistema de empleados ***\nBienvenido señor usuario")

nombre = input("Por favor ingrese su nombre: ")
edad = int(input(f"Bienvenido {nombre} por favor ingrese su edad: "))
salario = float(input("Ingrese su salario: "))
es_jefe_departamento = input("Es usted jefe de departamento? Digite Si o No: ")

# Haciendo booleana la variable es_jefe _departamento
es_jefe_departamento = es_jefe_departamento.lower() == "si" # Este tipo de comparación hace que esta variable tome un valor booleano
# Si recibe una cadena diferente a: si, entonces lo tomará como no, o como False

# Imprimiendo resultados
print(f"\nSu nombre es {nombre}, tiene una edad de {edad}, cuenta con un salario de {salario:.2f} y {es_jefe_departamento} es jefe de departamento")
# Aquello que hice en la variable salario, es indicar que deseo 2 decimales después del punto, además f indica que es un valor tipo flotante
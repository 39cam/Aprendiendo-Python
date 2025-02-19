print("*** Receta de cocina***")

nombre_receta = input("\nIngresa el nombre de la receta: ")
lista_ingredientes = input("\nIngresa los ingredientes de la receta separados por espacio: ").split()
tiempo_preparacion = int(input(f"\nIngresa el tiempo de preparación del plato en minutos: "))
dificultad_receta = input("\nIngresa la dificultad de la receta (Facil, Media, Difícil): ")

print(f"\n\n\nDatos de la receta \"{nombre_receta}\":\n")
print(f"Cuenta con los ingredientes: {lista_ingredientes}\n")
print(f"\nLleva un tiempo de preparación de: {tiempo_preparacion} minutos\n")
print(f"\nLa dificultad de la receta es: {dificultad_receta}\n")

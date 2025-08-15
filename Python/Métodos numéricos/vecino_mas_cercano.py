import numpy as np

# Matriz de distancias
# Cada entrada [i][j] representa la distancia de la ciudad i a la ciudad j
# Si no hay camino de i a j (o es la misma ciudad)
matriz_distancias = np.array([
    [np.inf, 10, 15, 20],
    [10, np.inf, 35, 25],
    [15, 35, np.inf, 30],
    [20, 25, 30, np.inf]
])

# Función para resolver con el método del vecino más cercano
def vecino_mas_cercano(distancias, ciudad_inicial=2):
    n_ciudades = len(distancias)                    # Total ciudades
    visitadas = [False] * n_ciudades                # Ciudades visitadas
    ruta = [ciudad_inicial]                         # Inicio ruta ciudad inicial
    visitadas[ciudad_inicial] = True                # Marcar como visitada

    ciudad_actual = ciudad_inicial
    distancia_total = 0                             # Acumulador de distancia total

    for _ in range(n_ciudades - 1):                 # Repetir hasta recorrer todas las ciudades o nodos
        # Ciudad más cercana no visitada
        distancia_minima = np.inf
        ciudad_mas_cercana = -1

        for ciudad in range(n_ciudades):
            if not visitadas[ciudad] and distancias[ciudad_actual][ciudad] < distancia_minima:
                distancia_minima = distancias[ciudad_actual][ciudad]
                ciudad_mas_cercana = ciudad

        # Agregamos la ciudad más cercana a la ruta
        ruta.append(ciudad_mas_cercana)
        visitadas[ciudad_mas_cercana] = True
        distancia_total += distancia_minima
        ciudad_actual = ciudad_mas_cercana

    # Regreso a ciudad origen para cerrar el ciclo
    distancia_total += distancias[ciudad_actual][ciudad_inicial]
    ruta.append(ciudad_inicial)

    return ruta, distancia_total




ruta_optima, distancia = vecino_mas_cercano(matriz_distancias, ciudad_inicial=2)

print("Ruta encontrada (orden de visita):", ruta_optima)
print("Distancia total del recorrido:", distancia)

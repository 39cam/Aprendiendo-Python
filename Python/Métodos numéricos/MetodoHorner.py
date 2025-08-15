def funcion(coef, x):
    """Evaluar un polinomio en x dado sus coeficientes."""
    res = coef[0]
    for c in coef[1:]:
        res = res * x + c
    return res

def horner(coeficientes, x0, tol=1e-12, max_iter=100):
    raices = []
    grado = len(coeficientes) - 1
    bloque = 1

    while grado > 0:
        x = x0
        iteracion = 0
        error = 1e9

        for _ in range(max_iter):
            iteracion += 1
            # Evaluar polinomio y derivada usando Horner
            b = [coeficientes[0]]
            for i in range(1, len(coeficientes)):
                b.append(coeficientes[i] + x * b[i - 1])
            fx = b[-1]

            # Derivada usando b (coeficientes deflactados)
            c = [b[0]]
            for i in range(1, len(b) - 1):
                c.append(b[i] + x * c[i - 1])
            dfx = c[-1]

            if abs(dfx) < 1e-14:
                break  # Evitar división por cero

            x_new = x - fx / dfx
            error = abs(x_new - x)
            x = x_new

            if error < tol:
                break

        raices.append(x)

        print(f"\n=== Raíz #{bloque} ===")
        print(f"Iteraciones: {iteracion}")
        print(f"Error final: {error}")
        print(f"Raíz encontrada: {x}")

        # Deflactar el polinomio (dividir entre (x - raíz))
        nuevos_coef = [coeficientes[0]]
        for i in range(1, len(coeficientes)-1):
            nuevos_coef.append(coeficientes[i] + x * nuevos_coef[i - 1])
        coeficientes = nuevos_coef
        grado -= 1
        bloque += 1

    print("\nNo quedan raíces por encontrar.")

def main():
    coef = [1, -5, 0, 5, -6]  # Polinomio: x^4 - 5x^3 + 0x^2 + 5x - 6
    horner(coef, x0=2.5)

main()

import cmath

def funcion(x):
    return x**4 - 5*x**3 + 5*x - 6

def bairstow(coeficientes, r, s, tol=1e-12, max_iter=100):
    n = len(coeficientes) - 1
    raices = []
    bloque = 1

    while n >= 3:
        iteracion = 0
        error = 1e9

        for _ in range(max_iter):
            iteracion += 1
            b = [0] * (n + 1)
            c = [0] * (n + 1)

            b[n] = coeficientes[n]
            b[n-1] = coeficientes[n-1] + r * b[n]

            for i in range(n-2, -1, -1):
                b[i] = coeficientes[i] + r * b[i+1] + s * b[i+2]

            c[n] = b[n]
            c[n-1] = b[n-1] + r * c[n]

            for i in range(n-2, -1, -1):
                c[i] = b[i+1] + r * c[i+1] + s * c[i+2]

            det = c[2]*c[2] - c[3]*c[1]
            if abs(det) < 1e-14:
                break

            dr = (-b[0]*c[2] + b[1]*c[1]) / det
            ds = (-b[1]*c[2] + b[0]*c[3]) / det

            r += dr
            s += ds

            error = abs(dr) + abs(ds)
            if error < tol:
                break

        discriminante = cmath.sqrt(r**2 - 4*s)
        raiz1 = (-r + discriminante) / 2
        raiz2 = (-r - discriminante) / 2
        raices.append((raiz1, raiz2))

        print(f"\n=== Raíces #{bloque} ===")
        print(f"Iteraciones: {iteracion}")
        print(f"Error final: {error}")
        print(f"Raíz 1: {raiz1}")
        print(f"Raíz 2: {raiz2}")

        bloque += 1
        coeficientes = b[2:]
        n = len(coeficientes) - 1

    if n == 2:
        a, b_, c_ = coeficientes
        discriminante = cmath.sqrt(b_**2 - 4*a*c_)
        raiz1 = (-b_ + discriminante) / (2*a)
        raiz2 = (-b_ - discriminante) / (2*a)
        print(f"\n=== Raíces finales (grado 2) ===")
        print(f"Raíz 1: {raiz1}")
        print(f"Raíz 2: {raiz2}")
    elif n == 1:
        a, b_ = coeficientes
        raiz = -b_ / a
        print(f"\n=== Raíz final (grado 1) ===")
        print(f"Raíz: {raiz}")
    elif n == 0:
        print("\nNo quedan raíces por encontrar.")

def main():
    coef = [1, -5, 0, 5, -6]  # x^4 - 5x^3 + 0x^2 + 5x - 6
    bairstow(coef, r=0.5, s=-1)

main()

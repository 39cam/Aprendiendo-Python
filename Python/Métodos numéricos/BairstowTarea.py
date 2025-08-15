from numpy.lib.scimath import sqrt


def bairstow(p, r_guess, s_guess):
    n = len(p) - 1
    if n < 2:
        return None, p

    b = [0] * len(p)
    c = [0] * len(p)
    r = r_guess
    s = s_guess
    e = 1e-12
    max_iter = 10000
    j = 0

    while j < max_iter:
        b[n] = p[n]
        b[n - 1] = p[n - 1] + r * b[n]
        for i in range(n - 2, -1, -1):
            b[i] = p[i] + r * b[i + 1] + s * b[i + 2]

        c[n] = b[n]
        c[n - 1] = b[n - 1] + r * c[n]
        for i in range(n - 2, -1, -1):
            c[i] = b[i] + r * c[i + 1] + s * c[i + 2]

        if len(c) < 4:
            break

        den = c[2] * c[2] - c[1] * c[3]
        if den == 0:
            break
        dr = (b[0] * c[3] - b[1] * c[2]) / den
        ds = (b[1] * c[1] - b[0] * c[2]) / den
        r += dr
        s += ds

        if abs(dr) < e and abs(ds) < e:
            break
        j += 1

    r1 = (r + sqrt(r ** 2 + 4 * s)) / 2
    r2 = (r - sqrt(r ** 2 + 4 * s)) / 2

    new_poly = b[2:] if len(b) > 2 else []

    return (r1, r2), new_poly


# Polinomio original: f(x) = x⁶ + 2x⁵ -6x⁴ -48x³ -9x² +93x -20
p = [1, 2, -6, -48, -9, 93, -20]

# Aplicar Bairstow hasta obtener 3 factores cuadráticos
factors = []
current_poly = p.copy()

for i in range(3):
    if len(current_poly) < 3:
        print("\nEl polinomio ya no puede factorizarse más en cuadráticos.")
        break

    initial_guesses = [
        (1.61, 6.22),  # Para -1.816 y 3.428
        (1.36, -0.26),  # Para 0.226 y 1.133
        (-1.6, 0.41)  # Para -1.816 y 0.226
    ]
    success = False

    for r_guess, s_guess in initial_guesses:
        roots, reduced_poly = bairstow(current_poly, r_guess, s_guess)
        if reduced_poly and len(reduced_poly) >= 1:
            factors.append((i + 1, roots, reduced_poly))
            current_poly = reduced_poly
            success = True
            break

    if not success:
        print("\nNo se pudo encontrar un factor cuadrático con los valores iniciales probados.")
        break

# Mostrar resultados de manera visual
print("\n" + "=" * 50)
print("RESULTADOS DE LA FACTORIZACIÓN CON BAIRSTOW")
print("=" * 50 + "\n")

for factor in factors:
    num, roots, reduced_poly = factor
    r1, r2 = roots

    print(f"FACTOR {num}:")
    print("-" * 40)
    print(f"Polinomio cuadrático encontrado:")
    print(f"x² - ({r1 + r2:.4f})x + ({r1 * r2:.4f})")
    print("\nRaíces del polinomio cuadrático:")
    print(f"x₁ = {r1:.4f}")
    print(f"x₂ = {r2:.4f}")
    print("\n" + "-" * 40 + "\n")

if len(current_poly) > 0 and len(current_poly) < 3:
    print("RESIDUO FINAL:")
    print("-" * 40)
    print(" + ".join([f"{coef:.4f}x^{i}" for i, coef in enumerate(current_poly[::-1])][::-1]))
    print("\n" + "=" * 50)

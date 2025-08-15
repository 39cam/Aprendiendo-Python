import cmath


def funcion(x):
    return x ** 4 - 5 * x ** 3 + 5 * x - 6


def muller(x0, x1, x2):
    n = 100
    ed = 1e-12
    e = 1
    i = 1
    f0 = f1 = f2 = 0

    while i <= n and e > ed:
        x2ant = x2

        f0 = funcion(x0)
        f1 = funcion(x1)
        f2 = funcion(x2)

        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (f1 - f0) / h0
        d1 = (f2 - f1) / h1
        a = (d1 - d0) / (h1 + h0)
        b = a * h1 + d1
        c = f2

        discriminante = cmath.sqrt(b ** 2 - 4 * a * c)
        if abs(b + discriminante) > abs(b - discriminante):
            den = b + discriminante
        else:
            den = b - discriminante

        if den == 0:
            print("División por cero en la iteración", i)
            break

        x3 = x2 - (2 * c) / den
        e = abs(x3 - x2)

        print(f'''Iteración #{i}
x0 = {x0}
x1 = {x1}
x2 = {x2}
f(x0) = {f0}
f(x1) = {f1}
f(x2) = {f2}
h0 = {h0}
h1 = {h1}
d0 = {d0}
d1 = {d1}
A = {a}
B = {b}
C = {c}
Error = {e}
''')

        x0, x1, x2 = x1, x2, x3
        i += 1

    print(f"Raíz aproximada encontrada: {x2}")


def main():
    muller(-3, -1, -2)

main()

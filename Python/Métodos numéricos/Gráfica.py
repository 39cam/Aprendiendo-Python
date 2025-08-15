import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**6 + 2*x**5 - 6*x**4 - 48*x**3 - 9*x**2 + 93*x - 20

x = np.linspace(-5, 5, 400)

y = f(x)

# Graficar
plt.plot(x, y, label='f(x)')
plt.axhline(0, color='black', linewidth=0.7)  # eje x
plt.axvline(0, color='black', linewidth=0.7)  # eje y
plt.title('Gráfica de f(x) = x^6 + 2x^5 - 6x^4 - 48x^3 - 9x^2 + 93x - 20')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

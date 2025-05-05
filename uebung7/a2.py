import numpy as np
import matplotlib.pyplot as plt

def f(x, y):        # Funktion von f
    return np.exp(-x**2) * np.sin(y)

x = np.linspace(-2, 2, 1000)  # start, ende, länge
y = np.linspace(0, 1 *2*np.pi, 1000)  # nur 1 Sinusperiode

X, Y = np.meshgrid(x, y)    # 2 arrays in 2D-Gitter darstellen
Z = f(X, Y)                 # Auswerten

plt.pcolormesh(X, Y, Z)
plt.show()

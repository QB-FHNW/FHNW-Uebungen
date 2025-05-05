import numpy as np
import matplotlib.pyplot as plt

amount = 1000
x = np.random.randint(-100, 100, amount)
y = np.random.randint(-100, 100, amount)

# print(x.astype(np.int64))
# print(y.astype(np.int64))

colours = ('b','g','r','c','m','y','k')

for i in range(amount):  # von 0 bis 999
    col = np.random.choice(colours)       # zufällige Farbe wählen
    plt.plot(x[i], y[i], f'{col}o')       # 'o' bedeutet Punkt, Buchstabe vor o gibt Farbe an z.B. grüner Punkt: 'go'

plt.axis([-100,100,-100,100])    # x-Achse (min bis max), y-Achse (min bis max) anzeigen
plt.xlabel('X-Achse')     
plt.ylabel('y-Achse')
plt.grid(True)

plt.show()
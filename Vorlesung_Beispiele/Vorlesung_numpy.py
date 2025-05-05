import numpy as np

a = np.array([1.2,4.4,6.8,7.7])         # array sind quasi Listen
print(a)
print('Datatype:', a.dtype)
print('\n')

b = np.array([1,4,6,7], dtype=np.float64)
print(b)
print('Datatype:', b.dtype)     # wird zu float konvertiert
print('\n')

c = a.astype(np.float64)
print(c)

print('Slicing:', a[0:2])     # Nur gewisse Ausschnitte ausgeben

print('\n')
# Mehrdimensionale arrays

d = np.array([[1,2,3], [4,5,6]], dtype = np.float64) # doppelte eckige klammer zur erkennung der mehreren arrays
print(d[0,2])       # Zeile 0, Spalte 2 (oder auch alle mit :)
print(d.shape)      # Matrix-Dimension

print('Is in: ', 5 in d)    # stimmt -> True.   100 wäre False

nulls = np.zeros((2,4))     # shape festlege
# nulls = np.ones((2,4))     # oder auch mit 1.
print(nulls)

print(np.random.random(7))      # Random (alles floats)
x = np.random.randint(1, 50, 5)  # 1: Untergrenze, 2: Obergrenze, 3: Anzahl Werte
print(x.astype(np.int64))
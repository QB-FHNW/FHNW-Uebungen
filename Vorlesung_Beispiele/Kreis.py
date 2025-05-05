import math

class Kreis:
    def __init__(self, mittelpunkt, radius):
        if radius <= 0:
            raise ValueError("Der Radius muss größer als 0 sein.")
        
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def umfang(self):
        return 2 * math.pi * self.radius

    def flaeche(self):
        return math.pi * self.radius**2

    def mittelpunkt(self):
        return self.mittelpunkt

k1 = Kreis((1, 2), 5)
print(k1.flaeche())
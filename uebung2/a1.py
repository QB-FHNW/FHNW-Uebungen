class Vector3:           
    def __init__(self, x=0, y=0,z=0):     # Standardwerte festlegen
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Der Vektor ist x: {str(self.x)}, y: {str(self.y)}, z: {str(self.z)}'
    
    def __add__(self, toBeAdded):
        return Vector3(self.x + toBeAdded.x, self.y + toBeAdded.y, self.z + toBeAdded.z)
    
    def __sub__(self, toBeSubed):
        return Vector3(self.x - toBeSubed.x, self.y - toBeSubed.y, self.z - toBeSubed.z)
    
    def __mul__(self, toBeMuled):
        if type(toBeMuled) == Vector3:
            return Vector3(self.x * toBeMuled.x, self.y * toBeMuled.y, self.z * toBeMuled.z)
        if type(toBeMuled) == float or type(toBeMuled) == int:
            return Vector3(self.x * toBeMuled.x, self.y * toBeMuled.y, self.z * toBeMuled.z)
        raise TypeError('Parameter has to be either type float, int or Vector3')

# Aufgabenstellung für Multiplikation mit Skalar definitv nicht verstanden.

    def dot(self, toBeDoted):
        if not type(toBeDoted) == Vector3:
            raise TypeError('Parameter has to be Vector3')
        return self.x * toBeDoted.x + self.y * toBeDoted.y + self.z * toBeDoted.z
    
    def cross(self, toBeCrossed):
        if not type(toBeCrossed) == Vector3:
            raise TypeError('Parameter has to be Vector3')
        return (
            self.y*toBeCrossed.z - self.z*toBeCrossed.y,
            self.z*toBeCrossed.x - self.x*toBeCrossed.z,
            self.x*toBeCrossed.y - self.y*toBeCrossed.x
            )
    
    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def normalize(self):
        mag = self.magnitude()
        return Vector3(
            self.x / mag,
            self.y / mag,
            self.z / mag
        )

a = Vector3(3,4,2)
b = Vector3(2,1,0)
c = a * b     # Komponentenweise Multiplikation
print(c)
d = a.dot(b) # Skalarprodukt
e = a.cross(b) # Kreuzprodukt
print(f'Skalarprodukt: {d}, Kreuzprodukt: {e}')
f = a.normalize() # f als normierter Vektor
print(f.magnitude()) # Betrag von Einheitsvektor muss 1 geben.
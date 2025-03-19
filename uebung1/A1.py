class Vector3:              # Klasse anlegen
    def __init__(self, x=0, y=0,z=0):     # standard Werte festlegen
        self.x = x
        self.y = y
        self.z = z
    
    def len(self):          # Vektor Länge
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
v = Vector3()               # Instanz anlegen
v.x = 3            
v.y = 4             
v.z = 0
print(v.len())
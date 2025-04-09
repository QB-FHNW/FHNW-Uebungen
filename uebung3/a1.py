import math
class Figur: 
    def __init__(self): 
        self.name = "Figur" 
    
    def Umfang(self): 
        return 0 
    
    def __str__(self): 
        return self.name
    
class Dreieck(Figur):
    def __init__(self, a,b,c):
        super().__init__()
        self.name = 'Dreieck'
        self.a = a
        self.b = b
        self.c = c

    def Umfang(self):
        return self.a+self.b+self.c
    
    def __str__(self):
        return self.name
    
class Rechteck(Figur):
    def __init__(self, a,b,c,d):
        super().__init__()
        self.name = 'Rechteck'
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def Umfang(self):
        return self.a+self.b+self.c+self.d
    
    def __str__(self):
        return self.name

class Kreis(Figur):
    def __init__(self, zentrum, radius):
        super().__init__()
        self.name = 'Kreis'
        self.zentrum = zentrum
        self.radius = radius
    
    def Umfang(self):
        return math.pi*self.radius*2
    
    def __str__(self):
        return self.name

class Polygon(Figur):
    def __init__(self):
        super().__init__()
    




print(Dreieck(2,3,4).name)
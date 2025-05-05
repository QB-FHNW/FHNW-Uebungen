class Ort:
    def __init__(self, name, koordinate, einwohnerzahl):
        self.name = name
        self.koordinate = koordinate
        self.einwohnerzahl = einwohnerzahl

    def __str__(self):
        return (f"{self.name} bei Koordinate {self.koordinate} hat {self.einwohnerzahl} Einwohner.")

    def __lt__(self, other):        
        return self.einwohnerzahl < other.einwohnerzahl

    def __gt__(self, other):        
        return self.einwohnerzahl > other.einwohnerzahl

    def __eq__(self, other):
        return self.einwohnerzahl == other.einwohnerzahl

Basel = Ort('Basel',(12000,26000),15)
Züri = Ort('Zürich',(2000,6000),20)

if Basel < Züri:
    print('jabadubadu')
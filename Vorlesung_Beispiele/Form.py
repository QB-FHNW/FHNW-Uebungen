class Form:
    def flaeche(self):
        raise NotImplementedError("Diese Methode kann zur Zeit nicht ausgeführt werden.")


class Rechteck(Form):
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

    def flaeche(self):
        return self.laenge * self.breite

r1 = Rechteck(4,2)
print(r1.flaeche())
class Tankstelle(benzinpreis,land,koordinate):
    def __init__(self, name):
        self.name = name
        self.benzinpreis = benzinpreis   # Standardwert: 0.0
        self.land = land           # Standardwert: leerer String
        self.koordinate = koordinate  # Standardkoordinate (Breite, Länge)

    def __str__(self):
        return (f"Tankstelle: {self.name}\n"
                f"Benzinpreis: {self.benzinpreis} €/L\n"
                f"Land: {self.land}\n"
                f"Koordinate: {self.koordinate}")

# Tankstelle erstellen
tanke = Tankstelle("Shell")

# Werte setzen
tanke.benzinpreis = 1.79

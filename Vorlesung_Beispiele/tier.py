# Basisklasse
class Tier:
    def __init__(self, name):
        self.name = name

    def sprich(self):
        return "Ein Geräusch"

# Abgeleitete Klasse Hund
class Hund(Tier):
    def sprich(self):
        return f"{self.name} sagt: Wuff!"

# Abgeleitete Klasse Katze
class Katze(Tier):
    def sprich(self):
        return f"{self.name} sagt: Miau!"

# Nutzung der Klassen
tiere = [Hund("Bello"), Katze("Miez"), Tier("Unbekannt")]

for tier in tiere:
    print(tier.sprich())


import sys
import urllib.parse
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

class LinkOpener(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Link oeffner")

        # Button
        self.button = QPushButton("Auf Karte zeigen")
        self.button.clicked.connect(self.link_oeffnen)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def link_oeffnen(self):
        adresse = "Hofackerstrasse 30 4132 Muttenz Schweiz"
        query = urllib.parse.quote(adresse)
        url = QUrl(f"https://www.google.ch/maps/place/{query}")
        QDesktopServices.openUrl(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenster = LinkOpener()
    fenster.show()
    sys.exit(app.exec_())
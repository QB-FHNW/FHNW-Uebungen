class Temperature:
    def __init__(self, c=0):
        self.celsius = c
    
    def __gt__(self, other):
        return self.celsius > other.celsius

t1 = Temperature(40)
t2 = Temperature(30)

if t1 > t2:
    print('check1')
if t2 > t1:
    print('check2')

import sys
from PyQt5.QtWidgets import *

# Fenster-Klasse: wird von QWindow vererbt
class MyWindow(QMainWindow):
    def __init__(self): # Konstruktor
        super().__init__() # Konstruktor Basis-Klasse
        self.setWindowTitle("Hello World") # Fenster-Titel setzen
        self.show() # Fenster anzeigen/sichtbar machen
    
def main():
    app = QApplication(sys.argv) # Qt Applikation erstellen
    mainwindow = MyWindow() # Instanz Fenster erstellen
    app.exec() # Applikations-Loop starten

if __name__ == '__main__':
    main()
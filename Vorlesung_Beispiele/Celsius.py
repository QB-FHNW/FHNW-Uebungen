import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Konverter")

        layout = QVBoxLayout()

        # Celsius-Eingabe horizontal anordnen
        celsius_layout = QHBoxLayout()

        self.celsius_label = QLabel("Celsius:")
        self.celsius_label.setFont(QFont("Arial", 16))
        celsius_layout.addWidget(self.celsius_label)

        self.celsius_input = QDoubleSpinBox()
        self.celsius_input.setFont(QFont("Arial", 16))
        self.celsius_input.setRange(-273.15, 1000)
        self.celsius_input.setDecimals(2)
        self.celsius_input.setValue(0.0)
        celsius_layout.addWidget(self.celsius_input)

        layout.addLayout(celsius_layout)


        # Ergebnisanzeige
        self.result_label = QLabel("Wert in Fahrenheit: 32.0")
        self.result_label.setFont(QFont("Arial", 12))
        layout.addWidget(self.result_label)

        # Layout setzen
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

        # Verbindung
        self.celsius_input.valueChanged.connect(self.update_result)

        self.show()

    def update_result(self):
        c = self.celsius_input.value()
        f = c * 1.8 + 32
        self.result_label.setText(f"Wert in Fahrenheit: {f:.1f}")

def main():
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

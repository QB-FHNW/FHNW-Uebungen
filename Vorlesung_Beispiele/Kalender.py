import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

    def createLayout(self):
        
        self.setWindowTitle("Mein Kalender")
        
        layout = QFormLayout()
        self.setMinimumSize(800,200)  



        menubar = self.menuBar()
        filemenu = menubar.addMenu("Programm")
        
        schliessen = QAction("schliessen",self)

        schliessen.triggered.connect(self.menu_schliessen)

        filemenu.addAction(schliessen)



        
        self.button1 = QPushButton("Speichern")
        self.button2 = QPushButton("Abbrechen")




        self.titel = QLabel("Titel des Anlasses:")
        self.titelline = QLineEdit()
        self.checkbox = QCheckBox("ganzer Tag")
        self.checkbox.setCheckState(Qt.CheckState.Checked)
        self.calendar = QCalendarWidget()

        layout.addWidget(self.titel)
        layout.addWidget(self.titelline)
        layout.addWidget(self.calendar)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        

      

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)


        self.show()



    def menu_speichern(self):
        datum = self.calendar.selectedDate().toString("yyyy-MM-dd")
        titel = self.titelline.text()
        if self.checkbox.isChecked():
            checkbox_text = "(Ganztägig)"
        else:
            checkbox_text = " "

        zeile = f"{datum} - {titel} {checkbox_text}\n"

        with open("output.txt","a",encoding="utf-8") as datei:
            datei.write(zeile)
        print("Daten gespeichert in txt File")



    def menu_schliessen(self):
        self.close()


    def createConnects(self):
        self.button1.clicked.connect(self.menu_speichern)
        self.button2.clicked.connect(self.menu_schliessen)



def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()      
    mainwindow.raise_()          
    app.exec()                  
 
if __name__ == '__main__':
    main()
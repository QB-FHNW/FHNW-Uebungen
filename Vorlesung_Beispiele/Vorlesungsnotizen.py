import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
 
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()
       
    def createLayout(self):
        self.setWindowTitle("Demo")
        layout = QVBoxLayout()
 
        self.button = QPushButton("Button 1")
        self.lineedit = QLineEdit()
        self.checkbox = QCheckBox("Check")
        self.checkbox.setCheckState(Qt.CheckState.Checked)
 
        self.radio1 = QRadioButton("Radio 1")
        self.radio2 = QRadioButton("Radio 2")
 
        self.calender = QCalendarWidget()
 
        self.combobox = QComboBox()
        self.combobox.addItems(["Eins", "Zwei", "Drei"])
 
        layout.addWidget(self.button)
        layout.addWidget(self.lineedit)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.calender)
        layout.addWidget(self.combobox)
 
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
 
        self.show()
 
    def createConnects(self):
        self.button.clicked.connect(self.button_clicked)
        self.lineedit.textChanged.connect(self.lineedit_update)
        self.checkbox.stateChanged.connect(self.check_boxchanged)
        self.radio1.toggled.connect(self.radio1_toggled)
        self.radio2.toggled.connect(self.radio2_toggled)
        self.calender.clicked.connect(self.calender_clicked)
        self.combobox.currentIndexChanged.connect(self.combobox_indexchanged)
 
    def button_clicked(self):
        print("button clicked")
 
    def lineedit_update(self, txt):
        print('Test changed', txt)
 
    def check_boxchanged(self, state):
        if state == Qt.CheckState.Checked:
            print('Checkbox is checked')
        elif state == Qt.CheckState.Unchecked:
            print('Checkbox is unchecked')
 
    def radio1_toggled(self, checked):
        print('Radio1', checked)
 
    def radio2_toggled(self, checked):
        print('Radio2', checked)
 
    def calender_clicked(self, date):
        print(date)
 
    def combobox_indexchanged(self, index):
        print(index)
       
 
 
 
def main():
    app = QApplication(sys.argv)  
    mainwindow = MyWindow()      
    mainwindow.raise_()          
    app.exec_()                  
 
if __name__ == '__main__':
    main()
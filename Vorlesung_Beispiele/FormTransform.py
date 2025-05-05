import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
 
 
 
 
class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r"C:\Users\quiri\Documents\GitHub\Qt-Designer/untitled.ui", self)
 
        self.show()
 
def main():
    app = QApplication(sys.argv)  
    mainwindow = MyWindow()      
    mainwindow.raise_()          
    app.exec_()                  
 
if __name__ == '__main__':
    main()
 
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# Qt Deginer로 만든 ui를 적용하는 법
form_class = uic.loadUiType("myMainWindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
import sys, random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QMouseEvent
from PyQt5.QtCore import Qt



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)


app = QApplication(sys.argv)
w = MyWidget()
sys.exit(app.exec_())
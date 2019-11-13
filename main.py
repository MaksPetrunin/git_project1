import sys, random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QMouseEvent



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.show()

    def run(self):
        a = random.randint(10, 200)
        self.paint = QPainter()
        self.paint.begin(self)
        self.paint.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.paint.drawEllipse(400, 300, a, a)
        self.paint.end()


app = QApplication(sys.argv)
w = MyWidget()
sys.exit(app.exec_())
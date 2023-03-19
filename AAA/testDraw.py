import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QFrame
from ui.draw import Ui_Form
from testsad import testWin

class mainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.layoutMain = QVBoxLayout()
        self.btn = QPushButton('test')
        self.btn.clicked.connect(self.reset)
        self.testWidget = testWin()
        self.drawForm = QFrame()
        self.layoutMain.addWidget(self.btn)
        self.layoutMain.addWidget(self.testWidget)
        self.show()


        self.setLayout(self.layoutMain)

    def reset(self):
        self.testWidget.setVisible(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mainWin()
    win.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox
from ui.draw import Ui_Form


class testWin(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(lambda: self.setVisible(True))
        self.pushButton.clicked.connect(lambda: self.setVisible(False))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = testWin()
    ex.show()
    sys.exit(app.exec_())

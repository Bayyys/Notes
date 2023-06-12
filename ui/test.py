from cgi import test
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QColor, QOpenGLVersionProfile
from MyGLWidget_ui import Ui_MyGLWidget


class MainWindow(QMainWindow, Ui_MyGLWidget):
    def __init__(self):
        super().__init__()#super()构造器方法返回父级的对象。
        # self.ui = loadUi("MyGLWidget_ui.ui")  # 加载ui
        self.setupUi(self)
 
 
app = QApplication(sys.argv)
w = MainWindow()
w.ui.show()
sys.exit(app.exec())
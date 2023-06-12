import sys
sys.path.append('../..')
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
# QApplication
from PyQt5.QtWidgets import QApplication
from ui.setting_ui.setting_ui import Ui_Setting

class SettingWidget(QWidget, Ui_Setting):
    def __init__(self, mainWin=None) -> None:
        super().__init__()
        self.mainWin = mainWin
        uic.loadUi('ui/setting_ui/setting_ui.ui', self)
        # self.setupUi(self)
        self.initUI()
        self.setWindowTitle('设置')
    
    def initUI(self):
        self.reset.clicked.connect(self.mainWin.setting)
        self.sleep.clicked.connect(self.mainWin.setting)
        self.algorithm.clicked.connect(self.mainWin.setting)
        self.direction.clicked.connect(self.mainWin.setting)
        self.angle_0.clicked.connect(self.mainWin.setting)
        self.z_0.clicked.connect(self.mainWin.setting)
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = SettingWidget()
    widget.show()
    sys.exit(app.exec_())
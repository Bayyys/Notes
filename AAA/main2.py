import sys
from PyQt5.QtWidgets import QWidget, QComboBox, QPushButton, QLabel, QFrame, QHBoxLayout, QVBoxLayout, QTextEdit, QApplication, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtChart import QChartView, QValueAxis, QChart, QSplineSeries
# 串口操作
import utils.serialUtil as serUtil
from PyQt5.QtGui import QPainter
from PyQt5 import uic
# 全局变量
# connected: 连接状态
# ser: 串口对象
import utils.globalParams as glo
from PyQt5.QtChart import QChart
from ui.chartView import Ui_chartViewForm
from ui.chart import Ui_chartForm



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.chart1 = Ui_chartViewForm()
        self.chart1.setupUi(self)
        self.chart2 = Ui_chartViewForm()
        self.chart2.setupUi(self)
        self.initUI()
    
    def initUI(self):
        # self.chartView = QChartView(self.chart.chart)
        layoutMain = QVBoxLayout()
        frame1 = QFrame()
        self.chart1.pushButton.setText('chart1')
        layout = self.chart1.horizontalLayout
        frame1.setLayout(layout)
        frame2 = QFrame()
        self.chart2.pushButton.setText('chart2')
        layout = self.chart2.horizontalLayout
        frame2.setLayout(layout)
        layoutMain.addWidget(frame1)
        layoutMain.addWidget(frame2)
        self.setLayout(layoutMain)
        box = QComboBox()
        box.addItem('1')
        box.addItem('2')
        box.currentIndexChanged
        layout.set
        ...
    
    def start_clicked(self):
        print('start_clicked')

if __name__ == '__main__':
    glo.__init__()
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
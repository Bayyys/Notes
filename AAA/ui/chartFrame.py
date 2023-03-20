from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFrame, QCheckBox
from PyQt5.QtCore import Qt, QTimer, QCoreApplication
from scipy.signal import butter, filtfilt
import time
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
sys.path.append("..") # 将上级目录加入到搜索路径中
import utils.globalParams as glo
from draw import Ui_Form
from drawFrame import drawFrame


class MyMplCanvas(FigureCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self):
        global xdata, ydata
        self.fig, self.ax = plt.subplots()
        ymax = 200000
        self.ax.set_ylim(-ymax, ymax)
        self.ax.set_xlim(0, 2000)
        self.ax.set_axis_off()
        self.line, = self.ax.plot([], [])
        FigureCanvas.__init__(self, self.fig)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(1)  # 更新时间间隔为1ms

    def update_figure(self):
        # if glo.connected:
        self.draw()
        # print(time.time())
        ...

class chartFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initData()
    
    def initUI(self):
        # self.canvas = MyMplCanvas()
        self.chartWidget = drawFrame()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.chartWidget)
        # self.chartWidget.canvasLayout.addWidget(self.canvas)
        self.setLayout(self.layout)
    
    def initData(self):
        global xdata, ydata
        xdata = np.arange(0, 2000, 1)
        ydata = np.zeros(2000)
        self.canvas.line.set_data(xdata, ydata)


    def checkBoxClicked(self):
        if self.checkBox.isChecked() == False:
            self.setVisible(False)
            self.checkBox.setChecked(True)
    
    def addData(self, data):
        global xdata, ydata
        len_data = len(data)
        ydata[:-len_data] = ydata[len_data:]
        ydata[-len_data:] = data

        self.canvas.line.set_data(xdata, ydata)

    
    def keyPressEvent(self, e) -> None:
        if e.key() == Qt.Key_Enter:
            self.chart.zoomReset()


if __name__ == '__main__':
    global xdata, ydata
    glo.__init__()
    app = QApplication(sys.argv)
    w = chartFrame()
    w.show()
    app.exec_()

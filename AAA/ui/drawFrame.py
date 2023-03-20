import sys
sys.path.append("..")  # 将上级目录加入到搜索路径中
import utils.globalParams as glo
from ui.draw import Ui_Form
import threading
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFrame, QCheckBox
from PyQt5.QtCore import Qt, QTimer, QCoreApplication
from scipy.signal import butter, filtfilt
import numpy as np
import matplotlib.pyplot as plt



class MyMplCanvas(FigureCanvas):
    """A canvas that updates itself every second with a new plot."""
    
    XMAX = 2000
    XMAX_FLAG = False
    xdis = 2000
    ymax = 200000
    xdata = np.array([])
    ydata = np.array([])


    def __init__(self):
        super().__init__()
        self.initChart()
        self.initData()
        self.initUpdataTimer()
        self.setFocusPolicy(Qt.ClickFocus)
        self.setFocus()

    def initChart(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_ylim(-self.ymax, self.ymax)
        self.ax.set_xlim(0, self.xdis)
        self.ax.set_axis_off()
        self.ax.grid(True)
        # self.ax.set_xmargin(0)
        # self.ax.set_ymargin(0)
        self.ax.get_xaxis().set_visible(True)
        # self.ax.get_yaxis().set_visible(False)
        self.line, = self.ax.plot([], [])
        FigureCanvas.__init__(self, self.fig)

        self.fig.set_constrained_layout_pads(
            w_pad=0, h_pad=0, wspace=0, hspace=0)
        self.fig.set_constrained_layout(True)

        self.fig.canvas.mpl_connect('scroll_event', self.button_call_back)
        self.fig.canvas.mpl_connect(
            'button_press_event', self.button_call_back)
        self.fig.canvas.mpl_connect('key_press_event', self.button_call_back)

    def initData(self):
        # self.xdata = np.arange(0, self.xdis, 1)
        # self.ydata = np.arange(0, self.xdis, 1)
        self.line.set_data(self.xdata, self.ydata)
        self.draw()

    def initUpdataTimer(self):
        # threading.Thread(target=self.update_figure).start()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(1)  # 更新时间间隔为1ms

    def update_figure(self):    # 定时更新图像 (1ms)
        # while True:
        # self.draw()
        if glo.connected:
            # self.line.set_ydata(self.ydata)
            # self.ax.cla() #每次循环画图前先清空当前坐标轴，包括 Line2D 对象
            # self.ax.plot(self.xdata, self.ydata, 'o-', c='b') #画图
            # self.fig.canvas.draw_idle()
            # self.fig.canvas.flush_events()
            # self.ax.cla()
            self.draw()
        # print(time.time())
        ...

    def button_call_back(self, event): # 鼠标滚轮事件
        axtemp = event.inaxes
        y_min, y_max = axtemp.get_ylim()
        y_dis = (y_max - y_min) / 10
        x_min, x_max = axtemp.get_xlim()
        x_dis = (x_max - x_min) / 10
        x_mouse = event.xdata
        y_mouse = event.ydata
        x_test = (x_max - x_min) / 2
        y_test = (y_max - y_min) / 2
        # if event.button == 'up':
        #     xmin_new = x_mouse - x_test + x_dis if x_mouse - x_test + x_dis > 0 else 0
        #     xmax_new = x_mouse + x_test - x_dis if x_mouse + x_test - x_dis < self.XMAX else self.XMAX
        #     if xmin_new >= xmax_new:
        #         xmin_new = xmax_new - x_test
        #     ymin_new = y_mouse - y_test + y_dis if y_mouse - y_test + y_dis > -20000 else -20000
        #     ymax_new = y_mouse + y_test - y_dis if y_mouse + y_test - y_dis < 20000 else 20000
        #     if ymin_new >= ymax_new:
        #         ymin_new = ymax_new - y_test
        #     axtemp.set(xlim=(xmin_new, xmax_new), ylim=(ymin_new, ymax_new))
        # if event.button == 'down':
        #     xmin_new = x_mouse - x_test - x_dis if x_mouse - x_test - x_dis > 0 else 0
        #     xmax_new = x_mouse + x_test + x_dis if x_mouse + x_test + x_dis < self.XMAX else self.XMAX
        #     if xmin_new >= xmax_new:
        #         xmin_new = xmax_new - x_test
        #     ymin_new = y_mouse - y_test - y_dis if y_mouse - y_test - y_dis > -20000 else -20000
        #     ymax_new = y_mouse + y_test + y_dis if y_mouse + y_test + y_dis < 20000 else 20000
        #     if ymin_new >= ymax_new:
        #         ymin_new = ymax_new - y_test
        #     axtemp.set(xlim=(xmin_new, xmax_new), ylim=(ymin_new, ymax_new))

        if event.button == 'up' and event.key == 'shift':
            axtemp.set(xlim=(x_min + x_dis, x_max - x_dis))
            print('right')
        elif event.button == 'up':
            axtemp.set(ylim=(y_min + y_dis, y_max - y_dis))
            print('up')
        if event.button == 'down' and event.key == 'shift':
            axtemp.set(xlim=(x_min - x_dis, x_max + x_dis))
            print('left')
        elif event.button == 'down':
            axtemp.set(ylim=(y_min - y_dis, y_max + y_dis))
            print('down')
        self.draw()
    
    def zoomReset(self):
        self.ax.set_xlim(0, self.xdis)
        self.ax.set_ylim(-self.ymax, self.ymax)
        self.fig.canvas.draw_idle()

class drawFrame(QFrame, Ui_Form):
    history = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        # self.initData()

    def initUI(self):
        self.canvas = MyMplCanvas()
        self.canvasLayout.addWidget(self.canvas)
        self.btn_reset.clicked.connect(self.btn_reset_clicked)
        # self.btn_close.clicked.connect(lambda: self.setVisible(False))
        # self.btn_close.clicked.connect(self.dataTimer)
        ...

    def btn_reset_clicked(self):    # 重置按钮
        self.canvas.zoomReset()
    
    def addData(self, data):    # 添加数据
        self.history += data
        if len(self.history) > self.canvas.XMAX:
            self.history = self.history[-self.canvas.XMAX:]
        data = self.BandFilter(self.HighPassFilter(data))[-len(data):]
        if len(self.canvas.xdata) == 0:
            print("add")
            self.canvas.xdata = np.arange(0, len(data), 1)
            self.canvas.ydata = np.array(data)
        else:
            if self.canvas.XMAX_FLAG == False:
                if len(self.canvas.xdata) + len(data) <= self.canvas.XMAX:
                    self.canvas.xdata = np.arange(0, len(self.canvas.xdata) + len(data), 1)
                    self.canvas.ydata = np.append(self.canvas.ydata, data)
                else:
                    self.canvas.xdata = np.arange(0, self.canvas.XMAX, 1)
                    self.canvas.ydata = np.append(self.canvas.ydata, data)
                    self.canvas.ydata = self.canvas.ydata[-self.canvas.XMAX:]
                    self.canvas.XMAX_FLAG = True
            else:
                self.canvas.ydata = np.append(self.canvas.ydata, data)
                self.canvas.ydata = self.canvas.ydata[-self.canvas.XMAX:]

        # len_data = len(data)
        # self.canvas.ydata = np.append(self.canvas.ydata, data)
        # len_data = len(self.canvas.ydata)
        # self.canvas.xdata = np.arange(0, len_data, 1)
        # print("length:", len(self.canvas.xdata), len(self.canvas.ydata))
        # self.canvas.line.set_data(self.canvas.xdata, self.canvas.ydata)
        # self.canvas.ydata[:-len_data] = self.canvas.ydata[len_data:]
        # self.canvas.ydata[-len_data:] = data
        self.canvas.line.set_data(self.canvas.xdata, self.canvas.ydata)
        
    def updateYlim(self, ymax):
        self.canvas.ax.set_ylim(-ymax, ymax)
        self.canvas.fig.canvas.draw_idle()

    def updateXlim(self, xmax):
        self.canvas.ax.set_xlim(self.canvas.XMAX - xmax, self.canvas.XMAX)
        self.canvas.fig.canvas.draw_idle()
    
    def HighPassFilter(self, data):
        # 高通滤波
        sampleRate = 1000
        filterParam = 1
        nyquistFreq = 0.5 * sampleRate
        cutoffFreq = filterParam
        b, a = butter(8, cutoffFreq/nyquistFreq, 'highpass')
        if len(data) > 3*max(len(a), len(b)):
            data = filtfilt(b, a, data)
        return data
        ...
    
    def BandFilter(self, data):
        # 带通滤波
        sampleRate = 1000
        nyquistFreq = 0.5 * sampleRate
        passbandFreq = 1
        stopbandFreq = 50
        b, a = butter(8, [passbandFreq/nyquistFreq,
                        stopbandFreq/nyquistFreq], 'bandpass')
        if len(data) > 3*max(len(a), len(b)):
            data = filtfilt(b, a, data)
        return data
    # def dataTimer(self):    # 定时器
    #     self.list = np.arange(0, 10, 1)
    #     self.mytimer = QTimer()
    #     self.mytimer.timeout.connect(self.add)
    #     self.mytimer.start(100)
    #     ...
    
    # def add(self):  # 添加数据
    #     self.list = np.arange(max(self.list) + 1, max(self.list) + 10, 1)
    #     self.addData(self.list)

    def keyPressEvent(self, e) -> None:
        if e.key() == Qt.Key_Enter:
            self.chart.zoomReset()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = drawFrame()
    ex.show()
    sys.exit(app.exec_())

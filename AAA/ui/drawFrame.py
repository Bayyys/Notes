import matplotlib.animation as animation
import sys
sys.path.append("..")  # 将上级目录加入到搜索路径中
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt, cheby1, cheby2, sosfilt, detrend
from PyQt5.QtCore import Qt, QTimer, QCoreApplication, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFrame, QCheckBox
from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import threading
from ui.draw import Ui_Form
import utils.globalParams as glo


class MyMplCanvas(FigureCanvas):
    """A canvas that updates itself every second with a new plot."""

    XMAX = 5000
    Xdis = 1000
    Ydis = 20000
    xdata = np.array([])
    ydata = np.array([])

    def __init__(self):
        super().__init__()
        self.initChart()
        self.initData()
        # self.initUpdataTimer()
        self.setFocusPolicy(Qt.ClickFocus)
        self.setFocus()

    def initChart(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_ylim(-self.Ydis, self.Ydis)
        self.ax.set_xlim(self.XMAX - self.Xdis, self.XMAX)
        # self.ax.set_xticklabels([])  # 去掉x轴刻度
        # self.ax.set_yticklabels([])  # 去掉y轴刻度
        # self.ax.set_xticks([])  # 去掉x轴刻度
        # self.ax.set_autoscalex_on(False)    # 关闭自动缩放
        # self.ax.set_yticks([])  # 去掉y轴刻度
        # self.ax.set_autoscaley_on(False)    # 关闭自动缩放
        # self.ax.set_axes_locator(None)  # 去掉坐标轴
        # self.ax.set_axis_off()
        # self.ax.grid(True)
        # self.ax.set_xmargin(0)
        # self.ax.set_ymargin(0)
        # self.ax.get_xaxis().set_visible(False)
        # self.ax.get_yaxis().set_visible(False)
        self.ax.set_ylabel('Voltage (μV)')
        self.ax.set_xlabel('Time (s)')
        self.line, = self.ax.plot([], [])
        FigureCanvas.__init__(self, self.fig)

        # self.fig.set_constrained_layout_pads(w_pad=0, h_pad=0, wspace=0, hspace=0)   # 自动调整子图间距
        self.fig.set_constrained_layout(True)   # 自动调整子图间距

        self.fig.canvas.mpl_connect('scroll_event', self.button_call_back)
        self.fig.canvas.mpl_connect(
            'button_press_event', self.button_call_back)
        self.fig.canvas.mpl_connect('key_press_event', self.button_call_back)

    def initData(self):
        self.xdata = np.arange(0, self.XMAX, 1)
        self.ydata = np.zeros(self.XMAX)
        self.line.set_data(self.xdata, self.ydata)
        self.draw()

    def initUpdataTimer(self):  # 定时更新图像 xxx
        # threading.Thread(target=self.update_figure).start()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(1)  # 更新时间间隔为1ms
        # self.mythread = drawThread(self)
        # self.mythread.start()
        # ani = animation.FuncAnimation(self.fig, self.update_figure, interval=1)

    def update_figure(self):    # 定时更新图像 (1ms)    xxx
        # time1 = time.time()
        # while True:
        # self.draw()
        # while True:
        if glo.connected:
            # print(time.time())
            # self.line.set_ydata(self.ydata)
            # self.line.set_ydata(self.ydata)
            # self.ax.cla() #每次循环画图前先清空当前坐标轴，包括 Line2D 对象
            # self.ax.plot(self.xdata, self.ydata, 'o-', c='b') #画图
            # self.fig.canvas.draw_idle()
            # self.fig.canvas.flush_events()
            # self.ax.cla()
            self.draw()
            self.flush_events()
        # print("use time:", time.time() - time1)
        # print(time.time())
        ...

    def button_call_back(self, event):  # 鼠标滚轮事件
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
        self.ax.set_xlim(0, glo.XDIS)
        self.ax.set_ylim(-glo.YDIS, glo.YDIS)
        self.fig.canvas.draw_idle()

    def close_event(self, event) -> None:
        try:
            self.timer.stop()
            # self.mythread.stop()
            self.mythread.terminate()
        except:
            ...

class drawFrame(QFrame, Ui_Form):
    # history = []
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        try:
            self.ui = uic.loadUi('ui/draw.ui', self)
        except:
            self.ui = uic.loadUi('draw.ui', self)
        self.initUI()
        # ani = animation(self.canvas.fig, self.test, interval = 50)
        # self.initData()

    def initUI(self):
        self.canvas = MyMplCanvas()
        self.time = 0
        self.canvasLayout.addWidget(self.canvas)
        self.btn_reset.clicked.connect(lambda: self.canvas.zoomReset())
        self.btn_close.clicked.connect(lambda: self.setVisible(False))
        # self.canvas2 = MyMplCanvas2()
        # self.frame1Layout.addWidget(self.canvas2)
        # self.canvas3 = MyMplCanvas2()
        # self.frame2Layout.addWidget(self.canvas3)
        # self.frame1.layout.addWidget(self.canvas2)
        # self.btn_close.clicked.connect(lambda: self.setVisible(False))
        # self.btn_close.clicked.connect(self.dataTimer)
        ...

    def addData(self, data):    # 添加数据
        len_data = len(data)

        # if glo.isHighPassFilter:
        #     data = self.HighPassFilter(data)
        # if glo.isBandFilter:
        #     data = self.BandFilter(data)
        # if glo.isNotchFilter:
        #     data = self.NotchFilter(data)
        # # time1 = time.time()
        # self.history += data
        # if len(self.history) > self.canvas.XMAX:
        #     self.history = self.history[-self.canvas.XMAX:]

        # # data = self.BandFilter(self.HighPassFilter(data))[-len(data):]

        # if len(self.canvas.xdata) == 0:
        #     print("add")
        #     self.canvas.xdata = np.arange(0, len(data), 1)
        #     self.canvas.ydata = np.array(data)
        # else:
        #     if self.canvas.XMAX_FLAG == False:
        #         if len(self.canvas.xdata) + len(data) <= self.canvas.XMAX:
        #             self.canvas.xdata = np.arange(0, len(self.canvas.xdata) + len(data), 1)
        #             self.canvas.ydata = np.append(self.canvas.ydata, data)
        #         else:
        #             self.canvas.xdata = np.arange(0, self.canvas.XMAX, 1)
        #             self.canvas.ydata = np.append(self.canvas.ydata, data)
        #             self.canvas.ydata = self.canvas.ydata[-self.canvas.XMAX:]
        #             self.canvas.XMAX_FLAG = True
        #     else:
        #         self.canvas.ydata = np.append(self.canvas.ydata, data)
        #         self.canvas.ydata = self.canvas.ydata[-self.canvas.XMAX:]
        # self.canvas.line.set_data(self.canvas.xdata, self.canvas.ydata)

        # self.canvas.ydata = np.append(self.canvas.ydata, data)
        # len_data = len(self.canvas.ydata)
        # self.canvas.xdata = np.arange(0, len_data, 1)
        # print("length:", len(self.canvas.xdata), len(self.canvas.ydata))
        self.canvas.ydata[:-len_data] = self.canvas.ydata[len_data:]
        self.canvas.ydata[-len_data:] = data
        self.canvas.line.set_ydata(self.canvas.ydata)
        # drawThread(self.canvas.fig.canvas).start()
        # time2 = time.time()
        # print("filter time: ", time2 - time1, "len(data): ", len(data))
        # self.time += time2 - time1

    def updateYlim(self):   # 更新Y轴范围
        self.canvas.ax.set_ylim(-glo.YDIS, glo.YDIS)
        self.canvas.fig.canvas.draw_idle()

    def updateXlim(self):  # 更新X轴范围
        self.canvas.ax.set_xlim(self.canvas.XMAX - glo.XDIS, self.canvas.XMAX)
        self.canvas.fig.canvas.draw_idle()

    def HighPassFilter(self, data): # 高通滤波
        # 高通滤波
        sampleRate = 8000
        cutoffFreq = 1
        ripple = 1
        N = 8
        sos = cheby2(N=N, rs=ripple,
                     Wn=cutoffFreq,
                     btype='highpass', fs=sampleRate,
                     analog=False, output='sos')
        data = sosfilt(sos, data)
        return data
        ...

    def NotchFilter(self, data):    # 陷波滤波
        # 陷波滤波
        sampleRate = 8000
        cutoffFreq = 50
        filterParam = 10
        ripple = 1
        N = 8
        sos = cheby2(N=N, rs=ripple,
                     Wn=[cutoffFreq - filterParam, cutoffFreq + filterParam],
                     btype='bandstop', fs=sampleRate,
                     analog=False, output='sos')
        data = sosfilt(sos, data)
        return data

    def BandFilter(self, data): #   带通滤波
        # 带通滤波
        sampleRate = 8000
        passbandFreq = 1
        stopbandFreq = 50
        ripple = 1
        N = 8
        sos = cheby2(N=N, rs=ripple,
                     Wn=[passbandFreq, stopbandFreq],
                     btype='bandpass', fs=sampleRate,
                     analog=False, output='sos')
        data = sosfilt(sos, data)
        return data

    def dataTimer(self):    # 定时器    xxx
        self.list = np.arange(0, 10, 1)
        self.mytimer = QTimer()
        self.mytimer.timeout.connect(self.add)
        # self.mytimer.start(10)
        ...
    
    def test(self):
        self.canvas.ax.set_ylim(-glo.YDIS, glo.YDIS)

    def add(self):  # 添加数据  xxx
        max = np.max(self.canvas.ydata)
        min = np.min(self.canvas.ydata)
        rms = np.sqrt(np.mean(self.canvas.ydata ** 2))
        # self.list = np.arange(max(self.list) + 1, max(self.list) + 10, 1)
        # self.addData(self.list)
        self.lb_min = min
        self.lb_max = max
        self.lb_rms = rms

    def keyPressEvent(self, e) -> None: # 键盘事件
        if e.key() == Qt.Key_Enter:
            self.chart.zoomReset()
    
    def closeEvent(self, event=None) -> None:   # 关闭事件
        # self.canvas.close_event()
        # self.canvas.mythread.terminate()
        ...

if __name__ == '__main__':
    data_o = np.loadtxt("txt.txt")
    data1 = data_o[::2]
    # for i in range(0, len(data1)):
        # data1[:i+1] = data1[:i+1] - np.mean(data2[:i+1])

    data3 = detrend(data1)
    # plt.plot(np.arange(0, len(data3) / 8000, 1 / 8000), data3)
    # plt.show()

    app = QApplication(sys.argv)
    ex = drawFrame()
    data2 = ex.HighPassFilter(data3)
    # plt.plot(np.arange(0, len(data2) / 8000, 1 / 8000), data2)
    # plt.show()
    data = ex.NotchFilter(data2)
    # plt.plot(np.arange(0, len(data) / 8000, 1 / 8000), data)
    # plt.show()
    data = ex.BandFilter(data)
    # plt.plot(np.arange(0, len(data) / 8000, 1 / 8000), data)
    # plt.show()
    data = data[2000:]
    ex.canvas.ydata = data
    ymax = np.max(data)
    ymin = np.min(data)
    ex.canvas.xdata = np.arange(0, len(data) / 8000, 1 / 8000)
    ex.canvas.line.set_data(ex.canvas.xdata, ex.canvas.ydata)
    ex.canvas.ax.set_xlim(0, np.max(ex.canvas.xdata) + 1)
    ex.canvas.ax.set_ylim(ymin, ymax)
    ex.canvas.draw()
    print(data[-100:])
    ex.show()
    sys.exit(app.exec_())
    ...
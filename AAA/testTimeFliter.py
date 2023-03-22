import sys
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFrame
from PyQt5.QtCore import Qt, QTimer
from scipy.signal import butter, filtfilt, cheby1, cheby2, sosfilt
import time


class MyMplCanvas(FigureCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self):
        global isCollecting
        self.fig, self.ax = plt.subplots()
        self.ax.set_ylim(-100, 100)
        self.ax.set_xlim(0, 8000)
        self.line, = self.ax.plot([], [])
        FigureCanvas.__init__(self, self.fig)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(1)  # 更新时间间隔为50ms

    def update_figure(self):
        if isCollecting:
        #     self.line.set_data(xdata, ydata)
            # print(len(xdata))
            self.draw()
            # print(time.time())
        ...


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        global isCollecting
        self.xdata = []
        self.ydata = []
        self.sampleRate = 0
        self.b = 0
        self.a = 0
        self.sos = []

    def initUI(self):
        
        self.setWindowTitle('Realtime EMG Monitor')
        self.setGeometry(50, 50, 1000, 800)

        # 频率输入框
        self.freq_label = QLabel('采样率（Hz）', self)
        self.freq_label.move(10, 10)
        self.freq_line = QLineEdit('8000', self)
        self.freq_line.setGeometry(100, 10, 80, 20)
        self.freq_line.setAlignment(Qt.AlignCenter)

        # 滤波类型下拉框
        self.filter_label = QLabel('滤波类型', self)
        self.filter_label.move(200, 10)
        self.filter_box = QComboBox(self)
        self.filter_box.setGeometry(280, 10, 80, 20)
        self.filter_box.addItems(['低通滤波', '带通滤波', '高通滤波', '陷波滤波'])

        # 滤波参数输入框
        self.filter_param_label = QLabel('滤波参数', self)
        self.filter_param_label.move(370, 10)
        self.filter_param_line = QLineEdit('50', self)
        self.filter_param_line.setGeometry(450, 10, 80, 20)
        self.filter_param_line.setAlignment(Qt.AlignCenter)

        # 开始按钮
        self.start_button = QPushButton('开始采集', self)
        self.start_button.setGeometry(540, 10, 80, 20)
        self.start_button.clicked.connect(self.start_button_clicked)

        # 退出按钮
        self.quit_button = QPushButton('退出', self)
        self.quit_button.setGeometry(630, 10, 80, 20)
        self.quit_button.clicked.connect(self.quit_button_clicked)

        # 实时绘图部分
        self.plot_widget = QWidget(self)
        self.plot_widget.setGeometry(10, 40, 980, 750)
        self.plot_widget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.plot_layout = QVBoxLayout(self.plot_widget)
        self.plot_layout.setContentsMargins(0, 0, 0, 0)
        self.mpl_canvas = MyMplCanvas()
        self.plot_layout.addWidget(self.mpl_canvas)
        self.plot_widget.setFocus()
        self.layoutMain = QVBoxLayout(self)
        self.layoutTest = QHBoxLayout(self)
        self.layoutTest.addWidget(self.freq_label)
        self.layoutTest.addWidget(self.freq_line)
        self.layoutTest.addWidget(self.filter_label)
        self.layoutTest.addWidget(self.filter_box)
        self.layoutTest.addWidget(self.filter_param_label)
        self.layoutTest.addWidget(self.filter_param_line)
        self.layoutTest.addWidget(self.start_button)
        self.layoutTest.addWidget(self.quit_button)
        self.frameTop = QFrame()
        self.frameTop.setLayout(self.layoutTest)
        self.layoutMain.addWidget(self.frameTop)
        self.layoutMain.addWidget(self.plot_widget)
        self.FrameTest = QFrame()
        self.FrameTest.setLayout(self.layoutMain)
        self.setCentralWidget(self.FrameTest)


    def start_button_clicked(self):
        global isCollecting

        # 判断是否已经在采集状态中
        if isCollecting:
            return

        # 获取采样率和滤波参数
        sampleRate = int(self.freq_line.text())
        sampleRate = 8000
        filterParam = int(self.filter_param_line.text())    # 滤波参数

        # 计算滤波系数
        nyquistFreq = 0.5 * sampleRate  # 奈奎斯特频率
        if self.filter_box.currentText() == '低通滤波':
            cutoffFreq = filterParam
            self.sos = cheby2(8, 1, 1, 'lowpass', fs=sampleRate, output='sos')
            self.b, self.a = butter(4, cutoffFreq/nyquistFreq, 'lowpass')
        elif self.filter_box.currentText() == '带通滤波':
            passbandFreq = filterParam
            stopbandFreq = filterParam + 10
            self.sos = cheby2(8, 1,
                              [passbandFreq/nyquistFreq,    # 带通滤波器的通带频率
                        stopbandFreq/nyquistFreq],  # 带通滤波器的截止频率
                        btype='bandpass', fs=sampleRate, output='sos')
            self.b, self.a = butter(4, [passbandFreq/nyquistFreq,
                        stopbandFreq/nyquistFreq], 'bandpass')
        elif self.filter_box.currentText() == '高通滤波':
            cutoffFreq = filterParam
            self.sos = cheby2(8, 1, 100, 'highpass', fs=sampleRate, output='sos')
            self.b, self.a = butter(4, cutoffFreq/nyquistFreq, 'highpass')
        
        elif self.filter_box.currentText() == '陷波滤波':
            passbandFreq = filterParam
            stopbandFreq = filterParam + 10
            self.sos = cheby2(8, 1, [passbandFreq/nyquistFreq,
                        stopbandFreq/nyquistFreq], btype='bandstop', fs=sampleRate, output='sos')
            self.b, self.a = butter(4, [passbandFreq/nyquistFreq,
                        stopbandFreq/nyquistFreq], 'bandstop')

        # 初始化数据
        isCollecting = True
        self.xdata = np.arange(8000)
        self.ydata = np.zeros(8000)

        # 开始采集
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.collect_data)
        self.timer.start(1/sampleRate)
        print('开始采集', 1/sampleRate)


    def collect_data(self):
        # 逐点采集数据
        newData = random.randint(-100, 100)  # 模拟采集到的数据
        # print(newData)
        self.ydata[:-1] = self.ydata[1:]
        self.ydata[-1] = newData

        time1 = time.time()
        # 滤波处理
        if len(self.ydata) > max(len(self.a), len(self.b)):
            # print(len(ydata), len(a), len(b))
            new = sosfilt(self.sos, self.ydata)[-1]
            self.ydata = np.append(self.ydata[1:], new)
        # 更新绘图
        # print(newData)
        # print(new)
        self.mpl_canvas.line.set_data(self.xdata, self.ydata)
        # self.mpl_canvas.draw()
        # print(time.time())
        # print(len(ydata))


    def quit_button_clicked(self):
        global isCollecting
        global xdata
        global ydata
        global sampleRate
        global b, a

        # 停止采集
        isCollecting = False
        # self.timer.stop()

        # 退出应用
        # QApplication.quit()

if __name__ == '__main__':
    global isCollecting
    global xdata
    global ydata
    global sampleRate
    global b, a
    isCollecting = False
    xdata = np.zeros(1)
    ydata = np.zeros(1)
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

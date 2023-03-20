import threading
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFrame, QCheckBox
from PyQt5.QtCore import Qt, QTimer, QCoreApplication
from scipy.signal import butter, filtfilt
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append("..")  # 将上级目录加入到搜索路径中
from ui.draw import Ui_Form
import utils.globalParams as glo


class MyMplCanvas(FigureCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self):
        self.initChart()
        self.initUpdataTimer()
        self.setFocusPolicy( Qt.ClickFocus )
        self.setFocus()
        
    
    def initChart(self):
        self.xdis = 5000
        self.fig, self.ax = plt.subplots()
        self.ymax = 200000
        self.ax.set_ylim(-self.ymax, self.ymax)
        self.ax.set_xlim(0, self.xdis)
        self.ax.set_axis_off()
        # self.ax.set_xmargin(0)
        # self.ax.set_ymargin(0)
        self.ax.get_xaxis().set_visible(True)
        # self.ax.get_yaxis().set_visible(False)
        self.line, = self.ax.plot([], [])
        FigureCanvas.__init__(self, self.fig)
        self.xdata = np.arange(0, self.xdis, 1)
        self.ydata = np.zeros(self.xdis)
        self.line.set_data(self.xdata, self.ydata)
        self.fig.set_constrained_layout_pads(
            w_pad=0, h_pad=0, wspace=0, hspace=0)
        self.fig.set_constrained_layout(True)

        self.fig.canvas.mpl_connect('scroll_event', self.call_back)
        self.fig.canvas.mpl_connect('button_press_event', self.call_back)
        self.fig.canvas.mpl_connect('key_press_event', self.call_back)
    
    def initUpdataTimer(self):
        # threading.Thread(target=self.update_figure).start()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start()  # 更新时间间隔为1ms

    def update_figure(self):    # 定时更新图像 (1ms)
        # while True:
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

    def call_back(self, event): # 鼠标滚轮事件
        axtemp = event.inaxes
        y_min, y_max = axtemp.get_ylim()
        y_dis = (y_max - y_min) / 10
        x_min, x_max = axtemp.get_xlim()
        x_dis = (x_max - x_min) / 10
        # if event.button == 'up' and event.key == 'shift':
        #     axtemp.set(ylim=(y_min + y_dis, y_max - y_dis))
        #     print('up')
        # # elif event.button == 'down':
        # #     axtemp.set(ylim=(y_min - y_dis, y_max + y_dis))
        # #     print('down')
        # if event.dblclick == True and event.button == 3:
        #     axtemp.set(xlim=(x_min - x_dis, x_max + x_dis))
        #     print('left')
        if event.key == 'shift':
            if event.button == 1:
                axtemp.set(xlim=(x_min + x_dis, x_max - x_dis))
                print('right')
        # self.fig.canvas.draw_idle()  # 绘图动作实时反映在图像上

    def zoomReset(self):
        self.ax.set_xlim(0, self.xdis)
        self.ax.set_ylim(-self.ymax, self.ymax)
        self.fig.canvas.draw_idle()

class drawFrame(QFrame, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        # self.initData()

    def initUI(self):
        self.canvas = MyMplCanvas()
        self.canvasLayout.addWidget(self.canvas)
        self.btn_reset.clicked.connect(self.btn_reset_clicked)
        self.btn_close.clicked.connect(lambda: self.setVisible(False))
        ...

    def btn_reset_clicked(self):    # 重置按钮
        self.canvas.zoomReset()
    
    def addData(self, data):    # 添加数据
        len_data = len(data)
        # self.canvas.ydata = np.append(self.canvas.ydata, data)
        # len_data = len(self.canvas.ydata)
        # self.canvas.xdata = np.arange(0, len_data, 1)
        # print("length:", len(self.canvas.xdata), len(self.canvas.ydata))
        # self.canvas.line.set_data(self.canvas.xdata, self.canvas.ydata)
        self.canvas.ydata[:-len_data] = self.canvas.ydata[len_data:]
        self.canvas.ydata[-len_data:] = data
        self.canvas.line.set_ydata(self.canvas.ydata)
        

    def keyPressEvent(self, e) -> None:
        if e.key() == Qt.Key_Enter:
            self.chart.zoomReset()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = drawFrame()
    ex.show()
    sys.exit(app.exec_())

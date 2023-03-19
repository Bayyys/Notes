import sys
import serial
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter
from PyQt5.QtChart import QChart, QChartView, QLineSeries

# 设置串口参数
COM_PORT = 'COM3'
BAUD_RATE = 460800


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("Real-time EMG Plot")
        self.setGeometry(100, 100, 800, 600)

        # 创建一个 QChart 对象
        self.chart = QChart()
        self.chart.setTitle("Real-time EMG Plot")
        self.chart.legend().hide()

        # 创建一个 QLineSeries 对象，用于存储和显示 EMG 数据
        self.series = QLineSeries()
        self.chart.addSeries(self.series)

        # 设置 X 轴和 Y 轴范围
        # self.axis_x = self.chart.createDefaultAxis()
        self.axis_x.setRange(0, 1000)
        # self.axis_y = self.chart.createDefaultAxis()
        self.axis_y.setRange(-128, 128)

        # 创建一个 QChartView 对象，并将 QChart 对象传递给它
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # 将 QChartView 添加到主窗口中
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.chart_view)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

        # 创建一个 QTimer 对象，定时读取串口数据并更新 QLineSeries
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(10)

        # 打开串口
        self.serial_port = serial.Serial(COM_PORT, BAUD_RATE)

    def update_chart(self):
        # 读取串口数据
        data = self.serial_port.read(64)

        # 将数据转换为整数列表
        data = [int(x) for x in data]

        # 更新 QLineSeries 中的数据
        self.series.clear()
        for i in range(len(data)):
            self.series.append(i, data[i])

        # 重新绘制图表
        self.chart.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

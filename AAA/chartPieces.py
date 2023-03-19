import sys
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtGui import QPainter


class DataThread(QThread):
    dataReceived = pyqtSignal(list)  # 自定义信号，用于将数据发送给主线程

    def __init__(self, parent=None):
        super().__init__(parent)
        self.port = "COM3"  # 串口号
        self.baudrate = 4608000  # 波特率

    def run(self):
        # 在此处实现数据读取的代码
        # 读取到的数据保存在 data 中
        while True:
            data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 示例数据
            self.dataReceived.emit(data)  # 发送数据给主线程


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-time Plotting")
        self.resize(800, 600)

        # 创建图表和线性序列
        self.chart = QChart()
        self.series = QLineSeries()
        self.chart.addSeries(self.series)

        # 创建图表视图并设置大小策略
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setMinimumSize(640, 480)

        # 创建布局和窗口，并将图表视图添加到布局中
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        layout.addWidget(self.chart_view)
        self.setCentralWidget(widget)

        # 创建数据线程并连接信号
        self.dataThread = DataThread()
        self.dataThread.dataReceived.connect(self.plotData)
        self.dataThread.start()

    def plotData(self, data):
        # 将收到的数据添加到序列中
        for i, d in enumerate(data):
            self.series.append(i, d)
        # 设置图表视图的 X 轴范围
        self.chart_view.chart().axisX().setRange(0, len(data) - 1)
        # 重绘图表视图
        self.chart_view.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

import sys
import matplotlib
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("Matplotlib in PyQt5")
        self.setGeometry(100, 100, 800, 600)

        # 创建 Matplotlib 图形对象
        self.figure = Figure()  # 创建一个 Figure，注意：该 Figure 是 matplotlib.backend_bases.FigureCanvasBase 的子类
        self.canvas = FigureCanvas(self.figure) # FigureCanvas：其实就是一个 QWidget（默认绘图区背景为白色）
        self.setCentralWidget(self.canvas)

        # 在图形窗口中绘图
        self.axes = self.figure.add_subplot(111)
        self.axes.plot([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5])
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

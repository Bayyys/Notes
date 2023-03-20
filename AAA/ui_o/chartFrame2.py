from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QPolygon, QPixmap
from PyQt5.QtCore import Qt, QPointF, QThread, pyqtSignal, QPoint
import sys
import numpy as np
from  time import sleep


class myThread(QThread):
    sig = pyqtSignal(int)

    def __init__(self, parent=None):
        super(myThread, self).__init__(parent)
        self.data = 0

    def run(self):
        while True:
            self.data = (self.data + 1) % 100
            self.sig.emit(self.data)
            self.sleep(1)


class RealtimePlot(QWidget):
    def __init__(self):
        super().__init__()
        self.maxY = 100
        self.X = 0
        self.initUI()
        self.mythread = myThread()
        self.mythread.sig.connect(self.hasDataToDraw)
        self.mythread.start()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.previous_point = QPoint(0, 50)
        self.setWindowTitle('Realtime Plot')
        self.xdata = np.arange(0, self.width(), 0.01)
        self.ydata = np.arange(0, self.width(), 0.01)
        print(len(self.xdata))
        print(len(self.ydata))
        self.pix = QPixmap(self.width(), self.height())
        self.pix.fill(Qt.white)
        

    def paintEvent(self, event):
        # self.qp = QPainter(self)
        # self.pen = QPen(Qt.red)
        # self.pen.setWidth(2)
        # self.qp.setPen(self.pen)
        qp = QPainter(self.pix)
        for i in range(1, len(self.xdata) - 1):
            qp.drawLine(self.xdata[i-1], self.ydata[i-1],
                        self.xdata[i], self.ydata[i])

    def hasDataToDraw(self, data):
        qb = QPainter(self.pix)
        frameHeight = self.height()
        y_perScale = 2 * self.maxY / frameHeight
        self.X = (self.X + 1) % 100
        y_point = QPoint(self.X, frameHeight - data / y_perScale)
        points = QPolygon([self.previous_point, y_point])
        qb.drawPolyline(points)
        self.previous_point = y_point

    def add_point(self, x, y):
        self.data.append((x, y))

        if len(self.data) > 50:
            self.data.pop(0)

        self.update()

    def clear_screen(self):
        self.data = []
        self.update()

    def closeEvent(self, event) -> None:
        self.mythread.terminate()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RealtimePlot()
    ex.show()
    sys.exit(app.exec_())

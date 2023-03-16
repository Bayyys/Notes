
import sys
from PyQt5.QtCore import Qt, QTimer, QRandomGenerator
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView,QSplineSeries, QValueAxis
 
class MyChart(QChart):
    def __init__(self, parent = None):
        super(MyChart, self).__init__(parent)
        
        self.series = None
        self.axisX = QValueAxis()
        self.axisY = QValueAxis()
        self.step = 0
        self.x = 5
        self.y = 1
        
        #创建一个定时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimeout)
        self.timer.setInterval(500)
        
        self.series = QSplineSeries(self)
        redPen = QPen(Qt.red)
        redPen.setWidth(3)
        self.series.setPen(redPen)
        self.series.append(self.x, self.y)
        
        self.addSeries(self.series)
        
        self.addAxis(self.axisX, Qt.AlignBottom)
        self.addAxis(self.axisY, Qt.AlignLeft)
        self.series.attachAxis(self.axisX)
        self.series.attachAxis(self.axisY)
        self.axisX.setTickCount(5)
        self.axisX.setRange(0, 10)
        self.axisY.setRange(-5, 10)
        
        self.timer.start()
        
    def handleTimeout(self):
        x = self.plotArea().width() / self.axisX.tickCount()
        y = (self.axisX.max() - self.axisX.min()) / self.axisX.tickCount()
        self.x += y
        self.y = QRandomGenerator.global_().bounded(5) - 2.5
        self.series.append(self.x, self.y)
        self.scroll(x, 0)
        print(x)
        print(self.plotArea().width() , ' ', self.axisX.tickCount())
        if self.x == 100:
            self.timer.stop()
        
 
class DemoDynamicSpline(QMainWindow):
    def __init__(self, parent=None):
        super(DemoDynamicSpline, self).__init__(parent)   
        
         # 设置窗口标题
        self.setWindowTitle('实战 Qt for Python: 动态样条曲线演示')      
        # 设置窗口大小
        self.resize(480, 360)
        
        self.createChart()
    
    def createChart(self):
        chart = MyChart()
        chart.setTitle('动态样条曲线')
        chart.legend().hide()
        chart.setAnimationOptions(QChart.AllAnimations)
        
        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chartView)
      
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoDynamicSpline()
    window.show()
    sys.exit(app.exec()) 

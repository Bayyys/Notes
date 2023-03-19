import sys
import math
from PyQt5.QtCore import Qt,QMargins
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog
from QCustomPlot2 import *  #先导入PyQt5,不然报错
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QCheckBox
from PyQt5.QtChart import QChartView, QChart, QSplineSeries, QValueAxis
from PyQt5.QtCore import Qt, QMargins
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QPointF
import sys

# app = QApplication(sys.argv)
# window = QMainWindow()
# window.resize(800, 600)

# customPlot = QCustomPlot()  #相当于pyqt5的一个控件
# layout = QVBoxLayout()
# layout.addWidget(customPlot)
# window.setCentralWidget(customPlot)

# customPlot.addGraph() #添加一个曲线图QGraph

# x=[]
# y=[]

# for i in range(101):
#     x.append(i/50.0-1)
#     y.append(x[i]**2)

# customPlot.graph(0).setData(x,y) #为曲线图添加数据
# customPlot.graph(0).setName("第一个示例") #设置曲线图的名字

# customPlot.xAxis.setLabel("x") #设置x轴的标签
# customPlot.yAxis.setLabel("y")

# customPlot.xAxis.setRange(-1,1) #设置x轴的范围为(-1,1)
# customPlot.yAxis.setRange(0,1)

# # customPlot.axisRect().setAutoMargins(QCP.msNone) #坐标轴到边界的距离，设置为0

# customPlot.legend.setVisible(True) #显示图例


# customPlot.replot()

# window.show()
# sys.exit(app.exec_())

class testWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        btn = QPushButton("1")
        btn.clicked.connect(self.btnClicked)
        layout.addWidget(btn)
        self.chartView = QChartView()
        self.chart = QChart()
        self.chart.setMargins(QMargins(0, 0, 0, 0))
        self.chart.setBackgroundRoundness(0)    # 设置背景圆角
        
        self.series = QSplineSeries()
        self.chart.addSeries(self.series)

        self.dataAxisX = QValueAxis()
        self.dataAxisX.setMax(0)
        self.dataAxisX.setTickCount(11)
        self.dataAxisX.setMinorTickCount(3)
        self.dataAxisX.setRange(0, 1000)

        self.valueAxisY = QValueAxis()
        self.valueRange = 10
        self.valueAxisY.setRange(0, self.valueRange * 1.1)
        self.valueAxisY.setLabelFormat('%.1f')
        self.valueAxisY.setTickCount(6)
        self.valueAxisY.setMinorTickCount(2)

        self.chart.addAxis(self.dataAxisX, Qt.AlignBottom)
        self.chart.addAxis(self.valueAxisY, Qt.AlignLeft)
        self.chart.legend().hide()
        # self.chart.setAnimationOptions(QChart.SeriesAnimations)    # 设置动画：chart中启用了所有动画类型。
        self.chart.setAnimationOptions(
            QChart.NoAnimation)    # 设置动画：chart中启用了所有动画类型。
        # self.chart.createDefaultAxes()  # 创建默认轴 可用在加载数据时使用

        self.series.attachAxis(self.dataAxisX)
        self.series.attachAxis(self.valueAxisY)
        self.chartView.setChart(self.chart)
        # self.ChartView.setRenderHint(QPainter.Antialiasing)   # 抗锯齿
        self.chartView.setRubberBand(QChartView.RectangleRubberBand)    # 框选 

        layout.addWidget(self.chartView)

        self.setLayout(layout)
    def btnClicked(self):
        # dirpath, type  = QFileDialog.getSaveFileName(self,
        #                                              caption='保存文件', directory='date', filter='CSV(*.csv) ;; 纯文本(*.txt)', initialFilter='CSV(*.csv)')
        # print(dirpath)
        # print(type)
        self.run()
    
    def run(self):
        x = 1;
        y = 1;
        while True:
            self.series.append(x, y)
            QApplication.processEvents()
            print(x, y)
            x = (x + 1) % 1000
            y = (y + 1) % 10


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = testWin()
    win.show()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QCheckBox
from PyQt5.QtChart import QChartView, QChart, QSplineSeries, QValueAxis
from PyQt5.QtCore import Qt, QMargins
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QPointF
import sys


class chartFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.initChart()
        self.ChartView.setChart(self.chart)
        self.setLayout(self.horizontalLayout)
        self.ChartView.setRenderHint(QPainter.Antialiasing)   # 抗锯齿
        self.ChartView.setRubberBand(QChartView.RectangleRubberBand)    # 可框选 
        
    def setupUi(self):
        self.horizontalLayout = QHBoxLayout()
        self.checkBox = QCheckBox()
        self.checkBox.setText("")
        self.checkBox.setChecked(True)
        self.checkBox.stateChanged.connect(self.checkBoxClicked)
        self.ChartView = QChartView()
        self.horizontalLayout.addWidget(self.checkBox)
        self.horizontalLayout.addWidget(self.ChartView)

    def initChart(self):
        self.chart = QChart()
        self.chart.setMargins(QMargins(0, 0, 0, 0))
        self.chart.setBackgroundRoundness(0)    # 设置背景圆角

        self.series = QSplineSeries()
        # self.series.useOpenGL()   # 使用OpenGL加速
        self.chart.addSeries(self.series)

        self.dataAxisX = QValueAxis()
        self.dataAxisX.setMax(0)
        self.dataAxisX.setTickCount(6)
        self.dataAxisX.setMinorTickCount(3)
        self.dataAxisX.setRange(0, 1)

        self.valueAxisY = QValueAxis()
        self.valueRange = 200000
        self.valueAxisY.setRange(-(self.valueRange * 1.1),
                                 self.valueRange * 1.1)
        self.valueAxisY.setLabelFormat('%.1f')
        self.valueAxisY.setTickCount(6)
        self.valueAxisY.setMinorTickCount(2)
        self.valueAxisY.setVisible(False)

        self.chart.addAxis(self.dataAxisX, Qt.AlignBottom)
        self.chart.addAxis(self.valueAxisY, Qt.AlignLeft)
        self.chart.legend().hide()
        # self.chart.setAnimationOptions(QChart.SeriesAnimations)    # 设置动画：chart中启用了所有动画类型
        self.chart.setAnimationOptions(QChart.NoAnimation)    # 设置动画：chart中不启用动画
        # self.chart.createDefaultAxes()  # 创建默认轴 可用在加载数据时使用

        self.series.attachAxis(self.dataAxisX)
        self.series.attachAxis(self.valueAxisY)

    def checkBoxClicked(self):
        if self.checkBox.isChecked() == False:
            self.setVisible(False)
            self.checkBox.setChecked(True)
    
    def keyPressEvent(self, e) -> None:
        if e.key() == Qt.Key_Enter:
            self.chart.zoomReset()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = chartFrame()
    w.show()
    sys.exit(app.exec_())
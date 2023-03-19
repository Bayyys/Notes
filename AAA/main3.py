import sys
from PyQt5.QtWidgets import QWidget, QComboBox, QPushButton, QLabel, QFrame, QHBoxLayout, QVBoxLayout, QTextEdit, QApplication, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtChart import QChartView, QValueAxis, QChart, QSplineSeries
# 串口操作
import utils.serialUtil as serUtil
from PyQt5.QtGui import QPainter
from PyQt5 import uic
# 全局变量
# connected: 连接状态
# ser: 串口对象
import utils.globalParams as glo
from ui.mainWindow import Ui_MainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.ui = uic.loadUi('ui/mainWindow.ui', self)
        self.initUI()

    def initUI(self):
        # 参数设置部分
        self.searchCom()
        # 按钮部分
        self.btn_start.clicked.connect(self.start_clicked)
        self.btn_stop.clicked.connect(self.stop_clicked)
        # 信息显示部分
        self.lb_info.setText('信息显示')
        self.et_text.setText('设置参数信息并点击开始按钮进行测量')
        # 图表显示部分
        self.chartInit()
        self.layoutChart.addWidget(self.Chart)
        # self.scrollArea.addWidget(self.frameChart)

    def chartInit(self):
        self.Chart = QChartView()
        self.Chart.setMinimumHeight(300)
        self.chart = QChart()

        self.series = QSplineSeries()
        self.chart.addSeries(self.series)
        self.dataAxisX = QValueAxis()
        self.dataAxisX.setMax(0)
        self.dataAxisX.setTickCount(11)
        self.dataAxisX.setMinorTickCount(3)
        self.dataAxisX.setRange(-10, 0)

        self.valueAxisY = QValueAxis()
        self.valueRange = 50
        self.valueAxisY.setRange(-(self.valueRange * 1.1), self.valueRange * 1.1)
        self.valueAxisY.setLabelFormat('%.4f')
        self.valueAxisY.setTickCount(6)
        self.valueAxisY.setMinorTickCount(2)
        self.chart.addAxis(self.dataAxisX, Qt.AlignBottom)
        self.chart.addAxis(self.valueAxisY, Qt.AlignLeft)
        self.chart.legend().hide()
        # self.chart.setAnimationOptions(QChart.SeriesAnimations)    # 设置动画：chart中启用了所有动画类型。
        # self.chart.createDefaultAxes()  # 创建默认轴 可用在加载数据时使用
        self.Chart.setRenderHint(QPainter.Antialiasing)   # 抗锯齿
        # self.Chart.isTouching = False
        self.Chart.setChart(self.chart)
        self.Chart.setRubberBand(QChartView.RectangleRubberBand)    
        self.series.attachAxis(self.dataAxisX)
        self.series.attachAxis(self.valueAxisY)

    def searchCom(self):    # 启动更新串口号线程
        self.getComThread = serUtil.getCom()
        self.getComThread.comUpdate.connect(self.updateCom)
        self.getComThread.start()
    
    def updateCom(self, port_list): # 更新串口号
        self.box_com.clear()
        if len(port_list) == 0:
            return
        self.box_com.addItems([port_list[i][0] + ' ' + port_list[i][1] for i in range(len(port_list))])
        self.box_com.setCurrentIndex(0)

    def start_clicked(self):    # 开始按钮点击事件
        if glo.connected:   # 当前已经连接, 避免重复连接
            print("已连接, 无需重复连接")
            return
        # 连接串口
        glo.set_ser(serUtil.serialOpen(self.box_com.currentText().split(' ')[0],    # 串口号
                            self.box_bps.currentText(),  # 波特率
                            self.box_timex.currentText()))   # 超时时间
        if glo.ser.isOpen():    # 连接成功
            self.connSuccess()
            self.connSeialThread()
            self.connChartTimer()

        else:   # 连接失败
            glo.set_connected(False)
            glo.ser.close()
            self.lb_info.setText('连接失败')

    def connSuccess(self):  # 连接成功
        glo.set_connected(True)  # 设置连接状态
        print("等待执行:", glo.ser.isOpen())    # 打印连接状态
        self.btn_stop.setEnabled(True)  # 开启停止按钮
        self.lb_info.setText('等待输入数据')
        self.et_text.setText('等待输入数据...')
    
    def connSeialThread(self):  # 连接串口读取线程
        self.serialRead = serUtil.serialRead()  # 串口读取线程
        self.serialRead.dateReadUpdate.connect(self.updateData)   # 信号连接: 串口读取数据 -> 更新数据
        self.serialRead.dateReadUpdate.connect(self.updateEt)   # 信号连接: 串口读取数据 -> 更新文本框
        self.serialRead.serDisconnect.connect(self.stop_clicked)    # 信号连接: 串口断开 -> 停止按钮点击事件
        self.serialRead.start() # 开启串口读取线程
    
    def connChartTimer(self):   # 连接图表定时器
        self.updateChartTimer = QTimer()    # 更新图表定时器
        self.updateChartTimer.timeout.connect(self.updateChart)    # 信号连接: 定时器 -> 更新图表
        self.updateChartTimer.start(0.00001)

    def updateEt(self, str_list):   # 更新文本框
        self.et_text.append(str_list)
        self.et_text.moveCursor(self.et_text.textCursor().End)
        ...

    def updateData(self, str_list):   # 更新本次数据(串口读取数据)
        glo.add_history(str_list)
    
    def updateChart(self):  # 更新图表
        # 更新折线上的点的坐标
        if glo.dataNotEmpty():
            y_list = glo.get_data()
            
            for i in range(len(y_list)):
                # self.chart.scroll(self.chart.plotArea().width() / 50000, 0)
                x = glo.get_time() * 0.001
                if i % 20 == 0:
                    y = float(y_list[i])
                    self.dataAxisX.setMin(x - 10)
                    self.dataAxisX.setMax(x)
                    # self.chart.createDefaultAxes()  # 重新创建坐标轴 # TODO
                    self.series.append(x, y)
                    QApplication.processEvents()
                    print("当前点数:", int(x * 1000))
                    print("总点数：" , len(glo.history))
                    
                    # self.chart.scroll(1, 0)
    
    def stop_clicked(self): # 停止按钮点击事件: 关闭串口、停止线程
        serUtil.serialClose(glo.ser)
        self.btn_stop.setEnabled(False)

    def keyPressEvent(self, e): # 重写键盘事件: 按下ESC键关闭串口
        if e.key() == Qt.Key_Escape:
            if glo.connected:
                self.stop_clicked()
        elif e.key() == Qt.Key_R:
            if ~glo.connected:
                self.start_clicked()
        if e.key() == Qt.Key_Plus:
            self.chart.zoomIn()
        elif e.key() == Qt.Key_Minus:
            self.chart.zoomOut()
        elif e.key() == Qt.Key_Return:
            # self.chart.scroll(-1000, 0)
            self.chart.zoomReset()
        elif e.key() == Qt.Key_Right:
            self.chart.scroll(1000, 0)
        elif e.key() == Qt.Key_Up:
            self.chart.scroll(0, 1000)
        elif e.key() == Qt.Key_Down:
            self.chart.scroll(0, -1000)

if __name__ == '__main__':
    glo.__init__()
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
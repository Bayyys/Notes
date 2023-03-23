import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5 import uic
# 串口操作
import utils.serialUtil as serUtil
# 全局变量
# connected: 连接状态
# ser: 串口对象
import utils.globalParams as glo
# 自定义控件
# 图表 Frame 控件
from ui.chartFrame import chartFrame


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.ui = uic.loadUi('ui/mainWindow.ui', self)
        self.winNum = 2
        # self.iii = 0
        # self.flag = False
        self.time = 0
        self.initUI()

    def initUI(self):
        # 参数设置部分
        self.searchCom()
        # 连接部分
        self.lb_connect.setStyleSheet('QLabel{color: gray}')
        self.lb_start.setStyleSheet('QLabel{color: gray}')
        self.btn_connect.clicked.connect(self.connect_clicked)
        self.btn_disconnect.clicked.connect(self.disconnect_clicked)
        # 按钮部分
        self.btn_start.clicked.connect(self.start_clicked)
        self.btn_stop.clicked.connect(self.stop_clicked)
        # 信息显示部分
        self.et_filePath.setText(os.getcwd())
        self.lb_info.setText('信息显示')
        self.et_text.setText('设置参数信息并点击开始按钮进行测量')
        # 其他部分
        self.btn_filePath.clicked.connect(self.filePath_clicked)
        self.btn_reset.clicked.connect(self.reset_clicked)
        # 图表显示部分
        self.chartFrameList = []
        self.initChartFrame()

    def initChartFrame(self):   # 初始化图表 Frame
        for i in range(self.winNum):
            chartFrameItem = chartFrame()
            self.chartFrameList.append(chartFrameItem)
            self.layoutChart.addWidget(chartFrameItem)

    def searchCom(self):    # 启动更新串口号线程
        self.getComThread = serUtil.getCom()
        self.getComThread.comUpdate.connect(self.updateCom)
        self.getComThread.start()
        self.box_com.currentIndexChanged.connect(self.com_changed)

    def updateCom(self, port_list):  # 更新串口号
        self.box_com.clear()
        if len(port_list) == 0:
            return
        self.box_com.addItems([port_list[i][0] + ' ' + port_list[i][1]
                              for i in range(len(port_list))])
        if glo.get_scan():  # 当前已经连接, 避免重复连接
            if glo.get_com() in [port_list[i][0] for i in range(len(port_list))]:
                self.box_com.setCurrentText(glo.get_com(
                ) + ' ' + port_list[[port_list[i][0] for i in range(len(port_list))].index(glo.get_com())][1])
                return
            else:
                self.disconnect_clicked()
        self.box_com.setCurrentIndex(0)

    def com_changed(self):  # 串口号改变事件
        if glo.get_scan():  # 当前已经连接, 避免重复连接
            self.disconnect_clicked()
            self.connect_clicked()

    def connect_clicked(self):  # 连接按钮点击事件
        if glo.get_scan():   # 当前已经连接, 避免重复连接
            print("已连接, 无需重复连接")
            return
        # 连接串口
        glo.set_ser(serUtil.serialOpen(
            self.box_com.currentText().split(' ')[0],    # 串口号
            self.box_bps.currentText(),  # 波特率
            self.box_timex.currentText()))  # 超时时间
        if serUtil.serialIsOpen(glo.get_ser()):    # 连接成功
            glo.set_scan(True)
            glo.set_com(self.box_com.currentText().split(' ')[0])
            self.btn_start.setEnabled(True)
            self.btn_disconnect.setEnabled(True)
            self.lb_connect.setText(glo.get_com())
            self.lb_connect.setStyleSheet('color: balck')
            self.lb_start.setText('Waiting...')
            self.lb_start.setStyleSheet('color: green')
            serUtil.serialClose(glo.get_ser)
            print("连接成功")
        else:
            print(glo.get_ser)
            self.lb_connect.setText('断开连接')
            self.lb_connect.setStyleSheet('color: red')
            print("连接失败")
            return
        for i in range(self.layoutChart.count()):
            self.layoutChart.itemAt(i).widget().deleteLater()
        self.chartFrameList.clear()
        self.initChartFrame()
        glo.history.clear()

    def disconnect_clicked(self):   # 断开连接按钮点击事件
        if glo.get_scan():
            glo.set_connected(False)
            serUtil.serialClose(glo.get_ser())
            glo.set_com('')
            self.lb_info.setText('断开连接')
            self.lb_connect.setText('等待连接')
            self.lb_connect.setStyleSheet('color: gray')
            self.lb_start.setText('尚未连接')
            self.lb_start.setStyleSheet('color: gray')
            self.btn_start.setEnabled(False)
            self.btn_stop.setEnabled(False)
            self.et_text.setText('设置参数信息并点击开始按钮进行测量')
            self.saveFile()
            glo.set_scan(False)
        else:
            print("未连接, 无需断开连接")
            return

    def start_clicked(self):    # 开始按钮点击事件
        if glo.get_connected():   # 当前已经连接, 避免重复连接
            print("已连接, 无需重复连接")
            return
        # 连接串口
        glo.set_ser(serUtil.serialOpen(self.box_com.currentText().split(' ')[0],    # 串口号
                                       self.box_bps.currentText(),  # 波特率
                                       self.box_timex.currentText()))   # 超时时间
        if serUtil.serialIsOpen(glo.get_ser()):    # 连接成功
            self.connSuccess()
            self.connSeialThread()
            self.connChartTimer()
        else:   # 连接失败
            glo.set_connected(False)
            serUtil.serialClose(glo.get_ser())
            self.lb_info.setText('连接失败')

    def stop_clicked(self):  # 停止按钮点击事件: 关闭串口、停止线程
        serUtil.serialClose(glo.get_ser())
        self.btn_stop.setEnabled(False)
        self.lb_start.setText('已暂停')
        self.lb_start.setStyleSheet('color: red')

    def saveFile(self):  # 保存文件
        if len(glo.history) == 0:
            return
        dirpath, type = QFileDialog.getSaveFileName(self,
                                                    directory=self.et_filePath.text()+QDateTime.currentDateTime().toString('/yy-MM-dd-hhmmss'), caption='保存文件', filter='CSV(*.csv) ;;纯文本(*.txt)', initialFilter='CSV(*.csv)')
        glo.save_data(dirpath, type)

    def connSuccess(self):  # 连接成功
        glo.set_connected(True)  # 设置连接状态
        print("等待执行:", serUtil.serialIsOpen(glo.get_ser()))    # 打印连接状态
        self.btn_stop.setEnabled(True)  # 开启停止按钮
        self.lb_start.setText('正在测量')
        self.lb_start.setStyleSheet('color: green')
        self.lb_info.setText('等待输入数据')
        self.et_text.setText('等待输入数据...')

    def connSeialThread(self):  # 连接串口读取线程
        self.serialRead = serUtil.serialRead()  # 串口读取线程
        self.serialRead.dateReadUpdate.connect(
            self.updateData)   # 信号连接: 串口读取数据 -> 更新数据
        self.serialRead.dateReadUpdate.connect(
            self.updateEt)   # 信号连接: 串口读取数据 -> 更新文本框
        self.serialRead.serDisconnect.connect(
            self.stop_clicked)    # 信号连接: 串口断开 -> 停止按钮点击事件
        self.serialRead.dateReadUpdate.connect(self.updateData_new)   # 信号连接: 串口读取数据 -> 更新图表
        self.serialRead.dateReadUpdate.connect(self.updateEt_new)   # 信号连接: 串口读取数据 -> 更新文本框
        self.serialRead.dateReadUpdate.connect(self.updateChart_new)   # 信号连接: 串口读取数据 -> 更新图表
        self.serialRead.start()  # 开启串口读取线程

    def updateData_new(self, data_list):
        glo.add_history(data_list)
        ...

    def updateEt_new(self, data_list):
        self.et_text.append(str(data_list))
        # self.et_text.append(123)
        self.et_text.moveCursor(self.et_text.textCursor().End)
        ...

    def connChartTimer(self):   # 连接图表定时器
        self.updateChartTimer = QTimer()    # 更新图表定时器
        self.updateChartTimer.timeout.connect(
            self.updateChart_new)    # 信号连接: 定时器 -> 更新图表
        self.updateChartTimer.start(2)

    def updateEt(self, str_list):   # 更新文本框
        self.et_text.append(str_list)
        self.et_text.moveCursor(self.et_text.textCursor().End)
        ...

    def updateData(self, str_list):   # 更新本次数据(串口读取数据)
        glo.add_history(str_list)

    def filePath_clicked(self, Filepath):   # 文件路径按钮点击事件
        path = QFileDialog.getExistingDirectory(
            None, "选取文件夹", self.et_filePath.text())  # 起始路径
        if path != "":
            self.et_filePath.setText(path)

    def reset_clicked(self):    # 重置按钮点击事件
        for chartFrame in self.chartFrameList:
            chartFrame.setVisible(True)
            chartFrame.chart.zoomReset()
        ...

    def updateChart(self):  # 更新图表
        # 更新折线上的点的坐标
        if glo.dataNotEmpty() and glo.get_connected():
            y_list = glo.get_data()
            index = 1
            for i in range(len(y_list)):
                # self.chart.scroll(self.chart.plotArea().width() / 50000, 0)
                x = glo.get_time() * 0.001
                if i % 10 == 0:
                    y = float(y_list[i])
                    self.chartFrameList[index].series.append(x, y)
                    self.chartFrameList[index].dataAxisX.setMin(x - 5)
                    self.chartFrameList[index].dataAxisX.setMax(x)
                    QApplication.processEvents()
                    # print("当前点数:", int(x * 1000))
                    print("总点数：", len(glo.history))
                    # print(len(glo.history))
                    # self.chart.scroll(1, 0)

    def updateChart_new(self):  # 更新图表_new
        # 更新折线上的点的坐标
        if glo.dataNotEmpty() and glo.get_connected():
            y_list = glo.get_data()
            for i in range(len(y_list)):
                x = glo.get_time()
                if x % 30 == 0:
                    x = x * 0.001
                    self.chartFrameList[0].series.append(
                        x, y_list[i][0])
                    self.chartFrameList[0].dataAxisX.setMin(x - 1)
                    self.chartFrameList[0].dataAxisX.setMax(x)
                    QApplication.processEvents()
                    self.chartFrameList[1].series.append(
                        x, y_list[i][1])
                    self.chartFrameList[1].dataAxisX.setMin(x - 1)
                    self.chartFrameList[1].dataAxisX.setMax(x)
                    QApplication.processEvents()
            # print("当前点数:", int(x * 1000))
            # print("总点数：" , len(glo.history))
            # print(len(glo.history))
            # self.chart.scroll(1, 0)

    def keyPressEvent(self, e):  # 重写键盘事件: 按下ESC键关闭串口
        if e.key() == Qt.Key_Escape:
            if glo.connected:
                self.stop_clicked()
        elif e.key() == Qt.Key_R:
            if ~glo.connected:
                self.start_clicked()
        elif e.key() == Qt.Key_Return:
            self.reset_clicked()
        # if e.key() == Qt.Key_Plus:
        #     self.chart.zoomIn()
        # elif e.key() == Qt.Key_Minus:
        #     self.chart.zoomOut()
        # elif e.key() == Qt.Key_Return:
        #     # self.chart.scroll(-1000, 0)
        #     self.chart.zoomReset()
        # elif e.key() == Qt.Key_Right:
        #     self.chart.scroll(1000, 0)
        # elif e.key() == Qt.Key_Up:
        #     self.chart.scroll(0, 1000)
        # elif e.key() == Qt.Key_Down:
        #     self.chart.scroll(0, -1000)


if __name__ == '__main__':
    glo.__init__()
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

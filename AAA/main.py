import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QComboBox, QVBoxLayout
from PyQt5.QtCore import Qt, QDateTime, pyqtSignal
from PyQt5 import uic
# 串口操作
import utils.serialUtil as serUtil
import utils.globalParams as glo
from ui.drawFrame import drawFrame, drawFrameFile
import threading
import time


class MyWindow(QMainWindow):
    XDIS_SIGNAL = pyqtSignal()
    YDIS_SIGNAL = pyqtSignal()
    SAMPLE_RATE_SIGNAL = pyqtSignal()

    def __init__(self):
        super().__init__()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.ui = uic.loadUi('ui/mainWindow.ui', self)
        # self.iii = 0
        # self.flag = False
        self.time = 0
        self.initUI()
        self.initDATA()
    
    def initDATA(self):
        # 串口参数设置部分
        self.searchCom()
        # 连接部分
        self.lb_connect.setStyleSheet('QLabel{color: gray}')
        self.lb_start.setStyleSheet('QLabel{color: gray}')
        # 信息显示部分
        self.et_filePath.setText(os.getcwd())
        self.lb_info.setText('信息显示')
        self.et_text.setText('设置参数信息并点击开始按钮进行测量')
        # 信号处理部分
        glo.YDIS = int(self.box_ydis.currentText())
        glo.XDIS = int(self.box_xdis.currentText())
        glo.isHighPassFilter = self.ck_high.isChecked()
        glo.isNotchFilter = self.ck_notch.isChecked()
        glo.isBandPassFilter = self.ck_band.isChecked()
        glo.sample_rate = int(self.box_sample_rate.currentText())
        # 图表显示列表部分
        self.chartFrameList = []
        self.initChartFrame()

    def initUI(self):
        # 菜单栏部分
        self.action_open.triggered.connect(self.action_open_clicked)
        self.action_save.triggered.connect(self.saveFile)
        self.action_exit.triggered.connect(self.action_exit_clicked)
        # 连接部分
        self.btn_connect.clicked.connect(self.connect_clicked)
        self.btn_disconnect.clicked.connect(self.disconnect_clicked)
        # 按钮部分
        self.btn_start.clicked.connect(self.start_clicked)
        self.btn_stop.clicked.connect(self.stop_clicked)
        # 其他部分
        self.btn_filePath.clicked.connect(self.filePath_clicked)
        self.btn_reset.clicked.connect(self.reset_clicked)
        # 信号处理部分
        self.box_ydis.currentIndexChanged.connect(self.box_all_DIS_changed)
        self.box_xdis.currentIndexChanged.connect(self.box_all_DIS_changed)
        self.ck_high.clicked.connect(self.ck_all_filter_clicked)
        self.sb_high.valueChanged.connect(self.sb_high_valueChanged)  # TODO
        self.sb_notch_cutoff.valueChanged.connect(self.sb_notch_valueChanged)  # TODO
        self.sb_notch_param.valueChanged.connect(self.sb_notch_valueChanged)  # TODO
        self.sb_band_pass.valueChanged.connect(self.sb_band_valueChanged)  # TODO
        self.sb_band_stop.valueChanged.connect(self.sb_band_valueChanged)  # TODO
        self.ck_notch.clicked.connect(self.ck_all_filter_clicked)
        self.ck_band.clicked.connect(self.ck_all_filter_clicked)
        self.box_sample_rate.currentIndexChanged.connect(self.box_sample_rate_changed)
        # Tab 部分
        self.tabWidget.setCurrentIndex(0)
        # tab_file 部分
        self.file_btn_open.clicked.connect(self.action_open_clicked)
        self.file_btn_draw.clicked.connect(self.file_btn_draw_clicked)

    def initDATAFile(self):
        # 信号处理部分
        glo.YDIS = int(self.file_box_ydis.currentText())
        glo.XDIS = int(self.file_box_xdis.currentText())
        glo.isHighPassFilter = self.file_ck_high.isChecked()
        glo.isNotchFilter = self.file_ck_notch.isChecked()
        glo.isBandPassFilter = self.file_ck_band.isChecked()
        glo.sample_rate = int(self.file_box_sample_rate.currentText())

    def file_btn_draw_clicked(self):
        for i in range(glo.channel_num):
            self.chartFrameList[i].history = glo.history[i, :]
            self.chartFrameList[i].drawFile()

    def sb_high_valueChanged(self):
        glo.highFilter_high = self.sb_high.value()
        glo.highFilterUpdate()

    def sb_notch_valueChanged(self):
        glo.notchFilter_cutoff = self.sb_notch_cutoff.value()
        glo.notchFilter_param = self.sb_notch_param.value()
        glo.notchFilterUpdate()
    
    def sb_band_valueChanged(self):
        glo.bandFilter_pass = self.sb_band_pass.value()
        glo.bandFilter_stop = self.sb_band_stop.value()
        glo.bandFilterUpdate()

    def action_open_clicked(self):  # 打开文件事件
        if glo.connected:
            print('请先断开连接')
            return
        dirpath, type = QFileDialog.getOpenFileName(self,
                                                    caption='打开文件', directory=self.et_filePath.text(),
                                                    filter='纯文本(*.txt) ;; CSV(*.csv) ;; All Files (*) ', initialFilter='纯文本(*.txt)')
        if glo.open_data(dirpath, type):
            self.tabWidget.setCurrentIndex(1)
            self.file_et_path.setText(dirpath)
            self.group_tab_file.setEnabled(True)
            glo.initFilterParams()
            self.initDATAFile()
            for i in range(glo.channel_num):
                self.chartFrameList[i].close()
            self.chartFrameList.clear()
            # 清空垂直布局内的表格
            self.chartFrameList = []
            self.initChartFrameFile()
            self.et_filePath.setText(dirpath)
            self.lb_info.setText('文件打开成功')
            self.et_text.setText('文件打开成功')
            print(glo.history.shape)
        ...
    
    def initChartFrameFile(self):
        for i in range(glo.channel_num):
            chartFrameItem = drawFrameFile()
            self.chartFrameList.append(chartFrameItem)
            self.layoutChart.addWidget(chartFrameItem)
        ...

    def saveFile(self):  # 保存文件
        if glo.history.shape[1] < 2:
            print("请先测量数据")
            return
        if glo.connected:
            print('请先断开连接')
            return
        dirpath, type = QFileDialog.getSaveFileName(self,
                                                    directory=self.et_filePath.text()+QDateTime.currentDateTime().toString('/yy-MM-dd-hhmmss'), caption='保存文件', filter='CSV(*.csv) ;;纯文本(*.txt)', initialFilter='CSV(*.csv)')
        glo.save_data(dirpath, type)
    
    def action_exit_clicked(self):  # 退出事件
        ...
    
    def box_all_DIS_changed(self): # 坐标轴轴显示范围改变事件
        if self.sender().objectName() == 'box_ydis':
            glo.YDIS = int(self.box_ydis.currentText())
            self.YDIS_SIGNAL.emit()
            print(glo.YDIS)
        elif self.sender().objectName() == 'box_xdis':
            glo.XDIS = int(self.box_xdis.currentText())
            self.XDIS_SIGNAL.emit()
            print(glo.XDIS)
        ...

    def ck_all_filter_clicked(self): # 滤波器选择事件
        if self.sender().objectName() == 'ck_low':
            glo.isHighPassFilter = self.ck_low.isChecked()
            print("HighPassFilter: ", glo.isHighPassFilter)
        
        elif self.sender().objectName() == 'ck_notch':
            glo.isNotchFilter = self.ck_notch.isChecked()
            print("NotchFilter: ", glo.isNotchFilter)
        
        elif self.sender().objectName() == 'ck_band':
            glo.isBandPassFilter = self.ck_band.isChecked()
            print("BandPassFilter", glo.isBandPassFilter)

    def box_sample_rate_changed(self):  # 采样率改变事件
        glo.sample_rate = int(self.box_sample_rate.currentText())
        print(glo.sample_rate)
        ...

    def initChartFrame(self):   # 初始化图表 Frame
        for i in range(glo.channel_num):
            chartFrameItem = drawFrame()
            self.XDIS_SIGNAL.connect(chartFrameItem.updateXlim)
            self.YDIS_SIGNAL.connect(chartFrameItem.updateYlim)
            # chartFrameItem.lb_min.setText(str(i))
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

    def com_changed(self):  # 串口号改变事
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
            self.group_tab_file.setEnabled(False)
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
        glo.init_history()

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
            # self.mythread = threading.Thread(target=self.updateChart)
            # self.mythread.daemon = True
            # self.mythread.start()
            glo.initFilterParams()
            self.connSuccess()
            self.connSeialThread()
            self.box_sample_rate.setEnabled(False)
            # self.updateFigThread()
            # self.connChartTimer()
        else:   # 连接失败
            glo.set_connected(False)
            serUtil.serialClose(glo.get_ser())
            self.lb_info.setText('连接失败')

    def stop_clicked(self):  # 停止按钮点击事件: 关闭串口、停止线程
        for i in range(3):
            try:
                glo.ser.write(glo.send_stop)
            except:
                ...
            finally:
                print("发送停止指令")
        serUtil.serialClose(glo.get_ser())
        self.serialRead.terminate()
        self.btn_stop.setEnabled(False)
        self.lb_start.setText('已暂停')
        self.lb_start.setStyleSheet('color: red')
        self.box_sample_rate.setEnabled(True)

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
        self.serialRead.serDisconnect.connect(
            self.stop_clicked)    # 信号连接: 串口断开 -> 停止按钮点击事件
        self.serialRead.dateReadUpdate_new.connect(self.updateData)   # 信号连接: 串口读取数据 -> 更新图表
        self.serialRead.dateReadUpdate_new.connect(self.updateEt)   # 信号连接: 串口读取数据 -> 更新文本框
        self.serialRead.start()  # 开启串口读取线程

    def updateFigThread(self):  # 更新图表线程
        for chart in self.chartFrameList:
            figThread = serUtil.updateFig(chart)
            # figThread = serUtil.processFig(chart)
            figThread.start()
        # self.figThread = serUtil.updateFig(self.chartFrameList)
        # self.figThread.start()

    def updateData(self, data_list):    # 更新数据及图表
        glo.add_history(data_list)
        # time1 = time.time()
        for i in range(len(self.chartFrameList)):
            if len(data_list[i]) > 0:
                self.chartFrameList[i].addData(data_list[i])
        # print("更新数据耗时:", time.time()-time1)
        ...

    def updateEt(self, data_list):  # 更新文本框
        self.et_text.append(str(data_list))
        # self.et_text.append(123)
        self.et_text.moveCursor(self.et_text.textCursor().End)
        ...

    def filePath_clicked(self, Filepath):   # 文件路径按钮点击事件
        path = QFileDialog.getExistingDirectory(
            None, "选取文件夹", self.et_filePath.text())  # 起始路径
        if path != "":
            self.et_filePath.setText(path)

    def reset_clicked(self):    # 重置按钮点击事件
        for chartFrame in self.chartFrameList:
            chartFrame.canvas.zoomReset()
            chartFrame.setVisible(True)
            # chartFrame.chart.zoomReset()
        ...

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
    
    def closeEvent(self, event):    # 重写关闭事件: 关闭串口
        try:
            self.serialRead.terminate()
            self.getComThread.terminate()
            self.updateFigThread.terminate()
        except:
            ...


if __name__ == '__main__':
    glo.__init__()
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
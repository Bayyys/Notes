import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QComboBox, QVBoxLayout
from PyQt5.QtCore import Qt, QDateTime, pyqtSignal, QThread, QMutex
from PyQt5 import uic
# 串口操作
import utils.serialUtil as serUtil
import utils.globalParams as glo
from ui.drawFrame import drawFrame, drawFrameFile, FFTCanvas, FFTThread
from ui.mainWindow import Ui_MainWindow
import numpy as np


class MyWindow(QMainWindow, Ui_MainWindow):
    XDIS_SIGNAL = pyqtSignal()
    YDIS_SIGNAL = pyqtSignal()
    SAMPLE_RATE_SIGNAL = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.ui = uic.loadUi('ui/mainWindow.ui', self)
        self.initDATA() # 初始化数据
        self.initUI()   # 初始化UI界面

    def initUI(self):
        self.initMenuUI()   # 菜单栏初始化
        self.initRealTimeUI()   # 实时检测界面初始化
        self.initFileUI()   # 文件处理界面初始化

    def initMenuUI(self):  # 菜单栏初始化
         # 菜单栏部分
        self.action_open.triggered.connect(self.action_open_clicked)    # 菜单栏-打开文件
        self.action_save.triggered.connect(self.action_save_clicked)           # 菜单栏-保存文件
        self.action_exit.triggered.connect(self.action_exit_clicked)    # 菜单栏-退出
        # Tab 部分
        self.tabWidget.setCurrentIndex(0)   # 默认显示实时检测部分
    
    def initRealTimeUI(self):  # 实时检测界面初始化
        #=========== 实时检测部分 ===========#
        # 连接部分
        self.btn_connect.clicked.connect(self.btn_connect_clicked)   # 连接按钮
        self.btn_disconnect.clicked.connect(
            self.btn_disconnect_clicked)    # 断开连接按钮
        self.box_com.currentIndexChanged.connect(
            self.box_com_changed)  # Com 端口选择
        # 按钮部分
        self.btn_start.clicked.connect(self.btn_start_clicked)  # 开始按钮
        self.btn_stop.clicked.connect(self.btn_stop_clicked)    # 停止按钮
        # 其他部分
        self.btn_filePath.clicked.connect(
            self.btn_filePath_clicked)    # 文件路径按钮
        self.btn_reset.clicked.connect(self.btn_reset_clicked)  # 重置按钮
        # 信号处理部分
        self.box_ydis.currentIndexChanged.connect(
            self.box_all_DIS_changed)  # Y轴显示范围
        self.box_xdis.currentIndexChanged.connect(
            self.box_all_DIS_changed)  # X轴显示范围
        self.ck_baseline.clicked.connect(self.ck_all_filter_clicked)    # 基线开关
        self.ck_low.clicked.connect(self.ck_all_filter_clicked)    # 低通滤波器开关
        self.ck_high.clicked.connect(self.ck_all_filter_clicked)    # 高通滤波器开关
        self.ck_notch.clicked.connect(self.ck_all_filter_clicked)   # 陷波滤波器开关
        self.ck_band.clicked.connect(self.ck_all_filter_clicked)    # 带通滤波器开关
        self.sb_low.valueChanged.connect(self.sb_low_valueChanged)  # 高通滤波器截止频率
        self.sb_high.valueChanged.connect(
            self.sb_high_valueChanged)  # 高通滤波器截止频率
        self.sb_notch_cutoff.valueChanged.connect(
            self.sb_notch_valueChanged)   # 陷波滤波器截止频率
        self.sb_notch_param.valueChanged.connect(
            self.sb_notch_valueChanged)  # 陷波滤波器参数
        self.sb_band_pass.valueChanged.connect(
            self.sb_band_valueChanged)   # 带通滤波器通带频率
        self.sb_band_stop.valueChanged.connect(
            self.sb_band_valueChanged)   # 带通滤波器阻带频率
        self.box_sample_rate.currentIndexChanged.connect(
            self.box_sample_rate_changed)  # 采样率
        self.box_channel_num.currentIndexChanged.connect(
            self.box_channel_num_changed)  # 通道数
    
    def initFileUI(self):  # 文件处理界面初始化
        #=========== 历史数据部分 ===========#
        # 文件操作部分
        self.file_btn_open.clicked.connect(
            self.action_open_clicked)    # 打开文件按钮
        self.file_btn_dataload.setVisible(False)    # 数据加载按钮: 隐藏
        self.file_btn_dataload.clicked.connect(
            self.file_btn_dataload_clicked)  # 数据加载按钮
        self.file_btn_draw.clicked.connect(self.file_btn_draw_clicked)  # 绘制按钮
        self.file_btn_reset.clicked.connect(
            self.file_btn_reset_clicked)    # 重置按钮
        # 信号处理部分
        self.file_box_ydis.currentIndexChanged.connect(
            self.file_box_all_DIS_changed)  # Y轴显示范围
        self.file_box_xdis.currentIndexChanged.connect(
            self.file_box_all_DIS_changed)  # X轴显示范围
        self.file_btn_delete.clicked.connect(self.file_btn_delete_clicked)  # 删除部分数据点按钮
        self.file_ck_baseline.clicked.connect(
            self.file_ck_all_filter_clicked)    # 基线开关
        self.file_ck_low.clicked.connect(
            self.file_ck_all_filter_clicked)    # 高通滤波器开关
        self.file_ck_high.clicked.connect(
            self.file_ck_all_filter_clicked)    # 高通滤波器开关
        self.file_ck_notch.clicked.connect(
            self.file_ck_all_filter_clicked)   # 陷波滤波器开关
        self.file_ck_band.clicked.connect(
            self.file_ck_all_filter_clicked)    # 带通滤波器开关
        self.file_sb_low.valueChanged.connect(
            self.sb_low_valueChanged)  # 高通滤波器截止频率
        self.file_sb_high.valueChanged.connect(
            self.sb_high_valueChanged)  # 高通滤波器截止频率
        self.file_sb_notch_cutoff.valueChanged.connect(
            self.sb_notch_valueChanged)   # 陷波滤波器截止频率
        self.file_sb_notch_param.valueChanged.connect(
            self.sb_notch_valueChanged)  # 陷波滤波器参数
        self.file_sb_band_pass.valueChanged.connect(
            self.sb_band_valueChanged)   # 带通滤波器通带频率
        self.file_sb_band_stop.valueChanged.connect(
            self.sb_band_valueChanged)   # 带通滤波器阻带频率
        self.file_box_sample_rate.currentIndexChanged.connect(
            self.file_box_sample_rate_changed)  # 采样率
    
    #============================= 实时检测界面 =============================#

    #-------------------------------  初始化 -------------------------------#

    def initDATA(self):  # 实时检测界面初始化数据
        # 串口参数设置部分
        self.searchCom()
        # 连接部分
        self.lb_connect.setStyleSheet('QLabel{color: gray}')
        self.lb_start.setStyleSheet('QLabel{color: gray}')
        # 信息显示部分
        self.et_filePath.setText(os.getcwd())
        # 信号处理部分
        self.initdata()
        # 图表显示列表部分
        self.chartFrameList = []
        self.initChartFrame()
        # FFT部分
        self.fftcanvas = FFTCanvas()
        self.layoutFFT.addWidget(self.fftcanvas)
    
    def initdata(self):
        glo.channel_num = int(self.box_channel_num.currentText())
        glo.YDIS = int(self.box_ydis.currentText())
        glo.XDIS = int(self.box_xdis.currentText())
        glo.isLowPassFilter = self.ck_low.isChecked()
        glo.isHighPassFilter = self.ck_high.isChecked()
        glo.isNotchFilter = self.ck_notch.isChecked()
        glo.isBandPassFilter = self.ck_band.isChecked()
        glo.highFilter_high = self.sb_high.value()
        glo.lowFilter_low = self.sb_low.value()
        glo.notchFilter_cutoff = self.sb_notch_cutoff.value()
        glo.notchFilter_param = self.sb_notch_param.value()
        glo.bandFilter_pass = self.sb_band_pass.value()
        glo.bandFilter_stop = self.sb_band_stop.value()
        glo.sample_rate = int(self.box_sample_rate.currentText())

    def initChartFrame(self):   # 初始化图表 Frame
        for i in range(2):
            chartFrameItem = drawFrame(self)
            self.XDIS_SIGNAL.connect(chartFrameItem.updateXlim)
            self.YDIS_SIGNAL.connect(chartFrameItem.updateYlim)
            if i == 2:
                chartFrameItem.canvas.line.set_color('orange')
            # chartFrameItem.lb_min.setText(str(i))
            self.chartFrameList.append(chartFrameItem)
            self.layoutChart.addWidget(chartFrameItem)

    def initUIDate(self):
        #----------------- 实时检测部分 -----------------#
        self.box_ydis.setCurrentIndex(5)
        self.box_xdis.setCurrentIndex(1)
        self.box_sample_rate.setCurrentIndex(2)
        self.box_channel_num.setCurrentIndex(0)
        self.ck_baseline.setChecked(True)
        self.ck_low.setChecked(False)
        self.ck_high.setChecked(False)
        self.ck_notch.setChecked(False)
        self.ck_band.setChecked(False)
        self.sb_low.setValue(50)
        self.sb_high.setValue(1)
        self.sb_notch_cutoff.setValue(50)
        self.sb_notch_param.setValue(10)
        self.sb_band_pass.setValue(1)
        self.sb_band_stop.setValue(50)
        #----------------- 文件检测部分 -----------------#
        self.file_box_ydis.setCurrentIndex(5)
        self.file_box_xdis.setCurrentIndex(1)
        self.file_box_sample_rate.setCurrentIndex(2)
        self.file_box_channel_num.setCurrentIndex(0)
        self.file_ck_baseline.setChecked(True)
        self.file_ck_low.setChecked(False)
        self.file_ck_high.setChecked(False)
        self.file_ck_notch.setChecked(False)
        self.file_ck_band.setChecked(False)
        self.file_sb_low.setValue(50)
        self.file_sb_high.setValue(1)
        self.file_sb_notch_cutoff.setValue(50)
        self.file_sb_notch_param.setValue(10)
        self.file_sb_band_pass.setValue(1)
        self.file_sb_band_stop.setValue(50)
        ...

    #------------------------------- 控件事件 -------------------------------#
 
    def action_open_clicked(self):  # 打开文件事件
        if glo.connected:
            self.statusBar.showMessage('请先断开连接', 3000)
            return
        dirpath, type = QFileDialog.getOpenFileName(self,
                                                    caption='打开文件', directory=self.et_filePath.text(),
                                                    filter='纯文本(*.txt) ;; CSV(*.csv) ;; All Files (*) ', initialFilter='纯文本(*.txt)')
        if glo.load_data(dirpath, type):
            self.file_btn_draw.setText('绘制')
            self.initUIDate()
            self.tabWidget.setCurrentIndex(1)
            self.file_et_path.setText(dirpath)
            self.group_state_file.setEnabled(True)
            self.group_draw_file.setEnabled(True)
            self.group_setting_file.setEnabled(True)
            self.group_params_file.setEnabled(False)
            glo.initFilterParams()
            self.initDATAFile()
            for i in range(2):
                self.chartFrameList[i].close()
            self.chartFrameList.clear()
            # 清空垂直布局内的表格
            self.chartFrameList = []
            self.initChartFrameFile()
            self.et_filePath.setText(dirpath)
            self.statusBar.showMessage('文件加载成功 (' + dirpath + ')', 5000)
            # print(glo.history.shape)
        ...

    def action_save_clicked(self):  # 保存文件
        if glo.history.shape[1] < 2:
            self.statusBar.showMessage("请先测量数据", 3000)
            return
        if glo.connected:
            self.statusBar.showMessage('请先断开连接', 3000)
            return
        dirpath, type = QFileDialog.getSaveFileName(self,
                                                    directory=self.et_filePath.text()+QDateTime.currentDateTime().toString('/yy-MM-dd-hhmm')+'-'+str(glo.sample_rate)+'Hz'+'-'+str(int(glo.history.shape[1] / glo.sample_rate))+'s', caption='保存文件', filter='CSV(*.csv) ;;纯文本(*.txt)', initialFilter='纯文本(*.txt)')
        glo.save_data(dirpath, type)
        if dirpath != '':
            self.statusBar.showMessage('文件保存成功 (' + dirpath + ')', 5000)
        else:
            self.statusBar.showMessage('文件保存失败, 请及时存储测量数据!', 3000)
        self.file_btn_dataload.setVisible(True) # 保存成功后, 打开数据加载按钮

    def action_exit_clicked(self):  # 退出事件
        ...

    def btn_connect_clicked(self):  # 连接按钮点击事件
        if glo.get_scan():   # 当前已经连接, 避免重复连接
            self.statusBar.showMessage("已连接, 无需重复连接", 3000)
            return
        # 连接串口

        glo.set_ser(serUtil.serialOpen(
            self.box_com.currentText().split(' ')[0],    # 串口号
            self.box_bps.currentText(),  # 波特率
            self.box_timex.currentText()))  # 超时时间
        if serUtil.serialIsOpen(glo.get_ser()):    # 连接成功
            self.statusBar.showMessage("串口连接成功, 点击<开始>按钮进行测量", 5000)
            self.group_state_file.setEnabled(False)
            self.group_params_file.setEnabled(False)
            glo.set_scan(True)
            glo.set_com(self.box_com.currentText().split(' ')[0])
            self.btn_start.setEnabled(True)
            self.btn_disconnect.setEnabled(True)
            self.lb_connect.setText(glo.get_com())
            self.lb_connect.setStyleSheet('color: balck')
            glo.time_all = 0
            glo.time_temp = 0
            self.lb_start.setText('等待测量')
            self.lb_start.setStyleSheet('color: green')
            self.initUIDate()
            self.initdata()
            serUtil.serialClose(glo.get_ser)
            self.initConnectParams()
        else:
            self.lb_connect.setText('无法连接')
            self.lb_connect.setStyleSheet('color: red')
            self.statusBar.showMessage("连接失败", 3000)
            return
        for i in range(self.layoutChart.count()):
            self.layoutChart.itemAt(i).widget().deleteLater()
        self.chartFrameList.clear()
        self.initChartFrame()
        glo.init_history()

    def btn_disconnect_clicked(self):   # 断开连接按钮点击事件
        if glo.get_scan():
            glo.set_connected(False)
            serUtil.serialClose(glo.get_ser())
            glo.set_com('')
            self.lb_connect.setText('等待连接')
            self.lb_connect.setStyleSheet('color: gray')
            self.lb_start.setText('尚未连接')
            self.lb_start.setStyleSheet('color: gray')
            self.btn_start.setEnabled(False)
            self.btn_stop.setEnabled(False)
            self.action_save_clicked()
            self.box_sample_rate.setEnabled(True)
            glo.set_scan(False)
        else:
            self.statusBar.showMessage("未连接, 无需断开连接", 3000)
            return

    def btn_start_clicked(self):    # 开始按钮点击事件
        if glo.get_connected():   # 当前已经连接, 避免重复连接
            self.statusBar.showMessage("已连接, 无需重复连接", 3000)
            return
        # 连接串口
        glo.set_ser(serUtil.serialOpen(self.box_com.currentText().split(' ')[0],    # 串口号
                                       self.box_bps.currentText(),  # 波特率
                                       self.box_timex.currentText()))   # 超时时间
        if serUtil.serialIsOpen(glo.get_ser()):    # 连接成功
            # self.mythread = threading.Thread(target=self.updateChart)
            # self.mythread.daemon = True
            # self.mythread.start()
            # print("开始发送指令")
            glo.sendMessage(state='start', connect='usb', sample_rate=glo.sample_rate, channel=glo.channel_num)
            # print("发送指令完毕")
            glo.initFilterParams()
            self.connSuccess()
            self.connSeialThread()
            self.fftThread()
            self.box_sample_rate.setEnabled(False)
            self.statusBar.showMessage("开始测量", 5000)
            # self.updateFigThread()
            # self.connChartTimer()
        else:   # 连接失败
            glo.set_connected(False)
            serUtil.serialClose(glo.get_ser())

    def btn_stop_clicked(self):  # 停止按钮点击事件: 关闭串口、停止线程
        glo.sendMessage(state='stop')
        serUtil.serialClose(glo.get_ser())
        self.serialRead.terminate()
        self.fftthread.terminate()
        self.btn_stop.setEnabled(False)
        self.lb_start.setText('已暂停')
        self.lb_start.setStyleSheet('color: red')
        self.box_sample_rate.setEnabled(True)

    def box_com_changed(self):  # 串口号改变事
        if glo.get_scan():  # 当前已经连接, 避免重复连接
            self.btn_disconnect_clicked()
            self.btn_connect_clicked()

    def btn_filePath_clicked(self):   # 文件路径按钮点击事件
        path = QFileDialog.getExistingDirectory(
            None, "选取文件夹", self.et_filePath.text())  # 起始路径
        if path != "":
            self.et_filePath.setText(path)

    def btn_reset_clicked(self):    # 重置按钮点击事件
        for chartFrame in self.chartFrameList:
            chartFrame.canvas.zoomReset()
            chartFrame.setVisible(True)
            # chartFrame.chart.zoomReset()
        ...

    def box_all_DIS_changed(self):  # 坐标轴轴显示范围改变事件
        if self.sender().objectName() == 'box_ydis':
            glo.YDIS = int(self.box_ydis.currentText())
            self.YDIS_SIGNAL.emit()
            self.statusBar.showMessage('Y轴显示范围: ' + self.box_ydis.currentText() + 'μV', 3000)
        elif self.sender().objectName() == 'box_xdis':
            glo.XDIS = int(self.box_xdis.currentText())
            self.XDIS_SIGNAL.emit()
            self.statusBar.showMessage('X轴显示范围: ' + self.box_xdis.currentText() + 'ms', 3000)
        ...

    def ck_all_filter_clicked(self):  # 滤波器选择事件
        if self.sender().objectName() == 'ck_baseline':
            glo.isBaseline = self.ck_baseline.isChecked()
            if glo.connected:
                self.statusBar.showMessage('基线移除: ' + ('开启' if glo.isBaseline else '关闭'), 3000)
        elif self.sender().objectName() == 'ck_low':
            glo.isLowPassFilter = self.ck_low.isChecked()
            if glo.connected:
                self.statusBar.showMessage('低通滤波器: ' + ('开启' if glo.isLowPassFilter else '关闭'), 3000)
        elif self.sender().objectName() == 'ck_high':
            glo.isHighPassFilter = self.ck_high.isChecked()
            if glo.connected:
                self.statusBar.showMessage('高通滤波器: ' + ('开启' if glo.isHighPassFilter else '关闭'), 3000)
        elif self.sender().objectName() == 'ck_notch':
            glo.isNotchFilter = self.ck_notch.isChecked()
            if glo.connected:
                self.statusBar.showMessage('陷波滤波器: ' + ('开启' if glo.isNotchFilter else '关闭'), 3000)

        elif self.sender().objectName() == 'ck_band':
            glo.isBandPassFilter = self.ck_band.isChecked()
            if glo.connected:
                self.statusBar.showMessage('带通滤波器: ' + ('开启' if glo.isBandPassFilter else '关闭'), 3000)

    def sb_low_valueChanged(self):     # 低通滤波器截止频率改变事件
        glo.lowFilter_low = self.sb_low.value()
        glo.lowFilterUpdate()

    def sb_high_valueChanged(self):     # 高通滤波器截止频率改变事件
        glo.highFilter_high = self.sb_high.value()
        glo.highFilterUpdate()

    def sb_notch_valueChanged(self):    # 陷波滤波器截止频率和参数改变事件
        glo.notchFilter_cutoff = self.sb_notch_cutoff.value()
        glo.notchFilter_param = self.sb_notch_param.value()
        glo.notchFilterUpdate()

    def sb_band_valueChanged(self):    # 带通滤波器通带频率和阻带频率改变事件
        glo.bandFilter_pass = self.sb_band_pass.value() # 
        glo.bandFilter_stop = self.sb_band_stop.value()
        if glo.bandFilter_stop < glo.bandFilter_pass:
            glo.bandFilter_stop += glo.bandFilter_pass
        glo.bandFilterUpdate()

    def box_sample_rate_changed(self):  # 采样率改变事件
        glo.sample_rate = int(self.box_sample_rate.currentText())
        self.statusBar.showMessage('采样率: ' + self.box_sample_rate.currentText() + 'Hz', 3000)
        if glo.sample_rate == 8000:
            self.box_xdis.setCurrentIndex(4)
            # self.box_xdis.setEnabled(False)
            ...
        else:
            self.box_xdis.setCurrentIndex(1)
            # self.box_xdis.setEnabled(True)
            ...
        ...

    def box_channel_num_changed(self):  # 通道数改变事件
        self.statusBar.showMessage(
            '通道数: ' + self.box_channel_num.currentText(), 3000)
        glo.channel_num = int(self.box_channel_num.currentText())
        ...

    #---------------------------- 串口线程操作 --------------------------#

    def searchCom(self):    # 启动更新串口号线程 --> initData()
        self.getComThread = serUtil.getCom()
        self.getComThread.comUpdate.connect(self.updateCom)
        self.getComThread.start()

    def updateCom(self, port_list):  # 更新串口号   --> 更新串口号线程：串口列表发生变化时触发
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
                self.btn_disconnect_clicked()
        self.box_com.setCurrentIndex(0)

    def connSuccess(self):  # 连接成功  --> 连接按钮点击事件：连接成功时触发
        glo.set_connected(True)  # 设置连接状态
        print("等待执行:", serUtil.serialIsOpen(glo.get_ser()))    # 打印连接状态
        self.btn_stop.setEnabled(True)  # 开启停止按钮
        self.lb_start.setText('正在测量')
        self.lb_start.setStyleSheet('color: green')

    def initConnectParams(self):  # 初始化连接参数  --> 连接按钮点击事件：连接成功时触发
        ...

    def connSeialThread(self):  # 连接串口读取线程  --> 连接按钮点击事件：连接成功时触发
        if glo.channel_num == 2:
            self.serialRead = serUtil.serialRead2()  # 串口读取线程-双通道
        else:
            self.serialRead = serUtil.serialRead()  # 串口读取线程-32通道
        self.serialRead.serDisconnect.connect(
            self.btn_stop_clicked)    # 信号连接: 串口断开 -> 停止按钮点击事件
        self.serialRead.dateReadUpdate.connect(self.updateData)   # 信号连接: 串口读取数据 -> 更新图表
        # self.serialRead.dateReadUpdate.connect(self.updateEt)   # 信号连接: 串口读取数据 -> 更新文本框
        self.serialRead.start()  # 开启串口读取线程

    def fftThread(self):
        self.fftthread = FFTThread(self)
        self.fftthread.fftSignal.connect(self.fftcanvas.updateFFT)
        self.fftthread.start()

    def updateData(self, data_list):    # 更新数据及图表    --> 串口读取线程：串口读取数据时触发
        glo.add_history(data_list)
        # time1 = time.time()
        for i in range(len(self.chartFrameList)):
            if len(data_list[i]) > 0:
                self.chartFrameList[i].addData(data_list[i])
        ...
    
    def updateEt(self, data_list):  # 更新文本框    --> 串口读取线程：串口读取数据时触发 # WAIT
        self.et_text.append(str(data_list))
        self.et_text.moveCursor(self.et_text.textCursor().End)
        ...

    #============================ 历史数据界面 ============================#

    def file_btn_dataload_clicked(self):  # 历史数据界面：数据加载按钮点击事件
        self.file_btn_draw.setText('绘制')
        self.initUIDate()
        self.file_btn_dataload.setVisible(False)
        self.file_et_path.setText("实时检测数据")
        self.group_state_file.setEnabled(True)
        self.group_setting_file.setEnabled(True)
        self.group_draw_file.setEnabled(True)
        self.group_params_file.setEnabled(False)
        glo.initFilterParams()
        self.initDATAFile()
        for i in range(2):
            self.chartFrameList[i].close()
        self.chartFrameList.clear()
        # 清空垂直布局内的表格
        self.chartFrameList = []
        self.initChartFrameFile()
        self.statusBar.showMessage("实时检测数据加载成功", 3000)

    def initDATAFile(self): # 历史数据界面初始化数据
        # 信号处理部分
        glo.YDIS = int(self.file_box_ydis.currentText())
        glo.XDIS = int(self.file_box_xdis.currentText())
        glo.isHighPassFilter = self.file_ck_high.isChecked()
        glo.isNotchFilter = self.file_ck_notch.isChecked()
        glo.isBandPassFilter = self.file_ck_band.isChecked()
        glo.sample_rate = int(self.file_box_sample_rate.currentText())

    def initChartFrameFile(self):   # 初始化历史数据界面的图表显示列表
        for i in range(2):
            chartFrameItem = drawFrameFile(self)
            self.XDIS_SIGNAL.connect(chartFrameItem.updateXlim)
            self.YDIS_SIGNAL.connect(chartFrameItem.updateYlim)
            if i == 2:
                chartFrameItem.canvas.line.set_color('orange')
            self.SAMPLE_RATE_SIGNAL.connect(chartFrameItem.updateSampleRate)
            chartFrameItem.history = glo.history[i, :]
            self.chartFrameList.append(chartFrameItem)
            self.layoutChart.addWidget(chartFrameItem)
        ...

    def file_btn_draw_clicked(self):    # 历史数据绘制按钮事件
        self.group_params_file.setEnabled(True)
        if self.file_btn_draw.text() == '绘制':
            for i in range(2):
                # self.chartFrameList[i].history = glo.history[i, :]
                self.chartFrameList[i].drawFile()
            self.file_btn_draw.setText('重新绘制')
        else:
            for i in range(2):
                self.chartFrameList[i].drawFileAgain()
        ...
    
    def file_btn_reset_clicked(self):    # 重置按钮点击事件
        for chartFrame in self.chartFrameList:
            chartFrame.canvas.zoomReset()
            chartFrame.setVisible(True)
            # chartFrame.chart.zoomReset()
        ...
    
    def file_btn_delete_clicked(self):
        self.file_btn_reset_clicked()
        delete_from = int(self.file_sb_delete_low.text())
        delete_to = int(self.file_sb_delete_high.text())
        if delete_from == '' or delete_to == '':
            return
        if delete_from >= delete_to:
            self.statusBar.showMessage("区间设置错误", 3000)
        if delete_to >= glo.history.shape[1] / glo.sample_rate:
            delete_to = glo.history.shape[1] / glo.sample_rate
            return
        glo.history = np.delete(glo.history, range(delete_from * glo.sample_rate, delete_to * glo.sample_rate), axis=1)
        self.statusBar.showMessage("删除区间：" + str(delete_from) + "s - " + str(delete_to) + "s 成功", 3000)
        for i in range(2):
            self.chartFrameList[i].history = glo.history[i, :]
            self.chartFrameList[i].drawFile()
            # chartFrame.chart.zoomReset()
        ...

    def file_box_sample_rate_changed(self): # 采样率改变事件
        glo.sample_rate = int(self.file_box_sample_rate.currentText())

        self.SAMPLE_RATE_SIGNAL.emit()
        self.statusBar.showMessage("采样率设置为：" + str(glo.sample_rate), 3000)

    def file_box_all_DIS_changed(self):  # 坐标轴轴显示范围改变事件
        if self.sender().objectName() == 'file_box_ydis':
            glo.YDIS = int(self.file_box_ydis.currentText())
            self.YDIS_SIGNAL.emit()
            self.statusBar.showMessage("Y轴显示范围设置为: " + str(glo.YDIS), 3000)
        elif self.sender().objectName() == 'file_box_xdis':
            glo.XDIS = int(self.file_box_xdis.currentText())
            # self.XDIS_SIGNAL.emit()
            self.statusBar.showMessage("X轴显示范围设置为: " + str(glo.XDIS) + '. 点击<重新绘制>按钮进行图像更新！', 3000)
        ...

    def file_ck_all_filter_clicked(self):  # 滤波器选择事件
        if self.sender().objectName() == 'file_ck_baseline':
            glo.isBaseline = self.file_ck_baseline.isChecked()
            self.statusBar.showMessage(
                '基线移除: ' + ('开启' if glo.isBaseline else '关闭') + '. 点击<重新绘制>按钮进行图像更新！', 3000)
        elif self.sender().objectName() == 'file_ck_low':
            glo.isLowPassFilter = self.file_ck_low.isChecked()
            self.statusBar.showMessage(
                '低通滤波: ' + ('开启' if glo.isLowPassFilter else '关闭') + '. 点击<重新绘制>按钮进行图像更新！', 3000)
        elif self.sender().objectName() == 'file_ck_low':
            glo.isHighPassFilter = self.file_ck_low.isChecked()
            self.statusBar.showMessage(
                '高通滤波: ' + ('开启' if glo.isHighPassFilter else '关闭') + '. 点击<重新绘制>按钮进行图像更新！', 3000)
        elif self.sender().objectName() == 'file_ck_notch':
            glo.isNotchFilter = self.file_ck_notch.isChecked()
            self.statusBar.showMessage(
                '陷波滤波: ' + ('开启' if glo.isNotchFilter else '关闭') + '. 点击<重新绘制>按钮进行图像更新！', 3000)
        elif self.sender().objectName() == 'file_ck_band':
            glo.isBandPassFilter = self.file_ck_band.isChecked()
            self.statusBar.showMessage(
                '带通滤波: ' + ('开启' if glo.isBandPassFilter else '关闭') + '. 点击<重新绘制>按钮进行图像更新！', 3000)

    #============================ 窗口线程重写 ============================#

    def keyPressEvent(self, e):  # 重写键盘事件: 按下ESC键关闭串口
        if e.key() == Qt.Key_Escape:
            if glo.connected:
                self.btn_stop_clicked()
        elif e.key() == Qt.Key_R:
            if ~glo.connected:
                self.btn_start_clicked()
        elif e.key() == Qt.Key_Return:
            self.btn_reset_clicked()
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
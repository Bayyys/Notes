import sys
import datetime
import time
from PyQt5 import QtCore
import serial
import serial.tools.list_ports

# PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QComboBox

class PacketDecode():
    '''数据包解析'''

    def __init__(self) -> None:
        self.remain = ""  # 保存上一次解析的数据包的剩余部分
        self.str_show = ""  # 保存解析后的数据(文本描述)
        # IMU
        self.Acc_list = []  # 保存解析后的加速度数据
        self.Gyro_list = [] # 保存解析后的角速度数据
        self.Angle_list = []    # 保存解析后的角度数据
        self.Mag_list = []  # 保存解析后的磁场数据
        self.T_list = []    # 保存解析后的温度数据
        # 压力传感器
        self.P_list = []    # 保存解析后的压力数据
        ...

    def decode_imu(self, recive: str) -> dict:
        ''' 解析 IMU 数据

        将接收到的数据根据包头(0x55)进行分段, 然后解析数据包

        Args:
        ----------------
            recive(str): 接收到的数据
        
        Returns:
        ----------------
            str_show(str): 解析后的数据
        '''
        self.str_show = ""
        self.Acc_list = []
        self.Gyro_list = []
        self.Angle_list = []
        self.Mag_list = []
        self.T_list = []
        # 从数据中提取出数据包
        recive = self.remain + recive
        while len(recive) >= 22:
            # 搜索包头
            if recive[0:2] != "55":
                # 找到第一个 '55'
                position = recive.find("55")
                if position == -1:
                    # 没有找到 '55'
                    self.remain = ""
                    return self.str_show
                else:
                    # 找到了 '55'
                    recive = recive[position:]
                continue
            # 提取数据包
            packet = recive[:22]
            # 解析数据包
            try:
                self.str_show += self.decode_packet_imu(packet)
                recive = recive[22:]
            except:
                # 打印错误信息
                print("IMU 数据包解析错误" + str(packet[:22]))
                recive = recive[2:]

        if len(recive) < 22:
            self.remain = recive
        return [self.str_show, [self.Acc_list, self.Gyro_list, self.Angle_list, self.Mag_list, self.T_list]]

    def decode_packet_imu(self, packet):
        ''' 解析 IMU 数据包

        数据包头为 0x55 0xXX, 其中 XX 为数据包类型

        数据包类型:
        ----------------
            0x51 - 加速度 Acc;
            0x52 - 角速度 Gyro;
            0x53 - 角度 Angle;
            0x54 - 磁场 Mag;
        
        Args:
        ----------------
            packet(str): 分割后的数据包(长度为 22 个字符)
        
        Returns:
        ----------------
            str_show(str): 解析后的数据
        '''
        code = packet[2:4]
        if code == "51":
            # self.print_packet(packet)
            # 加速度 Acc
            # 数据格式为 - 0x55 0x52 AxL AxH AyL AyH AzL AzH TL TH SUM
            # 加速度
            # xAcc = ((AxH << 8) | AxL) / 32768 * 16 * g (g = 9.8 m/s^2)
            # yAcc = ((AyH << 8) | AyL) / 32768 * 16 * g (g = 9.8 m/s^2)
            # zAcc = ((AzH << 8) | AzL) / 32768 * 16 * g (g = 9.8 m/s^2)
            # 温度
            # temp = ((TH << 8) | TL) / 100 ℃
            # 校验和
            # SUM = 0x55 + 0x51 + AxL + AxH + AyL + AyH + AzL + AzH + TL + TH
            XAcc = self.complement_compute(packet[4:8]) / 32768 * 16
            YAcc = self.complement_compute(packet[8:12]) / 32768 * 16
            ZAcc = self.complement_compute(packet[12:16]) / 32768 * 16
            Temp = self.complement_compute(packet[16:20]) / 100
            SUM = int(packet[20:22], 16)
            # print("XAcc: %f, YAcc: %f, ZAcc: %f, Temp: %f, SUM: %f\n" %
                #   (XAcc, YAcc, ZAcc, Temp, SUM))
            self.Acc_list.append([XAcc, YAcc, ZAcc])
            self.T_list.append(Temp)
            return str("XAcc: %f, YAcc: %f, ZAcc: %f, Temp: %f, SUM: %f\n" % (XAcc, YAcc, ZAcc, Temp, SUM))
            # if SUM == 0x55 + 0x51 + int(packet[4:20], 16):
            # print("XAcc: %f, YAcc: %f, ZAcc: %f, Temp: %f" % (XAcc, YAcc, ZAcc, Temp))

        elif code == "52":
            # self.print_packet(packet)
            # 角速度 Gyro
            # 数据格式为 - 0x55 0x52 wxL wxH wyL wyH wzL wzH TL TH SUM
            # 角速度
            # xGyro = ((wxH << 8) | wxL) / 32768 * 2000 °/s
            # yGyro = ((wyH << 8) | wyL) / 32768 * 2000 °/s
            # zGyro = ((wzH << 8) | wzL) / 32768 * 2000 °/s
            # 温度
            # temp = ((TH << 8) | TL) / 100 ℃
            # 校验和
            # SUM = 0x55 + 0x52 + wxL + wxH + wyL + wyH + wzL + wzH + TL + TH
            XGyro = self.complement_compute(packet[4:8]) / 32768 * 2000
            YGyro = self.complement_compute(packet[8:12]) / 32768 * 2000
            ZGyro = self.complement_compute(packet[12:16]) / 32768 * 2000
            Temp = self.complement_compute(packet[16:20]) / 100
            SUM = int(packet[20:22], 16)
            self.Gyro_list.append([XGyro, YGyro, ZGyro])
            self.T_list.append(Temp)
            # print("XGyro: %f, YGyro: %f, ZGyro: %f, Temp: %f, SUM: %f\n" %
            #       (XGyro, YGyro, ZGyro, Temp, SUM))
            return str("XGyro: %f, YGyro: %f, ZGyro: %f, Temp: %f, SUM: %f\n" % (XGyro, YGyro, ZGyro, Temp, SUM))
            # if SUM == 0x55 + 0x52 + int(packet[4:20], 16):
            #     print("XGyro: %f, YGyro: %f, ZGyro: %f, Temp: %f" % (XGyro, YGyro, ZGyro, Temp))

        elif code == "53":
            # self.print_packet(packet)
            # 角度 Ang
            # 数据格式为 - 0x55 0x53 RollL RollH PitchL PitchH YawL YawH VL VH SUM
            # 角度
            # 滚转角(x轴) Roll = ((RollH << 8) | RollL) / 32768 * 180 °
            # 俯仰角(y轴) Pitch = ((PitchH << 8) | PitchL) / 32768 * 180 °
            # 偏航角(z轴) Yaw = ((YawH << 8) | YawL) / 32768 * 180 °
            # 固件版本
            # Version = VH << 8 | VL
            # 校验和
            # SUM = 0x55 + 0x53 + RollL + RollH + PitchL + PitchH + YawL + YawH + VL + VH
            Roll = self.complement_compute(packet[4:8]) / 32768 * 180
            Pitch = self.complement_compute(packet[8:12]) / 32768 * 180
            Yaw = self.complement_compute(packet[12:16]) / 32768 * 180
            Version = int(packet[16:20], 16)
            SUM = int(packet[20:22], 16)
            self.Angle_list.append([Roll, Pitch, Yaw])
            # print("Roll: %f, Pitch: %f, Yaw: %f, Version: %d, SUM: %f\n" %
            #       (Roll, Pitch, Yaw, Version, SUM))
            return str("Roll: %f, Pitch: %f, Yaw: %f, Version: %d, SUM: %f\n" % (Roll, Pitch, Yaw, Version, SUM))
            # if SUM == 0x55 + 0x53 + int(packet[4:20], 16):
            #     print("Roll: %f, Pitch: %f, Yaw: %f, Version: %d" % (Roll, Pitch, Yaw, Version))

        elif code == "54":
            # self.print_packet(packet)
            # 磁场 Mag
            # 数据格式为 - 0x55 0x54 HxL HxH HyL HyH HzL HzH TL TH SUM
            # 磁场
            # Hx = ((HxH << 8) | HxL)
            # Hy = ((HyH << 8) | HyL)
            # Hz = ((HzH << 8) | HzL)
            # 温度
            # temp = ((TH << 8) | TL) / 100 ℃
            # 校验和
            # SUM = 0x55 + 0x54 + HxL + HxH + HyL + HyH + HzL + HzH + TL + TH
            Hx = self.complement_compute(packet[4:8]) / 1000
            Hy = self.complement_compute(packet[8:12]) / 1000
            Hz = self.complement_compute(packet[12:16]) / 1000
            Temp = self.complement_compute(packet[16:20]) / 100
            SUM = int(packet[20:22], 16)
            self.Mag_list.append([Hx, Hy, Hz])
            self.T_list.append(Temp)
            # print("Hx: %d, Hy: %d, Hz: %d, Temp: %f, SUM: %f\n" %
            #       (Hx, Hy, Hz, Temp, SUM))
            return str("Hx: %d, Hy: %d, Hz: %d, Temp: %f, SUM: %f\n" % (Hx, Hy, Hz, Temp, SUM))
            # if SUM == 0x55 + 0x54 + int(packet[4:20], 16):
            #     print("Hx: %d, Hy: %d, Hz: %d, Temp: %f" % (Hx, Hy, Hz, Temp))

        else:
            ...

    def decode_p(self, recive:str) -> dict:
        ''' 解析气压数据
        
        将得到的气压数据根据包头(0xAA)分段, 并解析成字典格式，方便后续处理

        Args:
        ----------
            recive (str): 接收的数据
        
        Returns:
        ----------
            dict: 解析后的数据
        '''
        self.str_show = ""
        self.P_list = []
        # 剩余数据追加到头部
        recive = self.remain + recive
        # 按包头分段
        num = 0
        while len(recive) >= 70:
            # 检查包头
            if recive[0:4] != "aa01":
                # 找到包头
                recive = recive[2:]
                continue
            # 提取数据包
            packet = recive[0:70]
            recive = recive[70:]
            # 解析数据包
            try:
                num += 1
                self.str_show += self.decode_packet_p(packet) + "\n"
            except:
                # 数据包解析错误
                print("压力传感器数据包解析错误 ", sys.exc_info()[0])
        return [self.str_show, self.P_list]

    def decode_packet_p(self, packet: str) -> str:
        ''' 解析压力传感器数据包

        数据包头为 0xaa 0x01, 分别为 帧头+数据包编号
        B1     B2        B3       B4     ( B5  ~  B32 )   B35
        AA     01        XX       XX     ( ...    ... )    XX
        帧头 数据包编号 点1高八位 点1第八位 点?高八位 点?第八位 校验和

        Args:
        ----------
            packet (str): 数据包
        
        Returns:
        ----------
            str: 解析后的字符串
        '''
        data_list = []
        point = 1
        str_show = ""
        for i in range(4, 68, 4):
            p0 = int(packet[i:i+2], 16) * 256 + int(packet[i+2:i+4], 16)
            data_list.append(p0)
            str_show += "P %2d:%4d; " % (point, p0)
            point += 1
        self.P_list.append(data_list)
        return str_show

    def print_packet(self, packet: str):
        '''以十六进制打印数据包
        AABBCC ===> AA BB CC

        Args:
        ----------
            packet (str): 数据包
        '''
        print(" ".join([packet[i:i+2] for i in range(0, len(packet), 2)]))

    def complement_compute(self, hex_str):
        '''计算大端存储补码的十进制数
        0x8000 - 0xFFFF 为负数
        0x0000 - 0x7FFF 为正数

        Args:
        ----------
            hex_str (str): 十六进制字符串
        
        Returns:
        ----------
            num (int): 十进制数
        '''
        num = int(hex_str[2:4] + hex_str[0:2], 16)
        if num & 0x8000:
            num -= 0x10000
        return num

class ReadThread(QtCore.QThread):
    '''数据读取线程'''
    hex_signal = QtCore.pyqtSignal(str) # 十六进制信号
    str_signal = QtCore.pyqtSignal(str) # 字符串信号
    data_signal = QtCore.pyqtSignal(str, list) # 数据信号
    pd = PacketDecode()

    def __init__(self, key: str, ser: serial.Serial, mainWin: QMainWindow) -> None:
        '''初始化线程

        Args:
        ----------
            ser (serial.Serial): 串口对象
        '''
        super().__init__()
        self.key = key
        self.ser = ser
        self.mainWin = mainWin
        self.isRunning = True

    def __del__(self):
        self.isRunning = False

    def run(self):
        while self.isRunning:
            if self.ser != None and self.ser.in_waiting >= 280:
                recive = self.ser.read(self.ser.in_waiting) # 读取串口数据
                if self.key != "H":
                    # bytes转化为十六进制字符串
                    recive = bytes(recive).hex()
                    str_recive, data_recive = self.pd.decode_imu(recive) # 解析数据包
                    str_recive = datetime.datetime.now().strftime("\n\n%Y-%m-%d %H:%M:%S:\n") + str_recive # 时间戳 + 字符串描述
                    # print(self.pd.decode(recive))
                    # 在行首添加时间戳
                    recive = datetime.datetime.now().strftime("\n\n%Y-%m-%d %H:%M:%S:\n") + recive
                    self.hex_signal.emit(recive)
                    self.str_signal.emit(str_recive)
                    self.data_signal.emit(self.key, data_recive)
                else:
                    recive = recive.hex()
                    str_recive, data_recive = self.pd.decode_p(recive)
                    str_recive = datetime.datetime.now().strftime("\n\n%Y-%m-%d %H:%M:%S:\n") + str_recive  # 时间戳 + 字符串描述
                    self.hex_signal.emit(recive)
                    self.str_signal.emit(str_recive)
                    self.data_signal.emit(self.key, data_recive)

class UpdateThread(QtCore.QThread):

    def __init__(self, mainWin: QApplication , key: str ,component: dict) -> None:
        super().__init__()
        self.mainWin = mainWin
        self.key = key
        self.component = component
        self.isRunning = True
        self.isUpdate = False
        self.imu_key_list = ["Acc", "Gyr", "Angle", "Mag", "T"]
        self.data = []
    
    def __del__(self):
        self.isRunning = False
    
    def update_data(self, data: list):
        self.data = data
        self.isUpdate = True

    def run(self):
        while self.isRunning:
            if self.isUpdate:
                try:
                    if self.key == "H":
                        self.update_presure_component()
                        ...
                    else:
                        self.update_imu_component()
                except:
                    print(self.data)
                    print("更新失败")
                self.isUpdate = False
            time.sleep(0.01)
    
    def update_presure_component(self):
        data = self.data[-1]
        for i in range(16):
            p = self.component["Pressure"][i]
            p.setText(str(data[i]))
            color = data[i] / 2000 * 255
            print(color)
            # 设置p的透明度为50%
            # p.setStyleSheet("background-color: rgba(255, 0, 0, %.1f);" % color)
            # palette = self.et_print.palette()
            # palette.setColor(QPalette.Base, QColor(255, 0, 0, 255))
            # self.et_print.setPalette(palette)

    def update_imu_component(self):
        Acc, Gyr, Angle, Mag, T = self.data
        for key in self.imu_key_list:
            if key == "T":
                self.component[key][0].setText(str(T[-1])+" ℃")
                ...
            elif key == "Acc":
                self.component[key][0].setText("X: %.2f ×g" % float(Acc[-1][0]))
                self.component[key][1].setText("Y: %.2f ×g" % float(Acc[-1][1]))
                self.component[key][2].setText("Z: %.2f ×g" % float(Acc[-1][2]))
            elif key == "Gyr":
                self.component[key][0].setText("X: %.2f °/s" % float(Gyr[-1][0]))
                self.component[key][1].setText("Y: %.2f °/s" % float(Gyr[-1][1]))
                self.component[key][2].setText("Z: %.2f °/s" % float(Gyr[-1][2]))
            elif key == "Angle":
                self.component[key][0].setText("X: %.2f °" % float(Angle[-1][0]))
                self.component[key][1].setText("Y: %.2f °" % float(Angle[-1][1]))
                self.component[key][2].setText("Z: %.2f °" % float(Angle[-1][2]))
            elif key == "Mag":
                self.component[key][0].setText("X: %.2f uT" % float(Mag[-1][0]))
                self.component[key][1].setText("Y: %.2f uT" % float(Mag[-1][1]))
                self.component[key][2].setText("Z: %.2f uT" % float(Mag[-1][2]))
                ...

class IMU(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = uic.loadUi("./ui/sensors.ui", self)
        self.initValues()
        self.initUI()
        self.initComponentDict()
    
    def initValues(self):
        self.ser = {} # 串口对象
        self.read_thread = {} # 读取线程
        self.update_thread = {} # 更新线程
        self.port_open_list = []
    
    def initUI(self):
        self.port_list_Init()   # 初始化串口列表
        self.cb_baudrate.addItems(["9600", "115200", "230400", "460800", "921600"]) # 初始化波特率列表
        # 美化文本框 et_print
        self.et_print.append("欢迎使用 IMU & 压力 传感器测试工具！\n\n")
        self.cb = QComboBox(self)
        self.cb.addItems(["Hex", "Str"])

        # 绑定按钮事件
        self.btn_start.clicked.connect(self.btn_start_clicked)
        self.btn_start_all.clicked.connect(self.btn_start_all_clicked)
        self.btn_stop.clicked.connect(self.btn_stop_clicked)
        self.btn_print.clicked.connect(self.btn_print_clicked)
        self.btn_pause.clicked.connect(self.btn_pause_clicked)
        self.btn_port_all.clicked.connect(self.btn_port_all_clicked)
    
    def initComponentDict(self):
        # 将组件打包成字典，供线程调用
        # 组件包括 A,B,C 三个部分
        # 每个部分分别包括 ACC、GYR、MAG、ANGLE、T 五个部分
        self.component = {
            "A": {
                "Acc": [self.lb_A_XAcc, self.lb_A_YAcc, self.lb_A_ZAcc],  # 加速度
                "Gyr": [self.lb_A_XGyro, self.lb_A_YGyro, self.lb_A_ZGyro],  # 角速度
                "Angle": [self.lb_A_Roll, self.lb_A_Pitch, self.lb_A_Yaw],    # 角度
                "Mag": [self.lb_A_Hx, self.lb_A_Hy, self.lb_A_Hz],  # 磁场
                "T": [self.lb_A_Temperature]    # 温度
            },
            "B": {
                "Acc": [self.lb_B_XAcc, self.lb_B_YAcc, self.lb_B_ZAcc],    # 加速度
                "Gyr": [self.lb_B_XGyro, self.lb_B_YGyro, self.lb_B_ZGyro],  # 角速度
                "Angle": [self.lb_B_Roll, self.lb_B_Pitch, self.lb_B_Yaw],   # 角度
                "Mag": [self.lb_B_Hx, self.lb_B_Hy, self.lb_B_Hz],  # 磁场
                "T": [self.lb_B_Temperature]    # 温度
            },
            "C": {
                "Acc": [self.lb_C_XAcc, self.lb_C_YAcc, self.lb_C_ZAcc],    # 加速度
                "Gyr": [self.lb_C_XGyro, self.lb_C_YGyro, self.lb_C_ZGyro],  # 角速度
                "Angle": [self.lb_C_Roll, self.lb_C_Pitch, self.lb_C_Yaw],   # 角度
                "Mag": [self.lb_C_Hx, self.lb_C_Hy, self.lb_C_Hz],  # 磁场
                "T": [self.lb_C_Temperature]    # 温度
            },
            "H": {
                # 从 p_1 到 p_16
                "Pressure": [self.lb_p_1, self.lb_p_2, self.lb_p_3, self.lb_p_4,
                             self.lb_p_5, self.lb_p_6, self.lb_p_7, self.lb_p_8,
                             self.lb_p_9, self.lb_p_10, self.lb_p_11, self.lb_p_12,
                             self.lb_p_13, self.lb_p_14, self.lb_p_15, self.lb_p_16]
            }
        }
    
    def port_list_Init(self, mode="identify"):
        '''初始化串口列表
        根据所选模式(all-所有串口/identify-设置所需串口)初始化串口列表

        Args:
        ----------
            mode (str): 模式
        '''
        self.port_list = serial.tools.list_ports.comports()
        self.port_list.sort()   # 按照串口名排序
        self.cb_port.clear()
        if mode == "identify":
            for port in self.port_list:
                if port.description.find("WCH USB-SERIAL Ch") != -1:
                    if port.description.split(" ")[-2] in ["A", "B", "C"]:
                        self.cb_port.addItem(str(port.name) + " IMU "+ port.description.split(" ")[-2])
                        ...
                    if port.description.split(" ")[-2] in ["H"]:
                        self.cb_port.addItem(str(port.name) + " Pressure "+ port.description.split(" ")[-2])
            ...
        else:
            for port in self.port_list:
                self.cb_port.addItem(str(port))
        ...

    def btn_port_all_clicked(self):
        if self.btn_port_all.text() == "show all":
            self.port_list_Init("all")
            self.btn_port_all.setText("show identify")
        else:
            self.port_list_Init("identify")
            self.btn_port_all.setText("show all")
        ...

    def btn_start_clicked(self):
        '''打开串口'''
        current_port = self.cb_port.currentText()  # 获取当前串口
        current_port_com = self.cb_port.currentText().split(" ")[0]  # 获取当前串口
        current_port_num = self.cb_port.currentText().split(" ")[-1]  # 获取当前串口编号
        # 判断当前串口是否已经打开
        if current_port_num in self.port_open_list:
            print(current_port, "-> already open")
            print(self.ser[current_port_num].in_waiting, "-> in_waiting")
            return
        
        # 判断当前串口是否为 A、B、C 串口
        elif current_port_num in ["A", "B", "C", "H"]:
            try:
                self.port_open_list.append(current_port_num)
                if current_port_num == "H":
                    self.ser[current_port_num] = serial.Serial(current_port_com, 115200)
                else:
                    self.ser[current_port_num] = serial.Serial(current_port_com, int(self.cb_baudrate.currentText()))
                self.ser[current_port_num].flushInput()
                print(current_port, "-> open success")
            except (OSError, serial.SerialException):
                print(current_port, "-> open failed")
                ...
            return

        else:
            print("please select A, B or C for IMU, or H for Pressure!")
            return


        # if self.ser is None:
        #     print("start")
        #     try:
        #         self.ser = serial.Serial(self.cb_port.currentText().split(" ")[0], int(self.cb_baudrate.currentText()))
        #         self.ser.flushInput()
        #     except (OSError, serial.SerialException):
        #         print(self.cb_port.currentText(), "-> open failed")
        #         ...
        # else:
        #     print(self.ser.name, "-> already open")
        #     print(self.ser.in_waiting, "-> in_waiting")
    
    def btn_start_all_clicked(self):
        '''打开所有串口'''
        # 通过cb_port中的串口名，打开串口
        for i in range(self.cb_port.count()):
            self.cb_port.setCurrentIndex(i)
            self.btn_start_clicked()
        ...

    def btn_stop_clicked(self):
        '''关闭串口'''
        try:
            self.btn_pause_clicked()
        except:
            ...
        print(self.ser.keys())
        for key in self.ser.keys():
            if self.ser[key] != None and self.ser[key].is_open:
                print("IMU " + key + " stop")
                self.port_open_list.remove(key)
                self.ser[key].close()
                self.ser[key] = None
                # print("IMU " + key + " stop")
            else:
                print("IMU " + key + " not start")
        self.ser = {}
        # for ser in self.ser:
        #     if ser != None and ser.is_open:
        #         ser.close()
        #         ser = None
        #         print("stop")
        #     else:
        #         print("not start")
        # if self.ser != None and self.ser.is_open:
        #     self.ser.close()
        #     self.ser = None
        #     print("stop")
        # else:
        #     print("not start")
    
    def btn_print_clicked(self):
        '''打印串口数据'''
        # 根据串口列表创建现成并启动
        print(self.read_thread.keys())
        for key in self.ser.keys():
            if self.ser[key] != None and self.ser[key].is_open and key not in self.read_thread.keys():
                print(key)
                self.read_thread[key] = ReadThread(key, self.ser[key], self)
                self.read_thread[key].hex_signal.connect(self.et_print_Update)
                # self.read_thread[key].str_signal.connect(self.et_show_Update)
                # data_sinal 与 data_update 信号连接, 且同时传递key值
                # self.read_thread[key].data_signal.connect(self.data_update)
                self.read_thread[key].start()
                self.read_thread[key].data_signal.connect(self.data_update)
                self.update_thread[key] = UpdateThread(
                    self, key, self.component[key])
                self.update_thread[key].start()
                if key != "H":
                    # self.read_thread[key].data_signal.connect(self.data_update)
                    # self.update_thread[key] = UpdateThread(self, key, self.component[key])
                    # self.update_thread[key].start()
                    ...
                else:
                    self.read_thread[key].str_signal.connect(self.et_show_Update)
            else:
                print(key, "-> not start")

        # if self.read_thread == None:
        #     self.read_thread = ReadThread(self.ser, self)
        #     self.read_thread.hex_signal.connect(self.et_print_Update)
        #     self.read_thread.str_signal.connect(self.et_show_Update)
        #     self.read_thread.data_signal.connect(self.data_update)
        #     self.read_thread.start()
        #     self.update_thread = UpdateThread(self, self.component["A"])
        #     self.update_thread.start()
        # else:
        #     print('already start')
    
    def btn_pause_clicked(self):
        '''暂停打印串口数据'''
        for key in self.ser.keys():
            self.read_thread[key].isRunning = False
            self.read_thread[key].quit()
            self.read_thread[key].wait()
            if key != "H":
                self.update_thread[key].isRunning = False
                self.update_thread[key].quit()
                self.update_thread[key].wait()
        self.read_thread = {}
        self.update_thread = {}

        # self.read_thread.isRunning = False
        # self.read_thread.quit()
        # self.read_thread.wait()
        # self.update_thread.isRunning = False
        # self.update_thread.quit()
        # self.update_thread.wait()
        # self.read_thread = None
        # self.read_thread = None
    
    def et_print_Update(self, recive=None):
        '''更新打印窗口
        
        Args:
        ----------
            recive (str): 串口接收到的数据
        '''
        self.et_print.insertPlainText(recive)
        self.et_print.moveCursor(self.et_print.textCursor().End)
    
    def et_show_Update(self, str_recive=None):
        '''更新显示窗口
        
        Args:
        ----------
            recive (str): 串口接收到的数据
        '''
        self.et_show.insertPlainText(str_recive)
        self.et_show.moveCursor(self.et_show.textCursor().End)

    def data_update(self, key="A", data_recive=None):
        '''更新数据
        
        Args:
        ----------
            recive (str): 串口接收到的数据
        '''
        self.update_thread[key].update_data(data_recive)
        ...

    def closeEvent(self, event):
        try:
            self.read_thread.isRunning = False
            self.read_thread.quit()
            self.read_thread.wait()
            self.read_thread = None
            self.ser.close()
        except:
            ...
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    imu = IMU()
    imu.show()
    sys.exit(app.exec_())
    # str1 = '555178fd4e0385f8fc0ef35552000000000000690b1b'
    # str2 = '55530cc6f1f60d0603017855547102e4122108690baf555186ff0af862006b0b0555520000000000006b0b1d55530cc6f1f60d0603017855546b02e71233086b0bc0555186ff09f86000680bff5552000000000000680b1a55530cc6f1f60d0603017855546f02e3122608680bb0555186ff0af86100670b005552000000000000670b1955530cc6f1f60d0603017855547a02e9122608670bc0555185ff0af86100670bff5552000000000000670b1955530cc6f1f60d0603017855547802e9122208670bba555186ff0af86200690b03555200'
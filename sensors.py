import sys
import datetime
import os
import time
import traceback
import numpy as np
from PyQt5 import QtCore
import serial
import serial.tools.list_ports
# ui_model
from ui.sensor_info_ui.SensorInfo import SensorInfo
from ui.sensor_print_ui.SensorPrint import SensorPrint
from ui.sensor_info_list_ui.SensorInfoList import SensorInfoList
from ui.canvas_ui.Canvas import CanvasWidget
from ui.setting_ui.Setting import SettingWidget
# PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QOpenGLWidget
import pyqtgraph.opengl as gl
import pyqtgraph as pg
# QAction
from PyQt5.QtWidgets import QAction
from scipy.interpolate import interp2d
# cv2
import cv2


class PacketDecode:
    """数据包解析
    根据串口关键字类型, 解析串口数据包

    Args:
    ----------------
        key(str): 串口关键字类型, "A" "B" "C" 为IMU, "H" 为Pressure
    """

    def __init__(self, key: str) -> None:
        self.key = key  # 串口关键字类型
        # 字符串部分
        self.remain = ""  # 保存上一次解析的数据包的剩余部分
        self.str_show = ""  # 保存解析后的数据(文本描述)
        # IMU
        self.Acc_list = []  # 保存解析后的加速度数据
        self.Gyro_list = []  # 保存解析后的角速度数据
        self.Angle_list = []  # 保存解析后的角度数据
        self.Mag_list = []  # 保存解析后的磁场数据
        self.T_list = []  # 保存解析后的温度数据
        # 压力传感器
        self.P_list = []  # 保存解析后的压力数据
        ...

    def decode(self, receive: str) -> list:
        """ 解析数据
        """
        if self.key == "H":
            return self.decode_p(receive)
        else:
            return self.decode_imu(receive)

    def decode_imu(self, receive: str) -> list:
        """ 解析 IMU 数据

        将接收到的数据根据包头(0x55)进行分段, 然后解析数据包

        Args:
        ----------------
            receive(str): 接收到的数据

        Returns:
        ----------------
            str_show(str): 解析后的数据
        """
        self.str_show = ""
        self.Acc_list = []
        self.Gyro_list = []
        self.Angle_list = []
        self.Mag_list = []
        self.T_list = []
        # 从数据中提取出数据包
        receive = self.remain + receive
        while len(receive) >= 22:
            # 搜索包头
            if receive[0:2] != "55":
                # 找到第一个 '55'
                position = receive.find("55")
                if position == -1:
                    # 没有找到 '55'
                    self.remain = ""
                    return [self.str_show, [self.Acc_list, self.Gyro_list, self.Angle_list, self.Mag_list, self.T_list]]
                else:
                    # 找到了 '55'
                    receive = receive[position:]
                continue
            # 提取数据包
            packet = receive[:22]
            # 解析数据包
            try:
                self.str_show += self.decode_packet_imu(packet)
                receive = receive[22:]
            except:
                # 打印错误信息
                print("IMU 数据包解析错误" + str(packet[:22]))
                receive = receive[2:]

        if len(receive) < 22:
            self.remain = receive
        return [self.str_show, [self.Acc_list, self.Gyro_list, self.Angle_list, self.Mag_list, self.T_list]]

    def decode_packet_imu(self, packet) -> str:
        """ 解析 IMU 数据包

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
        """
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
            self.Acc_list.append([XAcc, YAcc, ZAcc])
            self.T_list.append(Temp)
            return str("XAcc: %f, YAcc: %f, ZAcc: %f, Temp: %f, SUM: %f\n" % (XAcc, YAcc, ZAcc, Temp, SUM))

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
            return str("XGyro: %f, YGyro: %f, ZGyro: %f, Temp: %f, SUM: %f\n" % (XGyro, YGyro, ZGyro, Temp, SUM))

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
            return str("Roll: %f, Pitch: %f, Yaw: %f, Version: %d, SUM: %f\n" % (Roll, Pitch, Yaw, Version, SUM))

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
            return str("Hx: %d, Hy: %d, Hz: %d, Temp: %f, SUM: %f\n" % (Hx, Hy, Hz, Temp, SUM))

        elif code == "5f":
            print(packet)
            return "1" + str(packet)

        else:
            # 数据包类型错误
            ...

    def decode_p(self, receive: str) -> list:
        """ 解析气压数据

        将得到的气压数据根据包头(0xAA)分段, 并解析成字典格式，方便后续处理

        Args:
        ----------
            receive (str): 接收的数据
        
        Returns:
        ----------
            dict: 解析后的数据
        """
        self.str_show = ""  # 显示的字符串
        self.P_list = []  # 气压数据
        # 剩余数据追加到头部
        receive = self.remain + receive
        # 按包头分段
        while len(receive) >= 70:
            # 检查包头
            if receive[0:4] != "aa01":
                # 找到包头
                receive = receive[2:]
                continue
            # 提取数据包
            packet = receive[0:70]
            receive = receive[70:]
            # 解析数据包
            try:
                self.str_show += self.decode_packet_p(packet) + "\n"
            except:
                # 数据包解析错误
                print("压力传感器数据包解析错误 ", sys.exc_info()[0])
        return [self.str_show, self.P_list]

    def decode_packet_p(self, packet: str) -> str:
        """ 解析压力传感器数据包

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
        """
        data_list = []
        point = 1
        str_show = ""
        for i in range(4, 68, 4):
            p0 = int(packet[i:i + 2], 16) * 256 + int(packet[i + 2:i + 4], 16)
            data_list.append(p0)
            str_show += "P %2d:%4d; " % (point, p0)
            point += 1
        self.P_list.append(data_list)
        return str_show

    @staticmethod
    def print_packet(packet: str) -> None:
        """以十六进制打印数据包
        AABBCC ===> AA BB CC

        Args:
        ----------
            packet (str): 数据包
        """
        print(" ".join([packet[i:i + 2] for i in range(0, len(packet), 2)]))

    @staticmethod
    def complement_compute(hex_str) -> int:
        """计算大端存储补码的十进制数
        0x8000 - 0xFFFF 为负数
        0x0000 - 0x7FFF 为正数

        Args:
        ----------
            hex_str (str): 十六进制字符串
        
        Returns:
        ----------
            num (int): 十进制数
        """
        num = int(hex_str[2:4] + hex_str[0:2], 16)
        if num & 0x8000:
            num -= 0x10000
        return num


class ReadThread(QtCore.QThread):
    """数据读取线程
    根据串口对象读取数据，并解析成字符串、十六进制、数据三种格式

    Args:
    ----------
        key (str): 串口关键字 -> ["A", "B", "C", "H"]
        ser (serial.Serial): 串口对象
        mainWin (QMainWindow): 主窗口对象

    Signals:
    ----------
        hex_signal (str): 十六进制信号
        str_signal (str): 字符串信号
        data_signal (str, list): 数据信号 -> (串口关键字, 数据列表)
    """
    hex_signal = QtCore.pyqtSignal(str, str)  # 十六进制信号
    str_signal = QtCore.pyqtSignal(str, str)  # 字符串信号
    data_signal = QtCore.pyqtSignal(str, list)  # 数据信号

    def __init__(self, key: str, ser: serial.Serial, mainWin: QMainWindow) -> None:
        """初始化线程

        Args:
        ----------
            ser (serial.Serial): 串口对象
        """
        super().__init__()
        self.key = key  # 串口关键字 -> ["A", "B", "C", "H"]
        self.ser = ser  # 串口对象 -> serial.Serial
        self.mainWin = mainWin  # 主窗口对象 -> QMainWindow
        self.pd = PacketDecode(self.key)  # 数据解析对象
        self.isRunning = True  # 线程运行标志位
        self.write_flag = False  # 写入标志位
        self.instruction = ""  # 写入指令

    def __del__(self):
        self.isRunning = False
    
    def write_sensor(self, instruction: str) -> None:
        """写入数据

        Args:
        ----------
            data (str): 写入的数据
        """
        self.instruction = instruction
        self.write_flag = True
    
    def write_to_sensor(self, instruction: str) -> None:
        """写入十六进制数据

        Args:
        ----------
            data (str): 写入的数据
        """
        dict =  {'unlock': 'ffaa6988b5',
                    'sleep': 'ffaa220100',
                    'save': 'ffaa000000', 'restart':'ffaa00ff00', 'reset':'ffaa000100',
                    'led_off':'ffaa1b0100', 'led_on':'ffaa1b0000',
                    'acc':'ffaa270200', 'gyr':'ffaa275500', 'angle':'ffaa276100', 'mag':'ffaa276100', 'temp':'ffaa00',
                    'z_0':'ffaa010400', 'angle_0':'ffaa010800',
                    'horizontal':'ffaa230000', 'vertical':'ffaa230100',
                    'algorithm_9':'ffaa240000', 'algorithm_6':'ffaa240100'}
        # 解锁
        self.ser.write(bytes.fromhex(dict["unlock"]))
        self.msleep(100)
        self.ser.write(bytes.fromhex(dict[instruction]))
        self.msleep(100)
        self.ser.write(bytes.fromhex(dict["save"]))
        self.msleep(100)

    def run(self):
        while self.isRunning:
            if self.write_flag:
                self.write_to_sensor(self.instruction)
                self.write_flag = False
                self.ser.flushInput()  # 清空缓冲区
                continue
            if self.ser is not None and self.ser.in_waiting >= 280:
                receive = self.ser.read(self.ser.in_waiting)  # 读取串口数据
                # bytes转化为十六进制字符串
                receive = receive.hex()
                str_receive, data_receive = self.pd.decode(receive)  # 解析数据包
                str_receive = datetime.datetime.now().strftime("\n\n%Y-%m-%d %H:%M:%S:\n") + str_receive  # 时间戳 + 字符串描述
                # 在行首添加时间戳
                receive = datetime.datetime.now().strftime("\n\n%Y-%m-%d %H:%M:%S:\n") + receive
                self.hex_signal.emit(self.key, receive)
                self.str_signal.emit(self.key, str_receive)
                self.data_signal.emit(self.key, data_receive)
            self.msleep(10)


class UpdateThread(QtCore.QThread):
    """数据更新线程
    用于更新 SensorInfo 数据

    Args:
    ----------
        sensorinfo (SensorInfo): 传感器信息对象
    """

    def __init__(self, sensorinfo: SensorInfo) -> None:
        super().__init__()
        self.sensorinfo = sensorinfo
        self.isRunning = True
        self.isUpdate = False
        self.imu_key_list = ["Acc", "Gyr", "Angle", "Mag", "T"]  # IMU数据关键字
        self.data = []

    def __del__(self):
        self.isRunning = False

    def update_data(self, data: list):
        """ 数据更新线程 -> 更新数据

        Args:
        ----------
            data (list): 数据列表 -> {"A" "B" "C": [Acc, Gyr, Angle, Mag, T], "H": [16 x data]}
        """
        self.data = data
        self.isUpdate = True

    def run(self):
        while self.isRunning:
            if self.isUpdate:
                try:
                    self.sensorinfo.update(self.data)  # 调用 SensorInfo.update() 更新数据
                except Exception as e:
                    # 更新失败 输出更新失败的数据
                    print(self.data)
                    print("更新失败")
                self.isUpdate = False
            self.msleep(100)  # 10ms更新一次


class UpdateCanvasThread(QtCore.QThread):
    def __init__(self, key: str, canvas: None):
        super().__init__()
        self.key = key
        self.canvas = canvas
        self.isRunning = True
        self.isUpdate = False
        self.data = []
    
    def __del__(self):
        self.isRunning = False
    
    def update_data(self, data: list):
        if self.data != []:
            self.data += data
        else:
            self.data = data
        self.isUpdate = True

    def run(self):
        while self.isRunning:
            if self.isUpdate:
                data = self.data
                self.data = []
                self.canvas.update(data)
                self.isUpdate = False
            self.msleep(100)
    

# 使用线程保存数据
class SaveThread(QtCore.QThread):
    """数据保存线程
        用于保存数据, 线程创建时创建对应文件
    Args:
    ----------
        key (str): 串口关键字 -> ["A", "B", "C", "H"]
    """

    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = key
        self.isRunning = True
        self.data = np.array([])
        self.Acc = np.array([])
        self.Gyr = np.array([])
        self.Angle = np.array([])
        self.Mag = np.array([])
        self.T = np.array([])
        self.file_path = ""
        self.save_create()

    def __del__(self):
        self.isRunning = False

    def save_create(self):
        """ 数据保存线程 -> 创建文件
            文件存储路径为当前目录下的data文件夹
            文件名为: 年-月-日 时-分-秒_串口关键字.txt
        """
        dir_path = os.getcwd() + "\\data"
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        if self.key == "H":
            filename = datetime.datetime.now().strftime("\\%Y-%m-%d %H-%M-%S") + "_Pressure.txt"
        else:
            filename = datetime.datetime.now().strftime("\\%Y-%m-%d %H-%M-%S") + "_IMU_" + self.key + ".txt"
        self.file_path = dir_path + filename
        try:
            with open(self.file_path, "a") as f:
                print(filename + "创建文件成功")
        except:
            print(filename + "创建文件失败")

    def update_data(self, data: list):
        """数据保存线程 -> 更新数据

        Args:
        ----------
            data (list): 数据列表 -> {"A" "B" "C": [Acc, Gyr, Angle, Mag, T], "H": [16 x data]}
        """
        if self.key == "H":
            if self.data.shape[0] == 0:
                self.data = np.array(data)
            else:
                self.data = np.append(self.data, data)
        else:
            Acc, Gyr, Angle, Mag, T = data
            T = T[::4]
            length = min(len(Acc), len(Gyr), len(Angle), len(Mag), len(T))
            data = np.hstack(
                (Acc[:length], Gyr[:length], Angle[:length], Mag[:length], np.array(T[:length]).reshape(-1, 1)))
            if self.data.shape[0] == 0:
                self.data = data
            else:
                self.data = np.vstack([self.data, data])

    def run(self):
        while self.isRunning:
            if self.data.shape[0] != 0:
                try:
                    data = self.data
                    # 保存数据
                    with open(self.file_path, "a") as f:
                        if self.key == "H":
                            np.savetxt(f, data, fmt="%d")
                        else:
                            np.savetxt(f, data, fmt="%f")
                    self.data = np.array([])
                except Exception as e:
                    print("保存失败" + str(e))
            self.msleep(100)  # 10ms保存一次


class IMU(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = uic.loadUi("./ui/sensors.ui", self)
        self.initValues()
        self.initUI()

    def initValues(self) -> None:
        self.sensorInfo_list = {}  # 传感器数据 显示 字典
        self.sensorInfoList_list = {}  # 传感器数据列表 显示 字典
        self.sensorPrint_list = {}  # 传感器原始数据 显示 字典
        self.sensorCanvas_list = {}  # 传感器图表 显示 字典
        self.ser = {}  # 串口对象字典
        self.read_thread = {}  # 读取线程字典
        self.update_thread = {}  # 更新线程字典
        self.save_thread = {}  # 保存线程字典
        self.canvas_thread = {} # 画布更新线程字典
        self.port_open_list = []
        self.current_tab = self.tabWidget.currentIndex()  # 当前tab页

    def initUI(self) -> None:
        sensor_key_list = ["A", "B", "C", "H"]
        for key in sensor_key_list:
            self.sensorInfo_list.update({key: SensorInfo(key)})
            self.data_frame.layout().addWidget(self.sensorInfo_list[key])
            self.sensorPrint_list.update({key: SensorPrint(key)})
            self.data_print_frame.layout().addWidget(self.sensorPrint_list[key])
            if key != "H":
                self.sensorCanvas_list.update({key: CanvasWidget(key)})
                self.canvas_frame.layout().addWidget(self.sensorCanvas_list[key])
                # 设置 sensorCanvas 高度为界面的一半
                self.sensorCanvas_list[key].setMinimumHeight(int(self.scrollArea.height() / 2))

        self.tab_data_list_imu_title.layout().addWidget(SensorInfoList("O"))
        self.tab_data_list_p.layout().addWidget(SensorInfo("H"))


        # self.w = gl.GLViewWidget()
        # self.w.setCameraPosition(distance=50)

    #     # z = pg.gaussianFilter(np.random.normal(size=(50, 50)), (1, 1))
    #     # p1 = gl.GLSurfacePlotItem(z=z, shader='shaded', color=(0.5, 0.5, 1, 1))
    #     # p1.scale(16, 16, 16)
    #     # p1.translate(-18, 2, 0)
    #     # 显示网格
    #     g = gl.GLGridItem()
    #     # g.scale(16, 16, 16)
    #     self.w.addItem(g)
    #     # self.w.addItem(p1)
    #     # opengl 给一个二维数组， 根据大小绘制对应的三维热力图
    #     # 二维数组的大小为 4 x 4
    #     # 绘制热力图
    #     input_array = np.array([[1, 2, 3, 4],
    #                    [5, 6, 7, 8],
    #                    [9, 10, 11, 12],
    #                    [13, 14, 15, 16]])

    #     # 创建一个空的9x9数组，并初始化为0
    #     output_array = np.zeros((9, 9))

    #     # 在中间插入输入数组的值
    #     output_array[1:8:2, 1:8:2] = input_array
    #     print(output_array)

    #     # 定义输入数据的网格点
    #     x = np.arange(0, 9)
    #     y = np.arange(0, 9)

    #     # 定义插值后的网格点
    #     new_x = np.linspace(0, 8, 900)
    #     new_y = np.linspace(0, 8, 900)

    #     # 使用二维线性插值进行插值操作
    #     interp = interp2d(x, y, output_array * 10, kind='linear')
    #     output_array = interp(new_x, new_y)
    #     colors = np.ones((50, 50, 4), dtype=float)
    #     p1 = gl.GLSurfacePlotItem(
    #         z=output_array, shader='heightColor', colors=colors.reshape(
    # 50 * 50, 4))
    #     p1.scale(0.01, 0.01, 0.01)
    #     self.w.addItem(p1)

    #     self.tab.layout().addWidget(self.w)

        self.port_list_Init()  # 初始化串口列表
        self.cb_baudrate.addItems(["9600", "115200", "230400", "460800", "921600"])  # 初始化波特率列表

        # 绑定按钮事件
        self.tabWidget.currentChanged.connect(self.tabWidget_currentChanged)
        self.btn_start.clicked.connect(self.btn_start_clicked)
        self.btn_start_all.clicked.connect(self.btn_start_all_clicked)
        self.btn_stop.clicked.connect(self.btn_stop_clicked)
        self.btn_print.clicked.connect(self.btn_print_clicked)
        self.btn_pause.clicked.connect(self.btn_pause_clicked)
        self.btn_port_all.clicked.connect(self.btn_port_all_clicked)
        self.btn_test.clicked.connect(self.btn_test_clicked)
        self.SettingWidget = SettingWidget(self)
        act = QAction("设置", self)
        act.triggered.connect(self.SettingWidget.show)
        self.btn_test_2.clicked.connect(act.trigger)
        
    def setting(self, event):
        if self.sender().accessibleName() == "algorithm":
            self.sender().setText("算法：六轴") if self.sender().whatsThis() == "algorithm_9" else  self.sender().setText("算法：九轴")
            self.sender().setWhatsThis("algorithm_6")if self.sender().whatsThis() == "algorithm_9" else self.sender().setWhatsThis("algorithm_9")
        elif self.sender().accessibleName() == "direction":
            self.sender().setText("安装方向：水平") if self.sender().whatsThis(
            ) == "horizontal" else self.sender().setText("安装方向：垂直")
            self.sender().setWhatsThis("vertical")if self.sender().whatsThis(
            ) == "horizontal" else self.sender().setWhatsThis("horizontal")
        print(self.sender().whatsThis())
        for key in self.read_thread.keys():
            self.read_thread[key].write_sensor(self.sender().whatsThis())
    
    def btn_test_clicked(self) -> None:
        for key in self.ser.keys():
            if self.ser[key] is not None and self.ser[key].is_open:
                print(key)
                dict =  {'unlock': 'ffaa6988b5',
                                'sleep': 'ffaa220100',
                                'save': {'save': 'ffaa000000', 'restart':'ffaa00ff00', 'reset':'ffaa000100'},
                                'led': {'off':'ffaa1b0100', 'on':'ffaa1b0000'},
                                'read': {'test':'ffaa270200', 'gyr':'ffaa275500', 'angle':'ffaa276100', 'mag':'ffaa276100', 'temp':'ffaa00'},
                                'calibrate': {'z':'ffaa010400', 'angle':'ffaa010800'}}
                self.ser[key].write(bytes.fromhex(dict['unlock']))
                time.sleep(0.1)
                self.ser[key].write(bytes.fromhex(dict['calibrate']["angle"]))
                print("sleep")

    def port_list_Init(self, mode="identify") -> None:
        """初始化串口列表
        根据所选模式(all-所有串口/identify-设置所需串口)初始化串口列表

        Args:
        ----------
            mode (str): 模式
        """
        self.port_list = serial.tools.list_ports.comports()
        self.port_list.sort()  # 按照串口名排序
        self.cb_port.clear()
        if mode == "identify":
            for port in self.port_list:
                if port.description.find("WCH USB-SERIAL Ch") != -1:
                    if port.description.split(" ")[-2] in ["A", "B", "C"]:
                        self.cb_port.addItem(str(port.name) + " IMU " + port.description.split(" ")[-2])
                        ...
                    if port.description.split(" ")[-2] in ["H"]:
                        self.cb_port.addItem(str(port.name) + " Pressure " + port.description.split(" ")[-2])
            ...
        else:
            for port in self.port_list:
                self.cb_port.addItem(str(port))
        ...

    def btn_port_all_clicked(self) -> None:
        if self.btn_port_all.text() == "show all":
            self.port_list_Init("all")
            self.btn_port_all.setText("show identify")
        else:
            self.port_list_Init("identify")
            self.btn_port_all.setText("show all")
        ...

    def btn_start_clicked(self) -> None:
        """打开串口"""
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
                # 串口打开失败, 输出 "串口名 -> open failed"
                print(current_port, "-> open failed")
            return

        else:
            print("please select A, B or C for IMU, or H for Pressure!")
            self.ser[current_port_num] = serial.Serial(current_port_com, int(self.cb_baudrate.currentText()))
            return

    def btn_start_all_clicked(self) -> None:
        """打开所有串口"""
        # 通过cb_port中的串口名，打开串口
        for i in range(self.cb_port.count()):
            self.cb_port.setCurrentIndex(i)
            self.btn_start_clicked()

    def btn_stop_clicked(self) -> None:
        """关闭串口"""
        try:
            self.btn_pause_clicked()
        except Exception as e:
            # 打印异常信息
            print(e)
        print(self.ser.keys())
        for key in self.ser.keys():
            if self.ser[key] is not None and self.ser[key].is_open:
                print("IMU " + key + " stop")
                self.port_open_list.remove(key)
                self.ser[key].close()
                self.ser[key] = None
                # print("IMU " + key + " stop")
            else:
                print("IMU " + key + " not start")
        self.ser = {}

    def tabWidget_currentChanged(self, index: int) -> None:
        print("切换到 " + self.tabWidget.tabText(index))
        self.current_tab = index

    def btn_print_clicked(self) -> None:
        """打印串口数据"""
        # 根据串口列表创建现成并启动
        print(self.read_thread.keys())
        for key in self.ser.keys():
            if self.ser[key] is not None and self.ser[key].is_open and key not in self.read_thread.keys() and key in ["A", "B", "C", "H"]:
                print(key)
                self.read_thread[key] = ReadThread(key, self.ser[key], self)
                self.read_thread[key].hex_signal.connect(self.et_print_Update)
                self.read_thread[key].str_signal.connect(self.et_show_Update)
                self.read_thread[key].data_signal.connect(self.data_update)
                self.read_thread[key].start()
                self.update_thread[key] = UpdateThread(self.sensorInfo_list[key])
                self.update_thread[key].start()
                self.save_thread[key] = SaveThread(key)
                self.save_thread[key].start()
                if key != "H":
                    self.canvas_thread[key] = UpdateCanvasThread(key, self.sensorCanvas_list[key])
                    self.canvas_thread[key].start()
            else:
                print(key, "-> not start")

    def btn_pause_clicked(self) -> None:
        """暂停打印串口数据"""
        for key in self.ser.keys():
            self.read_thread[key].__del__()
            self.read_thread[key].quit()
            self.read_thread[key].wait()
            self.update_thread[key].__del__()
            self.update_thread[key].quit()
            self.update_thread[key].wait()
            self.save_thread[key].__del__()
            self.save_thread[key].quit()
            self.save_thread[key].wait()
            self.canvas_thread[key].__del__()
            self.canvas_thread[key].quit()
            self.canvas_thread[key].wait()
        self.read_thread = {}
        self.update_thread = {}
        self.save_thread = {}
        self.canvas_thread = {}

    def et_print_Update(self, key: str = "A", receive: str = None) -> None:
        """更新打印窗口

        Args:
        ----------
            key (str): 串口关键字
            receive (str): 串口接收到的数据
        """
        self.sensorPrint_list[key].update_hex(receive)

    def et_show_Update(self, key: str = "A", str_receive: str = None) -> None:
        """更新显示窗口

        Args:
        ----------
            key (str): 串口关键字
            receive (str): 串口接收到的数据
        """
        self.sensorPrint_list[key].update_str(str_receive)

    def data_update(self, key: str = "A", data_receive=None) -> None:
        """更新数据

        Args:
        ----------
            key (str): 串口关键字
            receive (str): 串口接收到的数据 ->
        """
        try:
            self.update_thread[key].update_data(data_receive)
            self.save_thread[key].update_data(data_receive)
            if key != "H":
                self.canvas_thread[key].update_data(data_receive[2])
        except Exception as e:
            # 打印错误信息
            print(traceback.format_exc())

    def closeEvent(self, event) -> None:
        try:
            self.btn_stop_clicked()
        except Exception as e:
            # 打印错误信息
            print(traceback.format_exc())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    imu = IMU()
    imu.show()
    sys.exit(app.exec_())
    # str1 = '555178fd4e0385f8fc0ef35552000000000000690b1b'
    # str2 = '55530cc6f1f60d0603017855547102e4122108690baf555186ff0af862006b0b0555520000000000006b0b1d55530cc6f1f60d0603017855546b02e71233086b0bc0555186ff09f86000680bff5552000000000000680b1a55530cc6f1f60d0603017855546f02e3122608680bb0555186ff0af86100670b005552000000000000670b1955530cc6f1f60d0603017855547a02e9122608670bc0555185ff0af86100670bff5552000000000000670b1955530cc6f1f60d0603017855547802e9122208670bba555186ff0af86200690b03555200'

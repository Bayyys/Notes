import sys
sys.path.append('./../')
from PyQt5 import QtCore
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QMainWindow
from utils.decode import PacketDecode
import datetime


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
    test_signal = QtCore.pyqtSignal(list)  # 测试信号

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
        self.is_running = True  # 线程运行标志位
        self.write_flag = False  # 写入标志位
        self.instruction = ""  # 写入指令

    def __del__(self):
        self.is_running = False
    
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
        while self.is_running:
            if self.write_flag:
                self.write_to_sensor(self.instruction)
                self.write_flag = False
                self.ser.reset_input_buffer()  # 清空缓冲区
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
                if self.key == 'A':
                    self.test_signal.emit(data_receive[2][-1])
            self.msleep(1)

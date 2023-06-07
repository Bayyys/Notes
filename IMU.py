import sys
import datetime
from PyQt5 import QtCore
import serial
import serial.tools.list_ports

# PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication


class PacketDecode():
    '''数据包解析'''

    def __init__(self) -> None:
        self.remain = ""  # 保存上一次解析的数据包的剩余部分
        self.str_show = ""
        ...

    def decode(self, recive: str) -> dict:
        self.str_show = ""
        # 从数据中提取出数据包
        recive = self.remain + recive
        while len(recive) >= 22:
            # 判断数据包是否完整
            if recive[0:2] != "55":
                # 找到第一个 '55'
                recive = recive[2:]
                if len(recive) < 22:
                    # 数据包不完整
                    self.remain = recive
                    break
                continue
            # 提取数据包
            packet = recive[:22]
            recive = recive[22:]
            # 解析数据包
            try:
                self.str_show += self.decode_packet(packet)
            except:
                # 打印错误信息
                print("Error: ", sys.exc_info()[0])
        if len(recive) < 22:
            self.remain = recive
        return self.str_show

    def decode_packet(self, packet: str):
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
            XAcc = self.compute(packet[4:8]) / 32768 * 16 * 9.8
            YAcc = self.compute(packet[8:12]) / 32768 * 16 * 9.8
            ZAcc = self.compute(packet[12:16]) / 32768 * 16 * 9.8
            Temp = self.compute(packet[18:20]) / 100
            SUM = int(packet[20:22], 16)
            # print("XAcc: %f, YAcc: %f, ZAcc: %f, Temp: %f, SUM: %f\n" %
                #   (XAcc, YAcc, ZAcc, Temp, SUM))
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
            XGyro = self.compute(packet[4:8]) / 32768 * 2000
            YGyro = self.compute(packet[8:12]) / 32768 * 2000
            ZGyro = self.compute(packet[12:16]) / 32768 * 2000
            Temp = self.compute(packet[18:20]) / 100
            SUM = int(packet[20:22], 16)
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
            Roll = self.compute(packet[4:8]) / 32768 * 180
            Pitch = self.compute(packet[8:12]) / 32768 * 180
            Yaw = self.compute(packet[12:16]) / 32768 * 180
            Version = int(packet[16:18], 16)
            SUM = int(packet[18:20], 16)
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
            Hx = self.compute(packet[4:8])
            Hy = self.compute(packet[8:12])
            Hz = self.compute(packet[12:16])
            Temp = self.compute(packet[18:20]) / 100
            SUM = int(packet[20:22], 16)
            # print("Hx: %d, Hy: %d, Hz: %d, Temp: %f, SUM: %f\n" %
            #       (Hx, Hy, Hz, Temp, SUM))
            return str("Hx: %d, Hy: %d, Hz: %d, Temp: %f, SUM: %f\n" % (Hx, Hy, Hz, Temp, SUM))
            # if SUM == 0x55 + 0x54 + int(packet[4:20], 16):
            #     print("Hx: %d, Hy: %d, Hz: %d, Temp: %f" % (Hx, Hy, Hz, Temp))

        else:
            ...

    def print_packet(self, packet: str):
        # 以十六进制打印数据包
        print(" ".join([packet[i:i+2] for i in range(0, len(packet), 2)]))

    def compute(self, hex_str: str):
        # 计算大端存储补码的十进制数
        num = int(hex_str[2:4] + hex_str[0:2], 16)
        if num & 0x8000:
            num -= 0x10000
        return num

class ReadThread(QtCore.QThread):
    '''数据读取线程'''
    hex_signal = QtCore.pyqtSignal(str)
    str_signal = QtCore.pyqtSignal(str)
    pd = PacketDecode()

    def __init__(self, ser: serial.Serial) -> None:
        '''初始化线程

        Args:
        ----------
            ser (serial.Serial): 串口对象
        '''
        super().__init__()
        self.ser = ser
        self.isRunning = True

    def __del__(self):
        self.isRunning = False

    def run(self):
        while self.isRunning:
            if self.ser != None and self.ser.in_waiting > 100:
                recive = self.ser.read(self.ser.in_waiting) # 读取串口数据
                # bytes转化为十六进制字符串
                recive = bytes(recive).hex()
                str_recive = datetime.datetime.now().strftime("\n\n%Y-%m-%d %H:%M:%S:\n") + self.pd.decode(recive) # 解析数据包
                # print(self.pd.decode(recive))
                # 在行首添加时间戳
                recive = datetime.datetime.now().strftime("\n\n%Y-%m-%d %H:%M:%S:\n") + recive
                self.hex_signal.emit(recive)
                self.str_signal.emit(str_recive)

class IMU(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = uic.loadUi("./ui/IMU.ui", self)
        self.initUI()
    
    def initUI(self):
        self.ser = None # 串口对象
        self.read_thread = None # 读取线程
        self.port_list_Init()   # 初始化串口列表
        self.cb_baudrate.addItems(["9600", "115200", "230400", "460800", "921600"]) # 初始化波特率列表
        self.btn_start.clicked.connect(self.btn_start_clicked)
        self.btn_stop.clicked.connect(self.btn_stop_clicked)
        self.btn_print.clicked.connect(self.btn_print_clicked)
        self.btn_pause.clicked.connect(self.btn_pause_clicked)
    
    def port_list_Init(self):
        '''初始化串口列表'''
        self.port_list = serial.tools.list_ports.comports()
        for port in self.port_list:
            self.cb_port.addItem(str(port))
    
    def btn_start_clicked(self):
        '''打开串口'''
        if self.ser is None:
            print("start")
            try:
                self.ser = serial.Serial(self.cb_port.currentText().split(" ")[0], int(self.cb_baudrate.currentText()))
                print(self.cb_port.currentText(), "-> open succeed")
                self.ser.flushInput()
            except (OSError, serial.SerialException):
                print(self.cb_port.currentText(), "-> open failed")
                ...
        else:
            print(self.ser.in_waiting)
    
    def btn_stop_clicked(self):
        '''关闭串口'''
        if self.ser != None and self.ser.is_open:
            self.ser.close()
            self.ser = None
            print("stop")
        else:
            print("not start")
    
    def btn_print_clicked(self):
        '''打印串口数据'''
        if self.read_thread == None:
            self.read_thread = ReadThread(self.ser)
            self.read_thread.hex_signal.connect(self.et_print_Update)
            self.read_thread.str_signal.connect(self.et_show_Update)

            self.read_thread.start(10)
        else:
            print('already start')
    
    def btn_pause_clicked(self):
        '''暂停打印串口数据'''
        self.read_thread.isRunning = False
        self.read_thread.quit()
        self.read_thread.wait()
        self.read_thread = None
    
    def et_print_Update(self, recive=None):
        '''更新打印窗口
        
        Args:
        ----------
            recive (str): 串口接收到的数据
        '''
        self.et_print.insertPlainText(recive)
        self.et_print.moveCursor(self.et_print.textCursor().End)
    
    def et_show_Update(self, recive=None):
        '''更新显示窗口
        
        Args:
        ----------
            recive (str): 串口接收到的数据
        '''
        self.et_show.insertPlainText(recive)
        self.et_show.moveCursor(self.et_show.textCursor().End)

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
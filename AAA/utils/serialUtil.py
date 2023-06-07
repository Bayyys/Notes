import serial
import serial.tools.list_ports
from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep
import utils.globalParams as glo
import utils.decodeUtil as decodeUtil
import time

class getCom(QThread):  # 获取串口号线程
    '''获取串口号线程

    Signal: comUpdate: 串口号更新信号

    emit: port_list_orignal: 串口号列表

    (检测串口的变化, 发生变化传递更新串口号列表)
    '''
    comUpdate = pyqtSignal(list)
    port_list_orignal = []
    def run(self):
        while(True):
            port_list = list(serial.tools.list_ports.comports())
            if set(port_list) != set(self.port_list_orignal):
                self.port_listUpdate(port_list)
                if len(port_list) == 0:
                    print('No serial port found!')
                    exit()
                else:
                    self.comUpdate.emit(port_list)
            sleep(1)
                
    def port_listUpdate(self, port_list):
        self.port_list_orignal = port_list

class serialRead2(QThread):  # 读取串口数据线程
    '''读取串口数据线程
    
    Signal: dateReadUpdate_new: 读取到的数据更新信号
            emit: None
    Signal: serDisconnect: 串口断开信号
            emit: num_list: 读取到的数据列表
    
    (读取串口数据, 并进行解码, 发送更新数据信号)
    '''
    serDisconnect = pyqtSignal()
    dateReadUpdate = pyqtSignal(list)
    rest = b''
    index_1 = 0 # 1号通道数据起始位置
    index_2 = 4    # 2号通道数据起始位置
    index_3 = 8    # 3号通道数据起始位置
    
    def run(self):
        print("serialRead start")
        glo.ser.flushOutput()
        glo.ser.flushInput()
        while(glo.connected):
            if serialIsOpen(glo.ser) == False:
                print("serialRead stop")
                self.serDisconnect.emit()
                serialClose(glo.ser)
                break
            if glo.ser.inWaiting():
                data = glo.ser.read(glo.ser.in_waiting)
                self.dateReadUpdate.emit(self.bytesSplit(data))

    def bytesSplit(self, data):
        '''解码数据
        
        args: data: 读取到的数据
        
        return: num_list: 解码后的数据列表'''
        num_list = [[], []]
        if len(self.rest) > 0:
            data = self.rest + data
        while len(data) > 24:
            find = data.find(b'\xa5Z')
            if find != -1 and len(data) > find + 24:
                index_s = data.find(b'\xa5Z') + 4
                index_e = index_s + 10
                get = data[index_s: index_e]
                num1 = self.bytestoFloat(get[self.index_1: self.index_2])
                if num1 > 100000:
                    num1 = 0
                num_list[0].append(num1)
                num2 = self.bytestoFloat(get[self.index_2: self.index_3])
                if num2 > 100000:
                    num2 = 0
                num_list[1].append(num2)
                data = data[index_e:]
            else:
                break
        self.rest = data
        return num_list
    
    def bytestoFloat(self, data):
        '''将字节转换为浮点数
        
        args: data: 读取到的数据
        
        return: data: 转换后的数据'''
        start_index = 0
        try:
            if data[3] > 128:
                tmp1 = (~data[start_index]) & 0xff
                tmp2 = ((~data[start_index + 1]) & 0xff) << 8
                tmp3 = ((~data[start_index + 2]) & 0xff) << 16
                data = -(tmp1 + tmp2 + tmp3 + 1)
                data = data / 24
            else:
                data = int((data[start_index]) + (data[start_index + 1] << 8) + (data[start_index + 2] << 16)
                            + (data[start_index + 3] << 24))
                data = data / 24
            return data
        except:
            return 0

class serialRead(QThread):  # 读取串口数据线程
    '''读取串口数据线程
    
    Signal: dateReadUpdate_new: 读取到的数据更新信号
            emit: None
    Signal: serDisconnect: 串口断开信号
            emit: num_list: 读取到的数据列表
    
    (读取串口数据, 并进行解码, 发送更新数据信号)
    '''
    serDisconnect = pyqtSignal()
    dateReadUpdate = pyqtSignal(list)
    rest = b''
    index_1 = 0 # 1号通道数据起始位置
    index_2 = 4    # 2号通道数据起始位置
    index_3 = 8    # 3号通道数据起始位置
    index_25 = 96  # 25号通道数据起始位置
    index_26 = 100  # 26号通道数据起始位置
    index_27 = 104  # 27号通道数据起始位置
    index_p = 128  # 通道连接状态起始位置
    index_n = 132  # 通道连接状态起始位置

    def run(self):
        print("serialRead start")
        glo.ser.flushOutput()
        glo.ser.flushInput()
        while(glo.connected):
            if serialIsOpen(glo.ser) == False:
                print("serialRead stop")
                self.serDisconnect.emit()
                serialClose(glo.ser)
                break
            if glo.ser.inWaiting():
                data = glo.ser.read(glo.ser.in_waiting)
                self.dateReadUpdate.emit(self.bytesSplit(data))

    def bytesSplit(self, data):
        '''解码数据
        
        args: data: 读取到的数据
        
        return: num_list: 解码后的数据列表'''
        num_list = [[], []]
        if len(self.rest) > 0:
            data = self.rest + data
        while len(data) > 144:
            find = data.find(b'\xa5Z')
            if find != -1 and len(data) > find + 144:
                index_s = data.find(b'\xa5Z') + 4
                index_e = index_s + 136
                get = data[index_s: index_e]
                if get[self.index_p] & 0x01 and get[self.index_n] & 0x01:
                    num1 = 0
                else:
                    num1 = self.bytestoFloat(get[self.index_1: self.index_2])
                num_list[0].append(num1)
                if get[self.index_p] & 0x02 or get[self.index_n] & 0x02:
                    num2 = 0
                else:
                    num2 = self.bytestoFloat(get[self.index_2: self.index_3])
                num_list[1].append(num2)
                data = data[index_e:]
            else:
                break
        self.rest = data
        return num_list
    
    def bytestoFloat(self, data):
        '''将字节转换为浮点数
        
        args: data: 读取到的数据
        
        return: data: 转换后的数据'''
        start_index = 0
        try:
            if data[3] > 128:
                tmp1 = (~data[start_index]) & 0xff
                tmp2 = ((~data[start_index + 1]) & 0xff) << 8
                tmp3 = ((~data[start_index + 2]) & 0xff) << 16
                data = -(tmp1 + tmp2 + tmp3 + 1)
                data = data / 24
            else:
                data = int((data[start_index]) + (data[start_index + 1] << 8) + (data[start_index + 2] << 16)
                            + (data[start_index + 3] << 24))
                data = data / 24
            return data
        except:
            return 0

def serialOpen(com, bps, timex):    # 打开串口
    """打开串口

    args: com: 串口号; bps: 波特率; timex: 超时时间

    return: ser: 串口对象
    """
    try:
        ser = serial.Serial(com, int(bps), timeout=int(timex))
        if ser.isOpen():
            print('open success')
            return ser
        else:
            print('open failed')
            return None
    except:
        print("serialOpen: 串口不存在")
        return
    finally:
        ...

def serialIsOpen(ser) -> bool:  # 判断串口是否打开
    ''' 判断串口是否打开
    
    args: ser: 串口对象
    
    return: True: 打开; False: 未打开'''
    try:
        count = ser.inWaiting()
        return True
    except:
        return False

def serialClose(ser):   # 关闭串口
    '''关闭串口
    
    args: ser: 串口对象'''
    try:
        glo.set_connected(False)
        glo.ser.close()
    except:
        print("serialClose: 串口不存在")
        return

class updateFig(QThread):   # WAIT
    def __init__(self, chartList):
        super().__init__()
        self.chartList = chartList
        # print(self.parent)

    def run(self):
        while glo.connected:
            self.chartList.canvas.draw()
class processFig(QThread):  # WAIT
    def __init__(self, chart):
        super().__init__()
        self.chart = chart
        # print(self.parent)
    
    def run(self):
        while glo.connected:
            self.chart.processData()
            ...
            

if __name__ == '__main__':
    port_list = list(serial.tools.list_ports.comports())
    print(type(port_list))
    print(port_list)
    print([port_list[0][i] + ' ' + port_list[1][i] for i in range(len(port_list[0]))])

import serial
import serial.tools.list_ports
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
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
                
    def port_listUpdate(self, port_list):
        self.port_list_orignal = port_list

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
    index_1 = 8 # 1号通道数据起始位置
    index_2 = 12    # 2号通道数据起始位置
    index_3 = 16    # 3号通道数据起始位置
    index_25 = 104  # 25号通道数据起始位置
    index_26 = 108  # 26号通道数据起始位置
    index_27 = 112  # 27号通道数据起始位置
    index_p = 136  # 通道连接状态起始位置
    index_n = 140  # 通道连接状态起始位置
    count = 0

    def run(self):
        print("serialRead start")
        glo.ser.flushInput()
        glo.ser.write(glo.send_start)
        while(glo.connected):
            if serialIsOpen(glo.ser) == False:
                print("serialRead stop")
                self.serDisconnect.emit()
                serialClose(glo.ser)
                break
            if glo.ser.inWaiting():
                data = glo.ser.read(glo.ser.in_waiting)
                get = self.bytesSplit(data)
                self.dateReadUpdate.emit(self.bytesSplit(data))
                # print(self.count)

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
                index_s = data.find(b'\xa5Z') - 4
                index_e = index_s + 144
                get = data[index_s: index_e]
                if data[self.index_p] & 0x80 == 0:
                    num1 = 0
                else:
                    num1 = decodeUtil.bytestoFloat(get[self.index_1: self.index_2])
                num_list[0].append(num1)
                if data[self.index_p] & 0x40 == 0:
                    num2 = 0
                else:
                    num2 = decodeUtil.bytestoFloat(get[self.index_2: self.index_3])
                num_list[1].append(num2)
                self.count += 1
                data = data[index_e:]
            else:
                break
        self.rest = data
        return num_list

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
            time1 = time.time()
            # for fig in self.chartList:
            #     fig.canvas.draw()
            #     fig.canvas.flush_events()
            self.chartList.canvas.draw()
            print(time.time() - time1)
            # print(len(glo.history))
            # sleep(1)

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

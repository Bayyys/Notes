import serial
import serial.tools.list_ports
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from time import sleep
import utils.globalParams as glo

class getCom(QThread):
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


def serialOpen(com, bps, timex):
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

def serialIsOpen(ser) -> bool:
    ''' 判断串口是否打开
    
    args: ser: 串口对象
    
    return: True: 打开; False: 未打开'''
    try:
        count = ser.inWaiting()
        return True
    except:
        return False

def serialClose(ser):
    '''关闭串口
    
    args: ser: 串口对象'''
    try:
        glo.set_connected(False)
        glo.ser.close()
    except:
        print("serialClose: 串口不存在")
        return


class serialRead_original(QThread):
    dateReadUpdate = pyqtSignal(str)
    serDisconnect = pyqtSignal()

    def run(self):
        """读取串口数据
        args: NONE
        return: NONE
        """
        print("serialRead start")
        glo.ser.flushInput()    # 清空缓冲区
        while(glo.connected):
            if serialIsOpen(glo.ser) == False:
                print("serialRead stop")
                self.serDisconnect.emit()
                serialClose(glo.ser)
                break
            count = glo.ser.inWaiting() # 获取缓冲区字符
            print("count: ", count)
            if count != 0:
                str0 = glo.ser.readline(glo.ser.in_waiting) # 读取内容并回显
                str = str0.decode(encoding='utf-8', errors='ignore')
                self.dateReadUpdate.emit(str)
            sleep(1)

class serialRead(QThread):
    '''读取串口数据线程
    
    Signal: dateReadUpdate_new: 读取到的数据更新信号
            emit: None
    Signal: serDisconnect: 串口断开信号
            emit: num_list: 读取到的数据列表
    
    (读取串口数据, 并进行解码, 发送更新数据信号)
    '''
    serDisconnect = pyqtSignal()
    dateReadUpdate_new = pyqtSignal(list)
    rest = b''
    index_25 = 104  # 25号通道数据起始位置
    index_26 = 108  # 26号通道数据起始位置
    index_27 = 112  # 27号通道数据起始位置
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
                self.dateReadUpdate_new.emit(self.bytesSplit(data))
                # print(self.count)

    def bytesSplit(self, data):
        '''解码数据
        
        args: data: 读取到的数据
        
        return: num_list: 解码后的数据列表'''
        num_list = [[],[]]
        if len(self.rest) > 0:
            data = self.rest + data
        while len(data) > 144:
            find = data.find(b'\xa5Z')
            if find != -1 and len(data) > find + 144:
                index_s = data.find(b'\xa5Z') - 4
                index_e = index_s + 144
                get = data[index_s: index_e]
                if data[-2] & 0x01 == 0:
                    num1 = 0
                else:
                    num1 = self.bytestoFloat(get[self.index_25: self.index_26])
                num_list[0].append(num1)
                if data[-2] & 0x02 == 0:
                    num2 = 0
                else:
                    num2 = self.bytestoFloat(get[self.index_26: self.index_27])
                num_list[1].append(num2)
                self.count += 1
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

class updateFig(QThread):
    def __init__(self, chartList):
        super().__init__()
        self.chartList = chartList
        # print(self.parent)

    def run(self):
        while glo.connected:
            for fig in self.chartList:
                fig.canvas.draw()
                # fig.canvas.flush_events()
            # print(len(glo.history))
            # sleep(1)


if __name__ == '__main__':
    port_list = list(serial.tools.list_ports.comports())
    print(type(port_list))
    print(port_list)
    print([port_list[0][i] + ' ' + port_list[1][i] for i in range(len(port_list[0]))])

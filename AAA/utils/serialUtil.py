import serial
import serial.tools.list_ports
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from time import sleep
import utils.globalParams as glo

class getCom(QThread):
    comUpdate = pyqtSignal(list)
    port_list_orignal = []

    def run(self):
        """得到所有的串口号
        args: NONE
        return: (串口号列表: ['COM1', ...], 串口名列表: ['通信端口 (COM1)'], 串口列表: ['COM1 - 通信端口 (COM1)', ...])
        """
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
    try:
        count = ser.inWaiting()
        return True
    except:
        return False

def serialClose(ser):
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
                # print('data:', data)
            sleep(1)

class serialRead(QThread):
    serDisconnect = pyqtSignal()
    dateReadUpdate_new = pyqtSignal(list)
    rest = b''
    index_25 = 104
    index_26 = 108
    index_27 = 112
    count = 0

    def run(self):
        """读取串口数据
        args: NONE
        return: NONE
        """
        print("serialRead start")
        glo.ser.flushInput()
        glo.ser.write(glo.send_start)
        while(glo.connected):
            if serialIsOpen(glo.ser) == False:
                print("serialRead stop")
                self.serDisconnect.emit()
                serialClose(glo.ser)
                break
            # if count != 0:
            if glo.ser.inWaiting():
                data = glo.ser.read(glo.ser.in_waiting)
                self.dateReadUpdate_new.emit(self.bytesSplit(data))
                # print(self.count)

    def bytesSplit(self, data):
        num_list = [[],[]]
        if len(self.rest) > 0:
            data = self.rest + data
        while len(data) > 144:
            find = data.find(b'\xa5Z')
            if find != -1 and len(data) > find + 144:
                index_s = data.find(b'\xa5Z') - 4
                index_e = index_s + 144
                get = data[index_s: index_e]
                num1 = self.bytestoFloat(get[self.index_25: self.index_26])
                num_list[0].append(num1)
                num2 = self.bytestoFloat(get[self.index_26: self.index_27])
                num_list[1].append(num2)
                self.count += 1
                self.rest = data[index_e:]
                data = data[index_e:]
            else:
                break
        return num_list

    def bytestoFloat(self, data):
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

if __name__ == '__main__':
    port_list = list(serial.tools.list_ports.comports())
    print(type(port_list))
    print(port_list)
    print([port_list[0][i] + ' ' + port_list[1][i] for i in range(len(port_list[0]))])

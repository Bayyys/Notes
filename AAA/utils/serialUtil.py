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

class serialRead(QThread):
    dateReadUpdate = pyqtSignal(str)
    serDisconnect = pyqtSignal()
    def run(self):
        """读取串口数据
        args: NONE
        return: NONE
        """
        print("serialRead start")
        glo.ser.flushInput()
        while(glo.connected):
            if serialIsOpen(glo.ser) == False:
                print("serialRead stop")
                self.serDisconnect.emit()
                serialClose(glo.ser)
                break
            count = glo.ser.inWaiting()
            if count != 0:
                str0 = glo.ser.read(glo.ser.in_waiting)
                str = str0.decode(encoding='utf-8', errors='ignore')
                self.dateReadUpdate.emit(str)
            sleep(0.1)

if __name__ == '__main__':
    port_list = list(serial.tools.list_ports.comports())
    # ser = serialOpen('COM6', 115200, 5)
    print(type(port_list))
    print(port_list)
    print([port_list[0][i] + ' ' + port_list[1][i] for i in range(len(port_list[0]))])

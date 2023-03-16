from PyQt5.QtCore  import QMutex
from decodeUtil import signalDecode
import numpy as np 
import pandas as pd

scan = None # 扫描 type: bool
connected = None    # 连接 type: bool
ser = None  # 串口对象 type: serial.Serial
history = []   # 数据 type: list
data = []   # 数据 type: list
mutex_history = None    # 互斥锁    type: QMutex
mutex_data = None   # 互斥锁    type: QMutex
time = None # 时间 type: QDateTime
com = None  # 当前连接串口号 type: str

def __init__():
    global scan, connected, ser, history, data, mutex_history, mutex_data, time, com
    scan = False
    connected = False
    ser = None
    history = [str(i + 1) for i in range(100)]
    data = []
    mutex_history = QMutex()
    mutex_data = QMutex()
    time = 1
    com = ""


def get_scan():
    return scan

def set_scan(value):
    global scan
    scan = value

def get_connected():
    return connected

def set_connected(value):
    global connected
    connected = value

def get_ser():
    return ser

def set_ser(value):
    global ser
    ser = value

# def get_history():
#     global history
#     mutex_history.lock()
#     ret = history
#     mutex_history.unlock()
#     return ret

# def set_history(value):
#     global history
#     mutex_history.lock()
#     history = value
#     mutex_history.unlock()

def add_history(value):
    global history
    mutex_history.lock()
    history += signalDecode(value)
    add_data(value)
    mutex_history.unlock()

def dataNotEmpty():
    global data
    return len(data) != 0

def get_data():
    global data
    mutex_data.lock()
    ret = data
    clear_data()
    mutex_data.unlock()
    return ret

def clear_data():
    global data
    data = []

def add_data(value):
    global data
    mutex_data.lock()
    data += signalDecode(value)
    mutex_data.unlock()

def get_time():
    global time
    ret = time
    time += 1
    return ret

def get_com():
    return com

def set_com(value):
    global com
    com = value

def save_data():
    try:
        np.savetxt('test.txt', np.array(history), fmt='%s', delimiter='\t\n', newline='', header='', footer='', comments='# ', encoding=None)
        print(np.array(history))
        print(np.array(history).shape)
    except Exception as e:
        print("error")
    ...


if __name__ == '__main__':
    __init__()
    test = pd.DataFrame(history)
    df = test.to_csv('test.csv', mode='a', index=False, header=False)
    print(test)
    print(pd.read_csv('test.csv', header=None))
    ...

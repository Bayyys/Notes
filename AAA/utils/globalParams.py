from utils.decodeUtil import HighPassFilter, NotchFilter, BandPassFilter
import sys
sys.path.append('..')
from PyQt5.QtCore import QMutex, pyqtSignal
import numpy as np
import pandas as pd

scan = None  # 扫描 type: bool
connected = None    # 连接 type: bool
ser = None  # 串口对象 type: serial.Serial
history = []   # 数据 type: list
data = []   # 数据 type: list   # WAIT
mutex_history = None    # 互斥锁    type: QMutex
mutex_data = None   # 互斥锁    type: QMutex
time = None  # 时间 type: QDateTime # WAIT
com = None  # 当前连接串口号 type: str
massage_start = ''  # 开始采集命令 type: str    # TODO
massage_stop = ''   # 停止采集命令 type: str    # TODO
massage_sampleRate = '' # 采样率命令 type: str    # TODO
send_start = [] # 开始采集命令 type: bytes    # TODO
send_stop = []  # 停止采集命令 type: bytes    # TODO
send_sampleRate = []    # 采样率命令 type: bytes    # TODO
isHighPassFilter = False    # 是否开启高通滤波 type: bool
isNotchFilter = False   # 是否开启陷波滤波 type: bool
isBandPassFilter = False    # 是否开启带通滤波 type: bool
XDIS = 8000 # X轴显示范围 type: int
YDIS = 200000   # Y轴显示范围 type: int
sample_rate = 1000  # 采样率 type: int

def __init__():
    global scan, connected, ser, history, data, mutex_history, mutex_data, time, com, massage_start, massage_stop, massage_sampleRate, send_start, send_stop, send_sampleRate, isHighPassFilter, isNotchFilter, isBandPassFilter, XDIS, YDIS, sample_rate, channel_num,  sos_high, sos_notch, sos_band, highFilter_high, notchFilter_cutoff, notchFilter_param, bandFilter_pass, bandFilter_stop
    scan = False
    connected = False
    ser = None
    history = np.array([[], []])
    data = []   # WAIT
    mutex_history = QMutex()
    mutex_data = QMutex()
    time = 1    # WAIT
    com = ""
    massage_start = 'AA 06 01'  # TODO
    massage_stop = 'AA 06 00'   # TODO
    massage_sampleRate = 'AA 03 01' # TODO
    for mas in massage_start.split(' '):
        send_start += bytes.fromhex(mas)    # TODO
    for mas in massage_stop.split(' '):
        send_stop += bytes.fromhex(mas) # TODO
    for mas in massage_sampleRate.split(' '):
        send_sampleRate += bytes.fromhex(mas)   # TODO
    isHighPassFilter = False
    isNotchFilter = False
    isBandPassFilter = False
    XDIS = 8000
    YDIS = 200000
    sample_rate = 1000
    channel_num = 2
    sos_high = None
    sos_notch = None
    sos_band = None
    highFilter_high = 1
    notchFilter_cutoff = 50
    notchFilter_param = 10
    bandFilter_pass = 1
    bandFilter_stop = 50

def initFilterParams():
    global sos_high, sos_notch, sos_band
    sos_high = HighPassFilter(highFilter_high, sample_rate)
    sos_notch = NotchFilter(notchFilter_cutoff, notchFilter_param, sample_rate)
    sos_band = BandPassFilter(bandFilter_pass, bandFilter_stop, sample_rate)

def highFilterUpdate():
    global sos_high, highFilter_high
    sos_high = HighPassFilter(highFilter_high, sample_rate)

def notchFilterUpdate():
    global sos_notch, notchFilter_cutoff, notchFilter_param
    sos_notch = NotchFilter(notchFilter_cutoff, notchFilter_param, sample_rate)

def bandFilterUpdate():
    global sos_band, bandFilter_pass, bandFilter_stop
    sos_band = BandPassFilter(bandFilter_pass, bandFilter_stop, sample_rate)

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

def init_history():
    global history
    mutex_history.lock()
    history = np.array([[], []])
    mutex_history.unlock()

def add_history(value):
    global history
    # add_data(value)
    mutex_history.lock()
    history = np.concatenate((history, value), axis=1)
    # print(history)
    mutex_history.unlock()

def len_history():
    global history
    return history.shape[1]

# WAIT
def dataNotEmpty():
    global data
    return len(data) != 0

# WAIT
def get_data():
    global data
    mutex_data.lock()
    ret = data
    clear_data()
    mutex_data.unlock()
    return ret

# WAIT
def clear_data():
    global data
    data = []

# WAIT
def add_data(value):
    global data
    mutex_data.lock()
    data += value
    mutex_data.unlock()

# WAIT
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


def save_data(fileName, type):
    try:
        if type == "CSV(*.csv)":
            pd.DataFrame(history).to_csv(fileName, mode='a', index=False, header=False)
        elif type == "纯文本(*.txt)":
            np.savetxt(fileName, np.array(history), fmt='%lf', delimiter=' ',
                   newline='\n', header='', footer='', comments='# ', encoding=None)
        # print(np.array(history))
        print(np.array(history).shape)
        return True
    except Exception as e:
        print("error")
        return False
    ...

def open_data(fileName, type):
    global history
    try:
        if type == "CSV(*.csv)":
            data = pd.read_csv(fileName, header=None)
            history = np.array(data.values)
            return True
        elif type == "纯文本(*.txt)":
            history = np.loadtxt(fileName, dtype=float)
            return True
        else:
            return False
    except Exception as e:
        print("error")
        return False
    ...

if __name__ == '__main__':
    __init__()
    # test = pd.DataFrame(history)
    # df = test.to_csv('test.csv', mode='a', index=False, header=False)
    # print(test)
    # data = pd.read_csv('test.csv', header=None)
    # print(data.loc[:, 0])
    # history = [str(i + 1) for i in range(100)]
    # data = np.array(history)
    # print(data)
    # np.savetxt('test.txt', data, fmt='%.2lf', delimiter='\t\n',
    #            newline='', header='', footer='', comments='# ', encoding=None)
    # data2 = np.loadtxt('test.txt', dtype=str)
    # print(data2)
    print(history.shape)
    add_history([[1,2], [3,4]])
    add_history([[5,6], [7,8]])
    print(history)
    ...

import numpy as np
import matplotlib.pyplot as plt  # plt用于显示图片
from collections import deque
import serial, time


# 如果你的电脑没有serial库, 需要先pip install serial, 然后再pip install pyserial. 不然会报错：找不到Serial函数.
def imu_analysis(buffer, data_everychannel):
    # 对于原始IMU传感器数据包的处理，自定义9个包数组，分别对应角加速度，角速度，欧拉角
    channel, i, data_channel, imu_channel, width = 9, 0, '', 0, 16
    while channel:
        for j in range(2):  # 循环两次,分别取高八位和低八位
            data_channel = data_channel + buffer[i:i + 2]
            i += 2
        imu_channel = int(data_channel, 16)  # 转化为16进制整型
        # 补码
        if imu_channel > 2 ** (width - 1) - 1:
            imu_channel = 2 ** width - imu_channel
            imu_channel = 0 - imu_channel
        imu_cal(data_everychannel, imu_channel, 9 - channel)
        channel -= 1
        data_channel = ''
    return data_everychannel


def imu_cal(data_everychannel, imu_channel, channel):
    # 根据IMU量程 对数据进行处理
    if (channel < 3):  # data_everychannel[0,1,2]:aacx1,aacy1,aacz1
        data_everychannel[channel] = imu_channel / 208.98  # 1671.837
    elif (channel < 6):  # data_everychannel[3,4,5]:gyrox1,gyroy1,gyroz1
        data_everychannel[channel] = imu_channel / 16.384
    elif (channel < 9):  # data_everychannel[6,7,8]:pitch,roll,yaw
        data_everychannel[channel] = imu_channel
    elif (channel < 12):  # data_everychannel[9,10,11]:aacx2,aacy2,aacz2
        data_everychannel[channel] = imu_channel / 208.98  # 208.98
    elif (channel < 15):  # data_everychannel[12,13,14]:gyrox2,gyroy2,gyroz2
        data_everychannel[channel] = imu_channel / 16.384
    elif (channel < 18):  # data_everychannel[15,16,17]:pitch2,roll2,yaw2
        data_everychannel[channel] = imu_channel

    return data_everychannel


def decode(code):  # (datapkg start with "FF FF 24", end with "16")
    # 对自定义原始数据包进行解析
    global data_everychannel
    codelen = len(code)
    while code:
        if codelen < 44:
            break
        pkghead, code = code[:2], code[2:]
        codelen = codelen - 2
        if pkghead == 'ff':  # 检查包头ffff1200000000000000000000000000000000000016
            pkgfun, pkglen, pkgend = code[:2], code[2:4], code[40:42]
            if pkgfun == 'ff' and pkglen == '12' and pkgend == '16':  # 检查功能字、数据长、包结尾
                buffer, code = code[4:40], code[42:]
                codelen = codelen - 42
                data_everychannel = imu_analysis(buffer, data_everychannel)
    return data_everychannel


def init_cal(data, data_init, rg):  # rg:range 量程
    # 初始化计算: 记录下初始值，坐标换算：当前坐标 = 原始坐标 - 初始坐标
    data_new = data - data_init
    # 超量程部分换算
    if data_new <= -rg:
        data_new = data_new + 2 * rg
    if data_new > rg:
        data_new = data_new - 2 * rg

    return data_new


def plot_durations3(y1, y2, y3, y11, y22):
    y = []
    y.append(np.array([y1, y2, y3]))
    plt.figure(3)
    plt.clf()
    plt.subplot(311)
    plt.ylabel("pitch")
    plt.plot(y1)
    plt.plot(y11)
    plt.subplot(312)
    plt.ylabel("roll")
    plt.plot(y2)
    plt.plot(y22)
    plt.subplot(313)
    plt.ylabel("yaw")
    plt.plot(y3)
    plt.pause(0.0001)  # pause a bit so that plots are updated
    plt.ioff()
    # plt.show()


if __name__ == "__main__":
    # data_everychannel = [i for i in range(9)]  # imu实时数据
    #
    roll, pitch, yaw = deque([], maxlen=20000), deque([], maxlen=20000), deque([], maxlen=20000)
    x, y, z = deque([], maxlen=20000), deque([], maxlen=20000), deque([], maxlen=20000)
    # # 串口初始化
    # serialport = serial.Serial()
    # serialport.port = 'COM9'
    # serialport.baudrate = 256000
    # serialport.bytesize = 8
    # serialport.parity = serial.PARITY_NONE
    # serialport.stopbits = 1
    # serialport.timeout = 0.001
    # serialport.close()
    # if not serialport.is_open:
    #     serialport.open()
    # time.sleep(0.05)  # 时间设置参考串口传输速率
    # num = serialport.inWaiting()
    # # ser = serial.Serial("COM6", 115200, timeout=5) # 这里写入对应串口
    # # time.sleep(3)
    # serialport.flushInput()
    # # count = ser.inWaiting()
    # time.sleep(1)
    # 数据采集处理与可视化绘图
    print(1)
    while True:
        init_time = time.time_ns()
        # count = serialport.inWaiting()

        # time.sleep(0.000001)

        if True:
            # read_data = (time.time_ns() - init_time) / 1e6
            # print(read_data)
            # recv = serialport.read(serialport.inWaiting()).hex()
            # print(recv)
            # data_everychannel = decode(recv)
            #
            # 读取大腿\小腿姿态角
            roll.append(0)  # roll
            pitch.append(0)  # pitch
            yaw.append(0)  # yaw
            x.append(0)  # roll
            y.append(0)  # pitch
            z.append(0)  # yaw
            # 实时打印显示
            # print(f"roll={data_everychannel[6]}, pitch={data_everychannel[7]}, yaw={data_everychannel[8]}")
            # 绘制图象
            # if len(roll) >= 20000:
            roll1 = np.arctan2(y, z) * 180 / np.pi
            pitch1 = np.arctan2(-np.array(x),
                                np.sqrt(np.array(y) ** 2 + np.array(z) ** 2)) * 180 / np.pi
            plt.ion()
            plot_durations3(pitch, roll, yaw, pitch1, roll1)
                # print((time.time_ns() - init_time) / 1e6)
            plt.show()

            # print((time.time_ns() - init_time) / 1e6)
        # time.sleep(0.1)  # 延时0.1秒，免得CPU出问题

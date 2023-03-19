import numpy as np
import matplotlib.pyplot as plt  # plt用于显示图片
import matplotlib.transforms as tr
from collections import deque
import serial, time
# from bleak import BleakScanner
# from bleak import BleakClient
# import asyncio

data_everychannel = [i for i in range(18)]
data_record = deque([[0 for i in range(18)] for j in range(3)], maxlen=1000)
length = 4

def imu_analysis(buffer, data_everychannel):
    # 对于原始IMU传感器数据包的处理，自定义18个包数组，分别对应角加速度，角速度，欧拉角
    channel, i, data_channel, imu_channel, width = 18, 0, '', 0, 16
    while (channel):
        for j in range (2): #循环两次,分别取高八位和低八位
            data_channel = data_channel + buffer[i:i + 2]
            i += 2
        imu_channel = int(data_channel, 16)  #转化为16进制整型
        # 补码
        if imu_channel > 2 ** (width - 1) - 1:
            imu_channel = 2 ** width - imu_channel
            imu_channel = 0 - imu_channel
        imu_cal(data_everychannel, imu_channel, 18 - channel)
        channel -= 1
        data_channel = ''
    return data_everychannel

def imu_cal(data_everychannel, imu_channel, channel):
    # 根据IMU量程 对数据进行处理
    if (channel < 3):  # data_everychannel[0,1,2]:aacx1,aacy1,aacz1
        data_everychannel[channel] = imu_channel / 1671.837#208.98
    elif (channel < 6):  # data_everychannel[3,4,5]:gyrox1,gyroy1,gyroz1
        data_everychannel[channel] = imu_channel #/ 16.384
    elif (channel < 9):  # data_everychannel[6,7,8]:pitch,roll,yaw
        data_everychannel[channel] = imu_channel
    elif (channel < 12):  # data_everychannel[9,10,11]:aacx2,aacy2,aacz2
        data_everychannel[channel] = imu_channel / 1671.837#208.98
    elif (channel < 15):  # data_everychannel[12,13,14]:gyrox2,gyroy2,gyroz2
        data_everychannel[channel] = imu_channel #/ 16.384
    elif (channel < 18):  # data_everychannel[15,16,17]:pitch2,roll2,yaw2
        data_everychannel[channel] = imu_channel

    return data_everychannel

def decode(code):  # 这个用于STM32WB55(start with "FE 36 xx xx 0B")新版在用
    # 对自定义原始数据包进行解析
    buffer, data_everychannel = '', [0 for i in range(18)]
    codelen = len(code)
    while (code):
        if codelen < 90: # 总数据包长度为10+36+36+2=84，这里留些余量
            break
        head, code = code[:2], code[2:]
        codelen -= 2
        if head == 'fe': # 成功获取包头
            pktlen, pktseq, fun, pktend = code[:2], code[2:6], code[6:8], code[80:82]
            if pktlen == '36' and fun == '0b' and pktend == '16':# 检查数据长、功能字、包结尾
                buffer, code = code[8:80], code[82:]
                codelen = codelen - 82
                data_everychannel = imu_analysis(buffer, data_everychannel)

    return data_everychannel

# def decode(code):  # 这个用于STM32WB55(start with "FE 36 xx xx 0B")原版，可能有问题
#     # 对自定义原始数据包进行解析
#     buffer, data_everychannel = '', [0 for i in range(18)]
#     codelen = len(code)
#     while (code):
#         if codelen < 90: # 总数据包长度为10+36+36+2=84，这里留些余量
#             break
#         head, code = code[:2], code[2:]
#         codelen -= 2
#         if head == 'fe': # 成功获取包头
#             pktlen, pktseq1, pktseq2, fun, code = code[:2], code[2:4], code[4:6], code[6:8], code[8:]
#             codelen = codelen - 8
#             if pktlen == '36' and fun == '0b':  # 获取数据长、包序号与功能字
#                 buffer, pktend = code[:72], code[72:74]  # 包结尾pktend == '16'
#                 codelen = codelen - 74
#             data_everychannel = imu_analysis(buffer, data_everychannel)
#     return data_everychannel

# def decode(code): # 这个用于STM32F103(start with "FF FF 24")
#     # 对自定义原始数据包进行解析
#     buffer = ''
#     data_everychannel = [i for i in range(18)]
#     codelen = len(code)
#     while (code):
#         if codelen < 80:
#             break
#         data, code = code[:2], code[2:]
#         codelen = codelen - 2
#         if data == 'ff':
#             lenbu1, lenbu2 = code[:2], code[2:4]
#             if lenbu1 == 'ff' and lenbu2 == '24':
#                 buffer, code = code[4:76], code[76:]
#                 codelen = codelen - 78
#                 data_everychannel = imu_analysis(buffer, data_everychannel)
#     return data_everychannel

def init_cal(data, data_init, rg): #rg:range 量程
    # 初始化计算: 记录下初始值，坐标换算：当前坐标 = 原始坐标 - 初始坐标
    data_new = data - data_init
    # 超量程部分换算
    if data_new <= -rg:
        data_new = data_new + 2*rg
    if data_new > rg:
        data_new = data_new - 2*rg

    return data_new



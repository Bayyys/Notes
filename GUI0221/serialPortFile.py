from tkinter import END
import serial
import threading
import time
# 获取并存储串口号到数组

#  串口控制
def GetCom():
    port_list = list(serial.tools.list_ports.comports())    # 获取串口号
    # print(len(port_list))
    portcnt = len(port_list)    # 获取串口数量
    serial_com = []    # 串口号数组
    for m in range(portcnt):
        port_list_1 = list(port_list[m])
        serial_com.append(port_list_1[0])
    return serial_com   # 返回串口号数组

# 波特率控制
def usart_ctrl(com, bps,parity_,stopbits_,bytesize_):
    # print(__file__, sys._getframe().f_lineno, port_, bitrate_, var.get())
    global ser, button_var  # 定义全局变量
    if button_var.get() == "打开串口":  # 判断按钮文本
        button_var.set("关闭串口")  # 设置按钮文本
        ser = serial.Serial(
            port=com,
            baudrate=int(bps),
            parity=parity_,
            timeout=0.2,
            stopbits=float(stopbits_),
            bytesize=int(bytesize_))    # 打开串口
        if ser.is_open:
            pass    # 串口已经打开
        else:
            ser.open()  # 打开串口
        # recv_data = threading.Thread(target=thread_recv)
        # recv_data.start()
    else:
        button_var.set("打开串口")
        if ser.is_open:
            ser.close()
        else:
            pass

# 发送数据
def usart_sent(var):
    # print(__file__, sys._getframe().f_lineno, "-->", var)
    print(var)
    if ser.is_open:
        ser.write(var.encode("gb2312")) # 发送数据

# 接收数据
def thread_recv():
    global text_rx  # 定义全局变量
    while True:
        try:
            read = ser.readall()    # 读取串口数据
            if len(read) > 0:   # 判断是否有数据
                print(bytes(read).decode('gb2312')) # 打印数据
                # print(__file__, sys._getframe().f_lineno, "<--", bytes(read).decode('ascii'))
                text_rx.insert(END,bytes(read).decode('gb2312'))    # 显示数据
        except Exception as e:
            print(e)    # 打印错误信息
            time.sleep(1)   # 等待1秒
            pass

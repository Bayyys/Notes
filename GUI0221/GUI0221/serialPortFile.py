import serial
import threading
import time
# 获取并存储串口号到数组


def GetCom():
    port_list = list(serial.tools.list_ports.comports())
    # print(len(port_list))
    portcnt = len(port_list)
    serial_com = []
    for m in range(portcnt):
        port_list_1 = list(port_list[m])
        serial_com.append(port_list_1[0])
    return serial_com


def usart_ctrl(com, bps,parity_,stopbits_,bytesize_):
    # print(__file__, sys._getframe().f_lineno, port_, bitrate_, var.get())
    global ser, button_var
    if button_var.get() == "打开串口":
        button_var.set("关闭串口")
        ser = serial.Serial(
            port=com,
            baudrate=int(bps),
            parity=parity_,
            timeout=0.2,
            stopbits=float(stopbits_),
            bytesize=int(bytesize_))
        if ser.is_open:
            pass
        else:
            ser.open()
        # recv_data = threading.Thread(target=thread_recv)
        # recv_data.start()
    else:
        button_var.set("打开串口")
        if ser.is_open:
            ser.close()
        else:
            pass


def usart_sent(var):
    # print(__file__, sys._getframe().f_lineno, "-->", var)
    print(var)
    if ser.is_open:
        ser.write(var.encode("gb2312"))


def thread_recv():
    global text_rx
    while True:
        try:
            read = ser.readall()
            if len(read) > 0:
                print(bytes(read).decode('gb2312'))
                # print(__file__, sys._getframe().f_lineno, "<--", bytes(read).decode('ascii'))
                text_rx.insert(END,bytes(read).decode('gb2312'))
        except Exception as e:
            print(e)
            time.sleep(1)
            pass

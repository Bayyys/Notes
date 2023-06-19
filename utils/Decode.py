import sys
sys.path.append('..')


class PacketDecode:
    """数据包解析
    根据串口关键字类型, 解析串口数据包

    Args:
    ----------------
        key(str): 串口关键字类型, "A" "B" "C" 为IMU, "H" 为Pressure
    """

    def __init__(self, key: str) -> None:
        self.key = key  # 串口关键字类型
        # 字符串部分
        self.remain = ""  # 保存上一次解析的数据包的剩余部分
        self.str_show = ""  # 保存解析后的数据(文本描述)
        # IMU
        self.Acc_list = []  # 保存解析后的加速度数据
        self.Gyro_list = []  # 保存解析后的角速度数据
        self.Angle_list = []  # 保存解析后的角度数据
        self.Mag_list = []  # 保存解析后的磁场数据
        self.T_list = []  # 保存解析后的温度数据
        # 压力传感器
        self.P_list = []  # 保存解析后的压力数据
        ...

    def decode(self, receive: str) -> list:
        """ 解析数据
        """
        if self.key == "H":
            return self.decode_p(receive)
        else:
            return self.decode_imu(receive)

    def decode_imu(self, receive: str) -> list:
        """ 解析 IMU 数据

        将接收到的数据根据包头(0x55)进行分段, 然后解析数据包

        Args:
        ----------------
            receive(str): 接收到的数据

        Returns:
        ----------------
            str_show(str): 解析后的数据
        """
        self.str_show = ""
        self.Acc_list = []
        self.Gyro_list = []
        self.Angle_list = []
        self.Mag_list = []
        self.T_list = []
        # 从数据中提取出数据包
        receive = self.remain + receive
        while len(receive) >= 22:
            # 搜索包头
            if receive[0:2] != "55":
                # 找到第一个 '55'
                position = receive.find("55")
                if position == -1:
                    # 没有找到 '55'
                    self.remain = ""
                    return [self.str_show, [self.Acc_list, self.Gyro_list, self.Angle_list, self.Mag_list, self.T_list]]
                else:
                    # 找到了 '55'
                    receive = receive[position:]
                continue
            # 提取数据包
            packet = receive[:22]
            # 解析数据包
            try:
                self.str_show += self.decode_packet_imu(packet)
                receive = receive[22:]
            except:
                # 打印错误信息
                print("IMU 数据包解析错误" + str(packet[:22]))
                receive = receive[2:]

        if len(receive) < 22:
            self.remain = receive
        return [self.str_show, [self.Acc_list, self.Gyro_list, self.Angle_list, self.Mag_list, self.T_list]]

    def decode_packet_imu(self, packet) -> str:
        """ 解析 IMU 数据包

        数据包头为 0x55 0xXX, 其中 XX 为数据包类型

        数据包类型:
        ----------------
            0x51 - 加速度 Acc;
            0x52 - 角速度 Gyro;
            0x53 - 角度 Angle;
            0x54 - 磁场 Mag;

        Args:
        ----------------
            packet(str): 分割后的数据包(长度为 22 个字符)

        Returns:
        ----------------
            str_show(str): 解析后的数据
        """
        code = packet[2:4]

        if code == "51":
            # self.print_packet(packet)
            # 加速度 Acc
            # 数据格式为 - 0x55 0x52 AxL AxH AyL AyH AzL AzH TL TH SUM
            # 加速度
            # xAcc = ((AxH << 8) | AxL) / 32768 * 16 * g (g = 9.8 m/s^2)
            # yAcc = ((AyH << 8) | AyL) / 32768 * 16 * g (g = 9.8 m/s^2)
            # zAcc = ((AzH << 8) | AzL) / 32768 * 16 * g (g = 9.8 m/s^2)
            # 温度
            # temp = ((TH << 8) | TL) / 100 ℃
            # 校验和
            # SUM = 0x55 + 0x51 + AxL + AxH + AyL + AyH + AzL + AzH + TL + TH
            XAcc = self.complement_compute(packet[4:8]) / 32768 * 16
            YAcc = self.complement_compute(packet[8:12]) / 32768 * 16
            ZAcc = self.complement_compute(packet[12:16]) / 32768 * 16
            Temp = self.complement_compute(packet[16:20]) / 100
            SUM = int(packet[20:22], 16)
            self.Acc_list.append([XAcc, YAcc, ZAcc])
            self.T_list.append(Temp)
            return str("XAcc: %f, YAcc: %f, ZAcc: %f, Temp: %f, SUM: %f\n" % (XAcc, YAcc, ZAcc, Temp, SUM))

        elif code == "52":
            # self.print_packet(packet)
            # 角速度 Gyro
            # 数据格式为 - 0x55 0x52 wxL wxH wyL wyH wzL wzH TL TH SUM
            # 角速度
            # xGyro = ((wxH << 8) | wxL) / 32768 * 2000 °/s
            # yGyro = ((wyH << 8) | wyL) / 32768 * 2000 °/s
            # zGyro = ((wzH << 8) | wzL) / 32768 * 2000 °/s
            # 温度
            # temp = ((TH << 8) | TL) / 100 ℃
            # 校验和
            # SUM = 0x55 + 0x52 + wxL + wxH + wyL + wyH + wzL + wzH + TL + TH
            XGyro = self.complement_compute(packet[4:8]) / 32768 * 2000
            YGyro = self.complement_compute(packet[8:12]) / 32768 * 2000
            ZGyro = self.complement_compute(packet[12:16]) / 32768 * 2000
            Temp = self.complement_compute(packet[16:20]) / 100
            SUM = int(packet[20:22], 16)
            self.Gyro_list.append([XGyro, YGyro, ZGyro])
            self.T_list.append(Temp)
            return str("XGyro: %f, YGyro: %f, ZGyro: %f, Temp: %f, SUM: %f\n" % (XGyro, YGyro, ZGyro, Temp, SUM))

        elif code == "53":
            # self.print_packet(packet)
            # 角度 Ang
            # 数据格式为 - 0x55 0x53 RollL RollH PitchL PitchH YawL YawH VL VH SUM
            # 角度
            # 滚转角(x轴) Roll = ((RollH << 8) | RollL) / 32768 * 180 °
            # 俯仰角(y轴) Pitch = ((PitchH << 8) | PitchL) / 32768 * 180 °
            # 偏航角(z轴) Yaw = ((YawH << 8) | YawL) / 32768 * 180 °
            # 固件版本
            # Version = VH << 8 | VL
            # 校验和
            # SUM = 0x55 + 0x53 + RollL + RollH + PitchL + PitchH + YawL + YawH + VL + VH
            Roll = self.complement_compute(packet[4:8]) / 32768 * 180
            Pitch = self.complement_compute(packet[8:12]) / 32768 * 180
            Yaw = self.complement_compute(packet[12:16]) / 32768 * 180
            Version = int(packet[16:20], 16)
            SUM = int(packet[20:22], 16)
            self.Angle_list.append([Roll, Pitch, Yaw])
            return str("Roll: %f, Pitch: %f, Yaw: %f, Version: %d, SUM: %f\n" % (Roll, Pitch, Yaw, Version, SUM))

        elif code == "54":
            # self.print_packet(packet)
            # 磁场 Mag
            # 数据格式为 - 0x55 0x54 HxL HxH HyL HyH HzL HzH TL TH SUM
            # 磁场
            # Hx = ((HxH << 8) | HxL)
            # Hy = ((HyH << 8) | HyL)
            # Hz = ((HzH << 8) | HzL)
            # 温度
            # temp = ((TH << 8) | TL) / 100 ℃
            # 校验和
            # SUM = 0x55 + 0x54 + HxL + HxH + HyL + HyH + HzL + HzH + TL + TH
            Hx = self.complement_compute(packet[4:8]) / 1000
            Hy = self.complement_compute(packet[8:12]) / 1000
            Hz = self.complement_compute(packet[12:16]) / 1000
            Temp = self.complement_compute(packet[16:20]) / 100
            SUM = int(packet[20:22], 16)
            self.Mag_list.append([Hx, Hy, Hz])
            self.T_list.append(Temp)
            return str("Hx: %d, Hy: %d, Hz: %d, Temp: %f, SUM: %f\n" % (Hx, Hy, Hz, Temp, SUM))

        elif code == "5f":
            print(packet)
            return "1" + str(packet)

        else:
            # 数据包类型错误
            return "else\n"
            ...

    def decode_p(self, receive: str) -> list:
        """ 解析气压数据

        将得到的气压数据根据包头(0xAA)分段, 并解析成字典格式，方便后续处理

        Args:
        ----------
            receive (str): 接收的数据
        
        Returns:
        ----------
            dict: 解析后的数据
        """
        self.str_show = ""  # 显示的字符串
        self.P_list = []  # 气压数据
        # 剩余数据追加到头部
        receive = self.remain + receive
        # 按包头分段
        while len(receive) >= 70:
            # 检查包头
            if receive[0:4] != "aa01":
                # 找到包头
                receive = receive[2:]
                continue
            # 提取数据包
            packet = receive[0:70]
            receive = receive[70:]
            # 解析数据包
            try:
                self.str_show += self.decode_packet_p(packet) + "\n"
            except:
                # 数据包解析错误
                print("压力传感器数据包解析错误 ", sys.exc_info()[0])
        return [self.str_show, self.P_list]

    def decode_packet_p(self, packet: str) -> str:
        """ 解析压力传感器数据包

        数据包头为 0xaa 0x01, 分别为 帧头+数据包编号
        B1     B2        B3       B4     ( B5  ~  B32 )   B35
        AA     01        XX       XX     ( ...    ... )    XX
        帧头 数据包编号 点1高八位 点1第八位 点?高八位 点?第八位 校验和

        Args:
        ----------
            packet (str): 数据包
        
        Returns:
        ----------
            str: 解析后的字符串
        """
        data_list = []
        point = 1
        str_show = ""
        for i in range(4, 68, 4):
            p0 = int(packet[i:i + 2], 16) * 256 + int(packet[i + 2:i + 4], 16)
            data_list.append(p0)
            str_show += "P %2d:%4d; " % (point, p0)
            point += 1
        self.P_list.append(data_list)
        return str_show

    @staticmethod
    def print_packet(packet: str) -> None:
        """以十六进制打印数据包
        AABBCC ===> AA BB CC

        Args:
        ----------
            packet (str): 数据包
        """
        print(" ".join([packet[i:i + 2] for i in range(0, len(packet), 2)]))

    @staticmethod
    def complement_compute(hex_str) -> int:
        """计算大端存储补码的十进制数
        0x8000 - 0xFFFF 为负数
        0x0000 - 0x7FFF 为正数

        Args:
        ----------
            hex_str (str): 十六进制字符串
        
        Returns:
        ----------
            num (int): 十进制数
        """
        num = int(hex_str[2:4] + hex_str[0:2], 16)
        if num & 0x8000:
            num -= 0x10000
        return num

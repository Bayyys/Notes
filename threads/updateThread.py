import sys
sys.path.append('..')
from PyQt5 import QtCore
from ui.sensor_info_ui.SensorInfo import SensorInfo


class UpdateThread(QtCore.QThread):
    """数据更新线程
    用于更新 SensorInfo 数据

    Args:
    ----------
        sensorinfo (SensorInfo): 传感器信息对象
    """

    def __init__(self, sensorinfo: SensorInfo) -> None:
        super().__init__()
        self.sensorinfo = sensorinfo
        self.is_running = True
        self.isUpdate = False
        self.imu_key_list = ["Acc", "Gyr", "Angle", "Mag", "T"]  # IMU数据关键字
        self.data = []

    def __del__(self):
        self.is_running = False

    def update_data(self, data: list):
        """ 数据更新线程 -> 更新数据

        Args:
        ----------
            data (list): 数据列表 -> {"A" "B" "C": [Acc, Gyr, Angle, Mag, T], "H": [16 x data]}
        """
        self.data = data
        self.isUpdate = True

    def run(self):
        while self.is_running:
            if self.isUpdate:
                try:
                    # 调用 SensorInfo.update() 更新数据
                    self.sensorinfo.update(self.data)
                except Exception as e:
                    # 更新失败 输出更新失败的数据
                    print(self.data)
                    print("更新失败")
                self.isUpdate = False
            self.msleep(100)  # 10ms更新一次

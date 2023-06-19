import numpy as np
from PyQt5 import QtCore
import datetime
import os
import sys
sys.path.append('./../')


# 使用线程保存数据
class SaveThread(QtCore.QThread):
    """数据保存线程
        用于保存数据, 线程创建时创建对应文件
    Args:
    ----------
        key (str): 串口关键字 -> ["A", "B", "C", "H"]
    """

    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = key
        self.is_running = True
        self.data = np.array([])
        self.Acc = []
        self.Gyr = []
        self.Angle = []
        self.Mag = []
        self.T = []
        self.file_path = ""
        self.save_create()

    def __del__(self):
        self.is_running = False

    def save_create(self):
        """ 数据保存线程 -> 创建文件
            文件存储路径为当前目录下的data文件夹
            文件名为: 年-月-日 时-分-秒_串口关键字.txt
        """
        dir_path = os.getcwd() + "\\data"
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        if self.key == "H":
            filename = datetime.datetime.now().strftime(
                "\\%Y-%m-%d %H-%M-%S") + "_Pressure.txt"
        else:
            filename = datetime.datetime.now().strftime("\\%Y-%m-%d %H-%M-%S") + \
                "_IMU_" + self.key + ".txt"
        self.file_path = dir_path + filename
        try:
            with open(self.file_path, "a") as f:
                print(filename + "创建文件成功")
        except:
            print(filename + "创建文件失败")

    def update_data(self, data: np.ndarray):
        """数据保存线程 -> 更新数据

        Args:
        ----------
            data (np.ndarray): 数据列表 -> {"A" "B" "C": [Acc, Gyr, Angle, Mag, T], "H": [16 x data]}
        """
        if self.key == "H":
            if self.data.shape[0] == 0:
                self.data = np.array(data)
            else:
                self.data = np.concatenate((self.data, data))
        else:
            Acc, Gyr, Angle, Mag, T = np.array(data, dtype=object).T
            T = T[::4]
            length = min(len(Acc), len(Gyr), len(Angle), len(Mag), len(T))
            data = np.hstack(
                (Acc[:length], Gyr[:length], Angle[:length], Mag[:length], np.array(T[:length]).reshape(-1, 1)))
            if self.data.size == 0:
                self.data = data
            else:
                self.data = np.vstack([self.data, data])

    def run(self):
        while self.is_running:
            if self.data.size != 0:
                try:
                    data = self.data
                    # 保存数据
                    with open(self.file_path, "a") as f:
                        if self.key == "H":
                            np.savetxt(f, data, fmt="%d")
                        else:
                            np.savetxt(f, data, fmt="%f")
                    self.data = np.array([])
                except Exception as e:
                    print("保存失败" + str(e))
            self.msleep(100)  # 10ms保存一次

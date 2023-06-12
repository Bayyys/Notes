import sys

sys.path.append('../..')
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFrame, QGridLayout, QSizePolicy, QHBoxLayout
from PyQt5.QtCore import Qt
from ui.sensor_info_ui.SensorInfo_ui import Ui_SensorInfo
from ui.sensor_info_ui.sensor_single_info_ui.SensorSingleInfo import SensorSingleInfo


class SensorInfo(QWidget, Ui_SensorInfo):
    """ 传感器数据信息界面
    用于显示某个传感器的数据信息, 3xIMU + 1xPressure

    Args:
    ----------------
        key[str]: 传感器类型, "A" "B" "C" 为IMU, "H" 为Pressure
    """

    def __init__(self, key: str = "A"):
        super().__init__()
        self.key = key
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.category = []  # 用于传感器数据标签
        if self.key == "H":  # 压力传感器
            self.btn_lb_X.setText("压力")
            self.info_layout = QGridLayout()  # 网格布局
            for i in range(16):
                label = QLabel(str(i + 1))  # 传感器数据标签
                font = label.font()
                font.setPointSize(12)
                label.setFont(font)
                label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置标签大小策略
                label.setFrameShape(QLabel.Box)  # 设置标签边框
                label.setAlignment(Qt.AlignCenter)  # 居中对齐
                self.category.append(label)  # 添加到列表
                self.info_layout.addWidget(label, i // 4, i % 4)  # 添加到布局

        else:  # IMU
            self.btn_lb_X.setText("IMU " + self.key)  # 设置按钮文本

            category_list = ["加速度", "角速度", "角度", "磁场"]  # 传感器数据类型列表
            self.info_layout = QHBoxLayout()  # 水平布局
            for key in category_list:
                self.category.append(SensorSingleInfo(key))  # 创建单个信息界面, 并添加到列表
                self.info_layout.addWidget(self.category[-1])  # 添加到布局
            self.lb_X_Temperature = QLabel("___℃")  # 温度标签
            self.lb_X_Temperature.setAlignment(Qt.AlignCenter)  # 居中对齐
            self.X_Info.layout().addWidget(self.lb_X_Temperature)  # 添加到布局
        font = self.btn_lb_X.font()  # 获取字体
        font.setPointSize(14)  # 设置字号
        # font.setBold(True)  # 设置加粗
        self.btn_lb_X.setFont(font)  # 设置字体
        self.info.setStyleSheet("background-color: rgb(255, 255, 255);")  # 设置背景颜色
        self.info_layout.setContentsMargins(0, 0, 0, 0)  # 设置布局边距
        self.info.setLayout(self.info_layout)  # 设置布局
        self.layout().setContentsMargins(0, 0, 0, 0)  # 设置边距

    def update(self, data=None):
        """ 更新传感器数据信息

        Args:
        ----------------
            data[dict]: 传感器数据, {"A" "B" "C": [Acc, Gyr, Angle, Mag, T], "H": [16 x data]}
        """
        if data is None:
            data = []
        if self.key == "H":  # 压力传感器
            self.update_p(data)
        else:  # IMU
            self.update_imu(data)

    def update_imu(self, data: dict):
        """ 更新IMU传感器数据信息

        Args:
        ----------------
            data[dict]: IMU传感器数据, [Acc, Gyr, Angle, Mag, T]
        """
        units = ["xg", "°/s", "°", "uT"]  # 单位列表
        for i in range(len(data) - 1):
            self.category[i].single_update_imu(data[i][-1], units[i])  # 更新单个信息界面
        self.lb_X_Temperature.setText(str(data[-1][-1]) + " ℃")  # 更新温度标签

    def update_p(self, data: dict):
        """ 更新压力传感器数据信息

        Args:
        ----------------
            data[dict]: 压力传感器数据, [16 x data]
        """
        data = data[-1]  # 获取最新压力传感器数据
        for i in range(16):
            self.category[i].setText(str(data[i]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    SensorInfo = SensorInfo()
    SensorInfo.show()
    sys.exit(app.exec_())

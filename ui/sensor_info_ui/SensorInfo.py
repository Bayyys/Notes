import sys
sys.path.append('../..')
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFrame, QGridLayout, QSizePolicy, QHBoxLayout
from PyQt5.QtCore import Qt
from ui.sensor_info_ui.SensorInfo_ui import Ui_SensorInfo
from ui.sensor_info_ui.sensor_single_info_ui.SensorSingleInfo import SensorSingleInfo

class SensorInfo(QWidget, Ui_SensorInfo):
    def __init__(self, key: str="A"):
        super().__init__()
        self.key = key
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.category = []
        if self.key == "H":
            self.btn_lb_X.setText("压力")
            self.info_layout = QGridLayout()
            for i in range(16):
                label = QLabel(str(i + 1))
                label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                label.setFrameShape(QLabel.Box)
                label.setAlignment(Qt.AlignCenter)
                self.category.append(label)
                self.info_layout.addWidget(label, i//4, i%4)

        else:
            self.btn_lb_X.setText(self.key)
            category_list = ["加速度", "角速度", "角度", "磁场"]
            self.info_layout = QHBoxLayout()
            for key in category_list:
                self.category.append(SensorSingleInfo(key))
                self.info_layout.addWidget(self.category[-1])
            self.lb_X_Temperature = QLabel("___℃")
            self.lb_X_Temperature.setAlignment(Qt.AlignCenter)
            self.X_Info.layout().addWidget(self.lb_X_Temperature)
        self.info.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.info_layout.setContentsMargins(0, 0, 0, 0)
        self.info.setLayout(self.info_layout)
        self.layout().setContentsMargins(0, 0, 0, 0)
    
    def update(self, data: dict):
        if self.key == "H":
            self.update_p(data)
        else:
            self.update_imu(data)

    def update_imu(self, data: dict):
        Acc, Gyr, Angle, Mag, T = data
        uinis = ["xg", "°/s", "°", "uT"]
        for i in range(len(data) - 1):
            self.category[i].update(data[i][-1], uinis[i])
        self.lb_X_Temperature.setText(str(T[-1]) + " ℃")
    
    def update_p(self, data: dict):
        data = data[-1]
        for i in range(16):
            self.category[i].setText(str(data[i]))
        ...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    SensorInfo = SensorInfo()
    SensorInfo.show()
    sys.exit(app.exec_())
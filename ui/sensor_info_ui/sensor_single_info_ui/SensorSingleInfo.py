import sys
sys.path.append('../../..')
from PyQt5.QtWidgets import QApplication, QFrame, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
# from ui.sensor_info_ui.sensor_single_info_ui.SensorSingleInfo_ui import Ui_SensorSingleInfo


class SensorSingleInfo(QFrame):
    def __init__(self, category: str="加速度"):
        super().__init__()
        self.category = category
        self.initUI()
    
    def initUI(self):
        self.params_list = []
        self.params = ["X", "Y", "Z"]
        self.Vlayout = QVBoxLayout()
        for i in range(3):
            label = QLabel(self.params[i])
            label.setAlignment(Qt.AlignCenter)
            self.params_list.append(label)
            self.Vlayout.addWidget(label)
        label = QLabel(self.category)
        label.setAlignment(Qt.AlignCenter)
        self.Vlayout.addWidget(label)
        self.Vlayout.setContentsMargins(0, 0, 0, 0)
        self.setFrameShape(QFrame.Box)
        self.setLayout(self.Vlayout)
        
    
    def update(self, data: dict, uinit: str):
        for i in range(len(data)):
            self.params_list[i].setText(self.params[i] + ": %.2f " % data[i] + uinit)
            ...
        ...




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    SensorSingleInfo = SensorSingleInfo()
    SensorSingleInfo.show()
    sys.exit(app.exec_())
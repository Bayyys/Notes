import sys
sys.path.append('../..')
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFrame, QGridLayout, QSizePolicy, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from ui.sensor_info_list_ui.SensorInfoList_ui import Ui_SensorInfoList
from ui.sensor_info_list_ui.sensor_single_info_list_ui.SensorSingleInfoList import SensorSingleInfoList
from ui.sensor_info_list_ui.sensor_single_info_list_ui.SensorSingleInfoList_single import SensorSingleInfoList_Single

class SensorInfoList(QWidget, Ui_SensorInfoList):
    def __init__(self, key: str="O"):
        super().__init__()
        self.key = key
        # self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        if self.key in ["O"]:
            self.Hlayout = QHBoxLayout()    # 水平布局
            categorys = ["加速度", "角速度", "角度", "磁场"]    # 类别列表
            units = ["xg", "°/s", "°", "uT"]    # 单位列表
            s_categorys = ["温度"]
            s_units = ["℃"]
            # 名称
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(1)
            sizePolicy.setVerticalStretch(1)
            form = SensorSingleInfoList_Single("连接名称")    # 创建一个单个传感器信息
            form.setSizePolicy(sizePolicy)
            self.Hlayout.addWidget(form)  # 添加到布局
            # 传感器数据
            self.category = []  # 用于传感器数据标签
            sizePolicy.setHorizontalStretch(3)
            for i in range(len(categorys)):
                form = SensorSingleInfoList(categorys[i], units[i])
                form.setSizePolicy(sizePolicy)
                self.category.append(form)
                self.Hlayout.addWidget(form)

            sizePolicy.setHorizontalStretch(1)
            for i in range(len(s_categorys)):
                form = SensorSingleInfoList_Single(s_categorys[i], s_units[i])
                form.setSizePolicy(sizePolicy)
                self.category.append(form)
                self.Hlayout.addWidget(form)
            self.setLayout(self.Hlayout)   # 设置布局
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.setSizePolicy(sizePolicy)
        else:
            

            ...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SensorInfoList()
    window.show()
    sys.exit(app.exec_())
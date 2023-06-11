import sys
sys.path.append('../..')
from PyQt5.QtWidgets import QApplication, QFrame, QVBoxLayout, QLabel, QHBoxLayout, QTextEdit, QSizePolicy
from PyQt5.QtCore import Qt

class SensorPrint(QFrame):
    ''' 传感器数据打印界面
    用于显示传感器数据的打印界面, 包括 原始数据(HEX)、解析数据(str)'''
    def __init__(self, key: str="A"):
        super().__init__()
        self.key = key  # 传感器类型 -> A/B/C: IMU H: Pressure
        self.initUI()
    
    def initUI(self):
        self.Hlayout = QHBoxLayout()    # 垂直布局
        # 设置标签
        self.label = QLabel(self.key)  # 标签
        self.label.setAlignment(Qt.AlignCenter)  # 居中对齐
        # 设置水平策略 Expanding, 垂直策略 Fixed
        label_sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        label_sizePolicy.setHorizontalStretch(1)
        self.label.setSizePolicy(label_sizePolicy)
        # 原始数据(HEX)
        self.et_hex = QTextEdit()
        self.et_hex.append("欢迎使用 IMU & 压力 传感器测试工具！\n\n")
        self.et_hex.setReadOnly(True)   # 设置只读
        # 解析数据(str)
        self.et_str = QTextEdit()
        self.et_str.setReadOnly(True)   # 设置只读
        et_sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        et_sizePolicy.setHorizontalStretch(9)
        self.et_hex.setSizePolicy(et_sizePolicy)
        self.et_str.setSizePolicy(et_sizePolicy)
        self.Hlayout.addWidget(self.label)   # 添加到布局
        self.Hlayout.addWidget(self.et_hex)    # 添加到布局
        self.Hlayout.addWidget(self.et_str)    # 添加到布局
        self.setLayout(self.Hlayout)    # 设置布局
    
    def update(self, hex_data: str="", str_data: str=""):
        self.update_hex(hex_data)
        self.update_str(str_data)
    
    def update_hex(self, hex_data: str=""):
        ''' 更新原始数据(HEX)
        由传感器信息界面调用，根据传感器数据类型更新界面

        Args:
        ----------------
            hex_data[str]: 原始数据(HEX)
        '''
        self.et_hex.append(hex_data)
    
    def update_str(self, str_data: str=""):
        ''' 更新解析数据(str)
        由传感器信息界面调用，根据传感器数据类型更新界面

        Args:
        ----------------
            str_data[str]: 解析数据(str)
        '''
        self.et_str.append(str_data)
    

if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    SensorPrint = SensorPrint()
    SensorPrint.show()
    sys.exit(app.exec_())

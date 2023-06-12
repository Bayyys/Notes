import sys
sys.path.append('../../..')
from PyQt5.QtWidgets import QApplication, QFrame, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class SensorSingleInfo(QFrame):
    ''' 传感器数据单个信息界面 
    用于显示传感器数据的单个信息, 即 加速度、角速度、角度、磁场 
    
    Args
    ----------------
        category[str]: 传感器数据类型
    '''
    def __init__(self, category: str="加速度"):
        super().__init__()
        self.category = category    # 传感器数据类型
        self.initUI()
    
    def initUI(self):
        self.params_list = []   # 用于传感器数据标签
        self.params = ["X", "Y", "Z"]   # 传感器数据 xyz 标签
        self.Vlayout = QVBoxLayout()    # 垂直布局
        for i in range(3):
            label = QLabel(self.params[i])  # 传感器数据标签
            label.setAlignment(Qt.AlignCenter)  # 居中对齐
            # 设置字号, 并加粗
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)
            self.params_list.append(label)  # 添加到列表
            self.Vlayout.addWidget(label)   # 添加到布局
        label = QLabel(self.category)   # 传感器数据类型标签, 根据 category 参数确定
        font = label.font()
        font.setBold(True)
        font.setPointSize(12)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)  # 居中对齐
        self.Vlayout.addWidget(label)   # 添加到布局
        self.Vlayout.setContentsMargins(0, 0, 0, 0) # 设置布局边距
        self.setFrameShape(QFrame.Box)  # 设置边框
        self.setLayout(self.Vlayout)    # 设置布局
        
    def single_update_imu(self, data: dict, uint: str):
        ''' 更新 imu 数据
        由传感器信息界面调用，根据传感器数据类型更新界面

        Args:
        ----------------
            data[dict]: 传感器数据
            uint[str]: 单位
        '''
        for i in range(len(data)):
            self.params_list[i].setText(self.params[i] + ": %.2f " % data[i] + uint)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    SensorSingleInfo = SensorSingleInfo()
    SensorSingleInfo.show()
    sys.exit(app.exec_())
import sys
sys.path.append('../../..')
from PyQt5.QtWidgets import QApplication, QFrame, QVBoxLayout, QLabel, QHBoxLayout, QTextEdit, QSizePolicy, QGridLayout
from PyQt5.QtCore import Qt

class SensorSingleInfoList_Single(QFrame):
    def __init__(self, category: str="连接名称", unit: str="") -> None:
        super().__init__()
        self.category = category
        self.unit = unit
        self.initUI()
    
    def initUI(self):
        self.setLayout(QVBoxLayout())   # 垂直布局
        self.setFrameStyle(QFrame.Box | QFrame.Raised)  # 设置边框样式
        self.info = QLabel(self.category)  # 单个名称
        self.info.setAlignment(Qt.AlignCenter)  # 居中对齐
        self.layout().addWidget(self.info)  # 添加到布局
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        self.info.setSizePolicy(sizePolicy)
        if self.category != "连接名称":
           self.info.setText(self.category + "(" + self.unit + ")")  # 设置文本 

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    SensorSingleInfoList_Single = SensorSingleInfoList_Single()
    SensorSingleInfoList_Single.show()
    sys.exit(app.exec_())


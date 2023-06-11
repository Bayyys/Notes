import sys
sys.path.append('../../..')
from PyQt5.QtWidgets import QApplication, QFrame, QVBoxLayout, QLabel, QHBoxLayout, QTextEdit, QSizePolicy, QGridLayout
from PyQt5.QtCore import Qt

class SensorSingleInfoList(QFrame):
    def __init__(self, category: str="加速度", unit: str="xg") -> None:
        super().__init__()
        self.category = category
        self.unit = unit
        self.initUI()
    
    def initUI(self):
        self.Glayout = QGridLayout()    # 网格布局
        self.lb_title = QLabel(str(self.category+"("+self.unit+")"))  # 标题
        self.lb_title.setAlignment(Qt.AlignCenter)  # 居中对齐
        self.lb_title.setFrameShape(QFrame.StyledPanel)  # 设置边框样式
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        self.lb_title.setSizePolicy(sizePolicy)
        self.Glayout.addWidget(self.lb_title, 0, 0, 1, 3)   # 添加到布局
        sizePolicy.setHorizontalStretch(1)
        for axis in ["X", "Y", "Z"]:
            label = QLabel("Axis " + axis)
            label.setAlignment(Qt.AlignCenter)  # 居中对齐
            label.setSizePolicy(sizePolicy)
            self.Glayout.addWidget(label, 1, ord(axis) - ord("X"), 1, 1)   # 添加到布局
        self.Glayout.setContentsMargins(0, 0, 0, 0)    # 设置边距
        self.setLayout(self.Glayout)    # 设置布局
        self.setFrameStyle(QFrame.Box | QFrame.Raised)  # 设置边框样式
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHorizontalStretch(3)
        self.setSizePolicy(sizePolicy)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    SensorSingleInfoList = SensorSingleInfoList()
    SensorSingleInfoList.show()
    sys.exit(app.exec_())


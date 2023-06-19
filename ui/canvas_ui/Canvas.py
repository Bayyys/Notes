import sys
sys.path.append('../..')
import numpy as np
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QFrame
from ui.canvas_ui.canvas_ui import Ui_Frame
import pyqtgraph as pg

class Canvas(pg.PlotWidget):
    '''FFT 绘图 canvas'''
    def __init__(self, key: str="A"):
        super().__init__()
        self.key=key
        self.initData()
    
    def initData(self):
        self.curve_list = []
        color_list = ['r', 'b', 'g']
        name_lsit = ['roll', 'pitch', 'yaw']
        data = np.zeros(1000)
        # 设置标题
        self.setTitle("IMU "+self.key+"(°)", color="k", size="14pt", bold=True)
        legend = pg.LegendItem(offset=(-1, 1), verSpacing=-10, horSpacing=20, labelTextColor='k')
        legend.setParentItem(self.graphicsItem())
        for i in range(3):
            curve = self.plot(pen=pg.mkPen(color=color_list[i], width=2), name=name_lsit[i], width=5)
            curve.setData(np.zeros(1))
            legend.addItem(curve, name_lsit[i])
            self.curve_list.append(curve)
        self.setBackground('w')  # 设置背景颜色
        self.showGrid(x=True, y=True)  # 显示网格
        self.is_not_full = True

class CanvasWidget(QFrame, Ui_Frame):
    def __init__(self, key: str="A") -> None:
        super().__init__()
        try:
            self.ui = uic.loadUi('ui/canvas_ui/canvas_ui.ui', self)
        except:
            self.ui = uic.loadUi('./canvas_ui.ui', self)
        self.key=key
        self.length=500
        # self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.Hlayout = QHBoxLayout()
        self.Hlayout.setContentsMargins(0, 0, 0, 0)
        self.cavas = Canvas(self.key)
        self.Hlayout.addWidget(self.cavas)
        self.canvas_frame.setLayout(self.Hlayout)
        self.btn_lb_X.setText(self.key)
        self.setContentsMargins(0, 0, 0, 0)
    
    def update_imu_data(self, datas):
        for data in datas:
            if self.cavas.is_not_full:
                for i in range(3):
                    set_data = np.append(self.cavas.curve_list[i].getData()[1], data[i])[-self.length:]
                    self.cavas.curve_list[i].setData(set_data)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = CanvasWidget()
    widget.show()
    sys.exit(app.exec_())
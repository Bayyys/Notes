import sys
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFrame
from PyQt5.QtCore import Qt, QTimer
from scipy.signal import butter, filtfilt
import time

class myCanvas(FigureCanvas):
    def __init__(self):
        global isCollecting
        global xdata
        global ydata
        global sampleRate
        global b, a
        self.fig, self.ax = plt.subplots()
        self.ax.set_ylim(-100, 100)
        self.ax.set_xlim(0, 800)
        self.line, = self.ax.plot([], [])
        FigureCanvas.__init__(self, self.fig)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(1)  # 更新时间间隔为50ms

    def update_figure(self):
        if isCollecting:
        #     self.line.set_data(xdata, ydata)
            print(len(xdata))
            self.draw()
            print(time.time())
        ...
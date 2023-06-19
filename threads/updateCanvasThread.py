import sys
sys.path.append('..')
from PyQt5 import QtCore
from ui.canvas_ui.Canvas import CanvasWidget

class UpdateCanvasThread(QtCore.QThread):
    def __init__(self, key: str, canvas: CanvasWidget):
        super().__init__()
        self.key = key
        self.canvas = canvas
        self.is_running = True
        self.isUpdate = False
        self.data = []
    
    def __del__(self):
        self.is_running = False
    
    def update_data(self, data: list):
        if self.data != []:
            self.data += data
        else:
            self.data = data
        self.isUpdate = True

    def run(self):
        while self.is_running:
            if self.isUpdate:
                data = self.data
                self.data = []
                self.canvas.update_imu_data(data)
                self.isUpdate = False
            self.msleep(100)
    

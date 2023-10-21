from enum import auto
from operator import index
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.patches as patches
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QMessageBox,
)
from scipy import optimize
from shapely.geometry import Polygon, LineString, MultiLineString, Point
from shapely.affinity import translate, scale  # translate 库用来平移多边形; scale 库用来缩放多边形
import math
import random

from gui.main import Ui_MainWindow
from Item import *

plt.ion()

TEST_BENCH = "testbench.csv"
MIN_DISTANCE = 30


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initParams()

        # 载入测试数据
        self.load_testbench()

        # matplotlib
        self.fig, self.ax = plt.subplots()
        self.init_raster()
        self.on_comboBox_select(0)

        self.comboBox.currentIndexChanged.connect(self.on_comboBox_select)
        self.pushButton_init_layout.clicked.connect(self.init_reset)
        self.pushButton_manual_optimize.clicked.connect(self.manual_optimize_group)
        self.pushButton_auto_optimize.clicked.connect(self.auto_optimize)

        self.initGroup()

    # 初始化参数
    def initParams(self):
        self.Areas: list[float] = [
            15300,
            8000,
            10700,
            9000,
            10000,
            13900,
            15000,
            15500,
            11000,
            12300,
            13200,
        ]
        self.gap: float = 30
        self.W: float = 600
        self.H: float = 400
        self.ratio_spec = 0
        self.P: list[MyPolygon] = []
        self.new_group: list[Polygon] = []
        self.round: int = 0
        self.ST_list = [
            "S1",
            "T1",
            "T4",
            "T5",
            "S2",
            "S3",
            "S4",
            "S5",
            "T2",
            "T3",
            "S6",
        ]
        MY_FLAG.flag = False

    # 按照 self.ST_list 顺序重新排列面积
    def sortAreas(self):
        num_list = self.df.columns[: len(self.Areas)].tolist()
        self.sort_Areas = [self.Areas[num_list.index(index)] for index in self.ST_list]

    # 初始化多边形组
    def initGroup(self):
        self.group = Group(self.sort_Areas, self.gap, self.W, self.H, self.ax)

    # 初始化布局
    def init_reset(self):
        self.ax.clear()
        for i in range(len(self.ST_list)):
            exec(f"self.label_{self.ST_list[i]}.setText(str(self.ST_list[i]))")
        self.lineEdit_ratio_real.setText("")
        self.init_raster()
        self.initGroup()
        self.new_group = []

    # 单步调优
    def optimize_step(self):
        try:
            self.group.next()
            polygon = self.adjust_polygon(self.group.P[self.group.round - 1].polygon)
            self.new_group.append(polygon)
            self.plot_polygon(polygon)
            exec(
                f"self.label_{self.ST_list[self.group.round - 1]}.setText(','.join(map(self.str_format,self.get_coords_from_bottom_left(polygon))))"
            )
        except Exception as e:
            print(e)
            QMessageBox.warning(
                self,
                "错误",
                "排布失败, 请重新初始化",
                QMessageBox.StandardButton.Ok,
            )
            self.init_reset()
            raise Exception("排布失败, 请重新初始化")

    # 调节多边形适应边框
    def adjust_polygon(self, polygon: Polygon):
        points: list = []
        # 如果不满足 0<=x<=self.Width, 0<=y<=self.Height, 则修改该点坐标至边界线上
        for i in range(len(polygon.exterior.coords)):
            x, y = polygon.exterior.coords[i]
            if x < 0:
                x = 0
            elif x > self.W:
                x = self.W
            if y < 0:
                y = 0
            elif y > self.H:
                y = self.H
            points.append((x, y))
        return Polygon(points)

    # 手动调优
    def manual_optimize_group(self):
        if self.group.round < len(self.sort_Areas):
            try:
                self.optimize_step()
                if self.group.round == len(self.sort_Areas):
                    self.cal_area_ratio()
            except:
                pass
        else:
            # 弹出对话框, 提示已经完成, 是否重新开始
            result = QMessageBox.information(
                self,
                "提示",
                "已经完成, 是否重新开始",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            match result:
                case QMessageBox.StandardButton.Yes:
                    self.init_reset()
                case QMessageBox.StandardButton.No:
                    print("No")

    # 自动调优
    def auto_optimize(self):
        if self.group.round != 0:
            self.init_reset()
            self.auto_optimize()
        else:
            try:
                for i in range(len(self.sort_Areas)):
                    self.optimize_step()
                self.cal_area_ratio()
            except:
                ...

    # 绘制多边形
    def plot_polygon(self, polygon: Polygon):
        current_centroid_coords = polygon.centroid.coords[0]
        x, y = polygon.exterior.xy
        type = self.ST_list[self.group.round - 1]

        if type.startswith("S"):
            self.ax.fill(
                x, y, alpha=0.5, fc="blue", ec="black"
            )  # fc and ec are facecolor and edgecolor respectively
            self.ax.plot(*current_centroid_coords, "ro")  # red dot for specified center
        elif type.startswith("T"):
            self.ax.fill(
                x, y, alpha=0.5, fc="red", ec="black"
            )  # fc and ec are facecolor and edgecolor respectively
            self.ax.plot(
                *current_centroid_coords, "bo"
            )  # blue dot for specified center
        else:
            print("string should begin with S or T")

        self.ax.annotate(
            type,
            (current_centroid_coords[0], current_centroid_coords[1]),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

    # 计算面积占空比
    def cal_area_ratio(self):
        PolygonCollection = GeometryCollection(self.new_group)
        # 最小外接矩形
        minx, miny, maxx, maxy = PolygonCollection.bounds
        bounds_matrix_area = (maxx - minx) * (maxy - miny)
        self.lineEdit_ratio_real.setText(
            str(f"{PolygonCollection.area * 100 / bounds_matrix_area:.2f}")
        )

    # 初始化栅格
    def init_raster(self):
        self.ax.clear()
        off = 5
        self.ax.set_aspect("equal")
        self.ax.set_xlim(-off, self.W + off)
        self.ax.set_ylim(-off, self.H + off)

        plt.grid(True, which="both")
        plt.show()

    # 下拉框选择
    def on_comboBox_select(self, index):
        for i in range(len(self.df.columns)):
            if self.df.columns[i].startswith("S") or self.df.columns[i].startswith("T"):
                self.Areas[i] = self.df.iloc[index][i]
            elif self.df.columns[i].startswith("ratio_spec"):
                exec(f"self.ratio_spec=self.df.iloc[index][i]")
                exec(f"self.lineEdit_ratio_set.setText(str(self.ratio_spec))")
                continue
            else:
                exec(f"self.{self.df.columns[i]}=self.df.iloc[index][i]")
            exec(
                f"self.lineEdit_{self.df.columns[i]}.setText(str(int(self.df.iloc[index][i])))"
            )
        self.sortAreas()
        self.init_raster()

    # 加载数据
    def load_testbench(self):
        self.df = pd.read_csv(TEST_BENCH, index_col=0)
        self.comboBox.clear()
        self.comboBox.addItems(self.df.index.tolist())

    # 坐标输出格式
    def str_format(self, number):
        return f"({number[0]:.0f}, {number[1]:.0f})"

    # 从左下角开始顺时针获取坐标
    def get_coords_from_bottom_left(self, pentagon):
        coords = list(pentagon.exterior.coords)[:-1]
        bottom_left = min(coords, key=lambda v: (v[1], v[0]))
        index_bottom_left = coords.index(bottom_left)
        reordered_coords = coords[index_bottom_left:] + coords[:index_bottom_left]
        return reordered_coords


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

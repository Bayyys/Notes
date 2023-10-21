import sys
from types import FunctionType
from tqdm import tqdm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from shapely import (
    Polygon,
    LineString,
    MultiLineString,
    Point,
    affinity,
    plotting,
    GeometryCollection,
    LinearRing,
)
from shapely.ops import orient  # orient 库用来判断多边形的方向
import math
import random
import rules

plt.ion()


class Item:
    """单个谐振器(多边形)"""

    def __init__(self, area: float = 10000) -> None:
        """单个谐振器(多边形)

        Args:
            area (float): 谐振器面积
        """
        super().__init__()
        self.area = area
        self.edge = random.randint(5, 6)
        self.polygon: Polygon = rules.generate_regular_polygon(self.edge, self.area)

    def get_item_coords_array(self) -> np.ndarray:
        """得到多边形的顶点坐标

        Returns:
            np.ndarray: 多边形顶点坐标
        """
        if len(self.polygon.exterior.coords) - 1 == 6:
            return np.asarray(self.polygon.exterior.coords)[:-1]
        else:
            return np.asarray(self.polygon.exterior.coords)

    def compute_area_with_set(self) -> float:
        return abs(self.polygon.area - self.area)

    def compute_item_parallel(self) -> float:
        return rules.edges_not_parallel(self.polygon)

    def get_polygon_edges(self) -> list[tuple]:
        coords = list(self.polygon.exterior.coords)
        edges = [(coords[i], coords[i + 1]) for i in range(len(coords) - 1)]
        return edges

    def get_coords_from_bottom_left(self):
        ...

    def update_polygon(self, new_coords: np.ndarray) -> None:
        # TODO: 解决自相交问题
        self.polygon = Polygon(new_coords)


class Group:
    """谐振器组合(多边形组合) 11个

    Args:
        Areas (list[float], optional): 谐振器面积. Defaults to [ 1000, ].
    """

    def __init__(
        self,
        Areas: list[float] = [
            1000,
        ],
        Width: float = 600,
        Height: float = 400,
    ) -> None:
        """谐振器组合(多边形组合) 11个

        Args:
            Areas (list[float], optional): 谐振器面积. Defaults to [ 1000, ].
            Width (float, optional): 谐振器宽度. Defaults to 600.
            Height (float, optional): 谐振器高度. Defaults to 400.
        """
        super().__init__()
        """
        id     case     S1     S2     S3     S4     S5     S6     T1     T2     T3     T4     T5   gap   W    H    ratio_spec_(%)
        0    case_1  15300  10000  13900  15000  15500  13200   8000  11000  12300  10700   9000   30  600  400           55.79
        1    case_2   8000   9000  12000  12000  13000  11000   7000   6000   5000   8500   5000   30  600  400           40.21
        2    case_3   7600   9500  10100  10500   8500  10300  14200  11500  12400   9700   8700   30  600  400           47.08
        3    case_4  14000   8200  12300   8900  13300  11400  11800  12500  10300   9200   8900   30  600  500           40.27
        4    case_5  11500   7500  22000  10000  11000  13500  12000  12500   8500  18000  18600   30  600  500           48.37
        5    case_6  21500  13000  12500  17000  24000  17000   9800   8500  10800  15900  10000   30  600  500           53.33
        6    case_7  24500   6500  17500   7500   9000  22500   9000  16500  17500   7500   9000   30  700  500           42.00
        7    case_8  19500  14300  10800  25000  11100  17300  16500  11500   7900  14900  10600   30  700  500           45.54
        8    case_9  10800   7500  19500  27000  19100   8100  17700   9800  15300   8400   9900   30  700  600           36.45
        9   case_10  20700  11300  11800  21000  10400  23000  18300  16500  11100  15300  19800   30  700  600           42.67
        10   custom  15300  10000  13900  15000  15500  13200   8000  11000  12300  10700   9000   30  600  400           55.80
        """
        self.Areas: list[float] = Areas
        self.Width: float = Width
        self.Height: float = Height
        # self.fig, self.ax = plt.subplots()
        # self.ax.set_aspect("equal")
        # self.ax.set_xlim(0, self.Width)
        # self.ax.set_ylim(0, self.Height)
        self.initPolygons()

    def initPolygons(self) -> None:
        """初始化谐振器组合"""
        self.polygons: list[Item] = []
        for i in range(len(self.Areas)):
            self.polygons.append(Item(self.Areas[i]))
            dx = i % 4 * self.Width / 4 + self.Width / 8
            if i == len(self.Areas) - 1:  # 右上角多边形需要空一个位置
                dx += self.Width / 4
            dy = i // 4 * self.Height / 3 + self.Height / 6
            self.polygons[i].polygon = affinity.translate(
                self.polygons[i].polygon, dx, dy
            )
        # self.show()

    def show(self):
        for polygon in self.polygons:
            self.ax.plot(*polygon.polygon.exterior.xy)
            print(polygon.polygon.area)
            print(polygon.polygon.centroid)
        plt.show()

    def compute_group_area(self):
        p = rules.get_min_bounding_rectangles(
            GeometryCollection([p.polygon for p in self.polygons])
        )
        return p.area

    def get_point_num_array(self) -> np.ndarray:
        """返回多边形的顶点个数

        Returns:
            np.ndarray: 多边形顶点个数
        """
        return np.array([len(p.polygon.exterior.coords) - 1 for p in self.polygons])

    def get_coords_array(self) -> np.ndarray:
        """返回多边形的顶点坐标

        Returns:
            np.ndarray: 多边形顶点坐标
        """
        return np.array([p.get_item_coords_array() for p in self.polygons])


class Q:
    def __init__(self, N: int = 5) -> None:
        self.N = N  # 初始种群个数
        self.Areas = [
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
        self.minS = 30
        self.Width = 600
        self.Height = 400
        self.initParams()
        # self.drawInit()

    def initParams(self):
        # ------- 约束项函数初始化 -------
        self.conFuncs: list[FunctionType] = [
            self.penalty_area_equal_set,
            self.penalty_item_not_parallel,
        ]
        # ------- PSO 超参数设置 -------
        self.xlimit: list[float] = [0, self.Width]  # x轴 限制条件
        self.ylimit: list[float] = [0, self.Height]  # y轴 限制条件
        self.vlimit: list[float] = [-10, 10]  # 速度限制
        self.w: int = 0.8  # 惯性权重
        self.c1: int = 0.5  # 个体学习因子
        self.c2: int = 0.5  # 群体学习因子
        # ------ 谐振器初始化 ------
        self.G: list[Group] = [
            Group(self.Areas, self.Width, self.Height) for i in range(self.N)
        ]  # 初始化位置
        self.pointN: np.ndarray = self.compute_num_of_points()  # 计算每个多边形的顶点个数
        # ----- PSO 参数初始化 -----
        self.x: np.ndarray = np.array(
            [g.get_coords_array() for g in self.G]
        )  # 初始化位置 [N, 11, 6, 2]
        self.v: np.ndarray = np.random.uniform(
            self.vlimit[0], self.vlimit[1], (self.N, len(self.Areas), 6, 2)
        )  # 初始化速度
        self.xm: np.ndarray = self.x  # 个体最优位置
        self.ym: np.ndarray = self.xm[0]  # 种群历史最优位置
        self.fxm: np.ndarray = np.ones(((self.N, 1))) * float("inf")  # 个体历史最佳适应度
        self.fym: float = float("inf")  # 种群历史最佳适应度
        print(self.fym)
        return

    def compute_num_of_points(self) -> np.ndarray:
        """计算每个多边形的顶点个数

        Returns:
            np.ndarray: 多边形顶点个数的矩阵
        """
        return np.array([g.get_point_num_array() for g in self.G])

    # 适应度函数
    def func(self, x: np.ndarray = np.empty([]), ger: int = 0) -> np.ndarray:
        """计算适应度函数

        Args:
            x (np.ndarray, optional): 位置坐标. Defaults to np.empty([]).

        Returns:
            np.ndarray: 适应度函数值
        """
        o = self.objective(x)
        h = self.penalty_coeff(ger) * self.constraints()
        print(np.min(o), np.min(h))
        return o + h
        # return self.objective(x) + self.penalty_coeff(ger) * self.constraints()

    # 目标函数项
    def objective(self, G: list[Group]) -> np.ndarray:
        """

        Args:
            G (list[Group]):

        Returns:
            np.ndarray: _description_
        """
        return np.array([Ps.compute_group_area() for Ps in G]).reshape((-1, 1))

    # 惩罚系数
    def penalty_coeff(self, k: int, type: bool = True) -> float:
        """计算惩罚系数

        Args:
            k (int): 迭代次数
            type (bool): 惩罚系数计算方式, True 为 k*sqrt(k), False 为 sqrt(k)

        Returns:
            float: 惩罚系数
        """
        return k * math.sqrt(k) if type else math.sqrt(k)

    # 约束项
    def constraints(self) -> np.ndarray:
        # 约束的惩罚项
        # ConFun = penalty_coeff(k) * H(x)
        #   penalty_coeff(k) = sqrt(k) or k * spart(k)
        #   H(x) = theta(q_i) * q_i ^ gamma(q_i)
        H = np.zeros((self.N, 1))
        for confun in self.conFuncs:
            H += confun()
        return H

    # 约束计算
    def compute_constrains(self, g_i: np.ndarray) -> np.ndarray:
        """计算惩罚约束项"""
        q_i = self.penalty(g_i)
        return self.theta(q_i) * q_i ** self.gamma(q_i)

    # 相对约束惩罚函数
    def penalty(self, g_i: np.ndarray) -> np.ndarray:
        """相对约束惩罚函数
        penalty = max(0, g_i)
        """
        return np.array([max(np.array([0]), g) for g in g_i]).reshape((-1, 1))

    # 分段赋值函数
    def theta(self, q_i: np.ndarray) -> np.ndarray:
        """分段赋值函数
        theta(q_i) = 10, q_i < 0.001
        theta(q_i) = 20, 0.001 <= q_i < 0.1
        theta(q_i) = 100, 0.1 <= q_i < 1
        theta(q_i) = 300, o.w.

        Args:
            q_i (np.ndarray): 相对约束惩罚函数

        Returns:
            np.ndarray: 分段赋值系数
        """
        return np.array(
            [10 if q < 0.001 else 20 if q < 0.1 else 100 if q < 1 else 300 for q in q_i]
        ).reshape((-1, 1))

    # 惩罚指数
    def gamma(self, q_i: np.ndarray) -> np.ndarray:
        """惩罚指数
        gamma(q_i) = 1, q_i < 1
        gamma(q_i) = 2, o.w.
        """
        return np.array([1 if q < 1 else 2 for q in q_i]).reshape((-1, 1))

    # 面积相等约束项    # TODO: 约束项计算有问题
    def penalty_area_equal_set(self) -> np.ndarray:
        H = np.zeros((self.N, 1))
        for i in range(len(self.Areas)):
            g_i = np.array(
                [self.G[j].polygons[i].compute_area_with_set() for j in range(self.N)]
            ).reshape((-1, 1))
            H += self.compute_constrains(g_i)
        return H

    # 对边不平行约束项
    def penalty_item_not_parallel(self) -> np.ndarray:
        H = np.zeros((self.N, 1))
        for i in range(len(self.Areas)):
            g_i = np.array(
                [self.G[j].polygons[i].compute_item_parallel() for j in range(self.N)]
            ).reshape((-1, 1))
            H += self.compute_constrains(g_i)
        return H

    # 四角为直角约束项  # TODO
    def penalty_item_is_square(self) -> np.ndarray:
        H = np.zeros((self.N, 1))
        for i in range(len(self.Areas)):
            g_i = H
            H += self.compute_constrains(g_i)
        return H

    # 临边平行约束项    # NOTE: 临边选取方式有问题
    def penalty_neighbor_item_parallel(self) -> np.ndarray:
        H = np.zeros((self.N, 1))
        for i in range(len(self.Areas)):
            g_i = np.array(
                [self.G[j].polygons[i].compute_area_with_set() for j in range(self.N)]
            ).reshape((-1, 1))
            H += self.compute_constrains(g_i)
        return H

    # 间距约束项    # TODO
    def penalty_item_gap(self) -> np.ndarray:
        H = np.zeros((self.N, 1))
        for i in range(len(self.Areas)):
            # 找到该多边形的相邻多边形
            neighbor_index = [
                i - 1,
                i + 1,
                i - 4,
                i + 4,
            ]
            g_i = np.array(
                [self.G[j].polygons[i].compute_area_with_set() for j in range(self.N)]
            ).reshape((-1, 1))
            H += self.compute_constrains(g_i)
        return H

    def run(self, Ger: int = 20) -> None:
        for i in tqdm(range(Ger), desc="迭代进度"):
            self.update(i + 1)
            plt.pause(0.01)
        self.show()

    def update(self, ger: int = 0) -> None:
        self.fx = self.func(self.G, ger)
        for i in range(1, self.N):
            if self.fx[i] < self.fxm[i]:
                self.xm[i] = self.x[i]
                self.fxm[i] = self.fx[i]

        if np.min(self.fxm) < self.fym:
            self.ym = self.xm[np.argmin(self.fxm)]
            self.fym = np.min(self.fxm)
        # print(self.fym)

        self.v = (
            self.w * self.v
            + self.c1 * np.random.rand() * (self.xm - self.x)
            + self.c2 * np.random.rand() * (self.ym - self.x)
            # + 质心移动
        )

        self.v[self.v < self.vlimit[0]] = self.vlimit[0]
        self.v[self.v > self.vlimit[1]] = self.vlimit[1]

        self.x = self.x + self.v
        self.x[self.x < self.xlimit[0]] = self.xlimit[0]
        self.x[self.x > self.xlimit[1]] = self.xlimit[1]

        self.update_G()

    def show(self) -> None:
        """按照 self.ym 的点 绘制点图"""
        print(f"最优解: {self.fym}")
        # print("最优解取值为: ", self.ym)
        plt.figure("最优解")
        plt.xlim(0, self.Width)
        plt.ylim(0, self.Height)
        plt.gca().set_aspect("equal", adjustable="box")
        for i in range(len(self.Areas)):
            plt.plot(*self.ym[i].T)

    def update_G(self) -> None:
        """由 self.x 更新 self.G"""
        for i in range(self.N):
            for j in range(len(self.Areas)):
                self.G[i].polygons[j].update_polygon(self.x[i][j])
        self.x: np.ndarray = np.array(
            [g.get_coords_array() for g in self.G]
        )  # 初始化位置 [N, 11, 6, 2]


if __name__ == "__main__":
    q = Q(100)
    q.run(100)
    # 等待按键 q 关闭
    plt.waitforbuttonpress()

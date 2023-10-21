from re import M
from exceptiongroup import catch
import numpy as np
from shapely import (
    Point,
    Polygon,
    affinity,
    LineString,
    oriented_envelope,
    GeometryCollection,
    LinearRing,
    MultiPoint,
    plotting,
)
import random
import math
from shapely.ops import nearest_points
import matplotlib.pyplot as plt
from tools import *

plt.ion()


class MyPoint:
    def __init__(self, x, y, type: int = 0, limit_x=None, limit_y=None):
        super().__init__()
        self.x = x
        self.y = y
        self.type = type  # 0: 完全不可动 1: 只可切除 2: y轴可动 3: x轴可动 4: 完全可动
        self.limit_x = limit_x
        self.limit_y = limit_y

    @property
    def limit(self):
        if self.type == 3:
            return self.limit_x
        if self.type == 2:
            return self.limit_y

    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def point(self):
        return Point(self.x, self.y)

    def distance(self, p):
        return self.point.distance(p.point)

    def slope(self, p):
        if self.x == p.x:
            return float("inf")
        return (self.y - p.y) / (self.x - p.x)

    def __str__(self):
        # return f"({self.x}, {self.y}) --- type: {self.type} --- limit: {self.limit}"
        return f"({self.x}, {self.y})"

    def __eq__(self, __value: object) -> bool:
        if abs(self.x - __value.x) < 0.001 and abs(self.y - __value.y) < 0.001:
            return True
        return False


class MyPolygon:
    def __init__(self, points):
        super().__init__()
        self.points = points
        self.OLD_POINTS = points.copy()
        self.AREA = self.polygon.area

    @property
    def polygon(self):
        return self.generate_polygon(self.points)

    def update(self):
        self.OLD_POINTS = self.points.copy()

    def reset(self):
        self.points = self.OLD_POINTS.copy()

    @property
    def area(self):
        return self.polygon.area

    def generate_polygon(self, points):
        try:
            p = Polygon(LineString([(p.x, p.y) for p in points]))
        except:
            my_print("generate_polygon error")
            my_print(f"points: {[p.pos for p in points]}")
            p = Polygon(LineString([(0, 0), (0, 1), (1, 1), (1, 0)]))
        return Polygon(LineString([(p.x, p.y) for p in points]))

    def show_polygon(self):
        # self.check_parallel()
        plotting.plot_polygon(self.polygon)

    def check_parallel(self):
        parallel_edges = find_parallel_edges(self.points)
        while len(parallel_edges) > 0:
            self.fix_parallel_edges(parallel_edges)
            parallel_edges = find_parallel_edges(self.points)

    def fix_parallel_edges(self, parallel_edges):
        my_print("fix_parallel_edges")
        point = random.choice(parallel_edges)
        for p in self.points:
            if p.pos == point:
                choose = p
                break
        while choose.type == 4 or choose.type == 0:
            point = random.choice(parallel_edges)
            for p in self.points:
                if p.pos == point:
                    choose = p
                    break
        self.move_point_get(point)

    # 随机选择一个可动点
    def get_random_point(self):
        points = self.points
        p = random.choice(points)
        # while p.type != 4:
        while p.type == 4 or p.type == 0:
            p = random.choice(points)
        return p

    # 移动多边形中的一个点
    def move_point_get(self, point):
        (p1, p2) = self.get_suitable_edge_of_point(point)  # 获取该点所在的边
        limit = point.limit if point.limit != None else (p2.x - p1.x, p2.y - p1.y)
        edge_length = np.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)  # 计算边长
        e = random.uniform(0.05, 0.15) * edge_length  # 限制移动距离
        e = e if random.random() > 0.5 else -e  # 随机正负
        unit_v = compute_unit_vector(limit)  # 计算单位向量
        (point.x, point.y) = (
            point.x + unit_v[0] * e,
            point.y + unit_v[1] * e,
        )  # 计算移动后的坐标
        self.get_fix_edge(point, limit)  # 修补面积

    def get_fix_edge(self, point, limit):
        area_off = self.AREA - self.polygon.area  # 计算面积差
        flag = True if area_off > 0 else False  # 判断是否需要增加面积
        s = self.get_edge_parallel(limit, point, flag)  # 找到与指定向量夹角最小的边
        self.fix_change(*s)  # 补充边

    # 随机移动一个点
    def move_point(self):
        point = self.get_random_point()  # 随机选择一个点
        self.move_point_get(point)  # 移动该点

    # 修补面积
    def fix_change(self, p1, p2):
        """修补面积"""
        area_off = self.AREA - self.polygon.area  # 计算面积差
        if area_off > 0:  # 需要增加面积
            fix_line = LineString([(p1.x, p1.y), (p2.x, p2.y)])  # 计算边的直线方程
            point_choose = get_random_point_in_line(fix_line)  # 在边上随机取一点
            len_edge = fix_line.length
            edge_offset_distance = 2 * area_off / len_edge  # 计算边的偏移距离
            v_vertor = compute_vertical_vector((p1.x, p1.y), (p2.x, p2.y))
            point_choose = (
                point_choose[0] + v_vertor[0] * edge_offset_distance,
                point_choose[1] + v_vertor[1] * edge_offset_distance,
            )
            self.points.insert(
                self.points.index(p1) + 1, MyPoint(point_choose[0], point_choose[1], 4)
            )
        else:
            point_choose = p1 if random.random() > 0.5 else p2  # 选择减少面积的点
            p1, p2 = self.get_two_edges_of_point(point_choose)  # 获取该点所在的边
            angle = compute_angle(
                (p1.x - point_choose.x, p1.y - point_choose.y),
                (p2.x - point_choose.x, p2.y - point_choose.y),
            )
            equal_a = math.sqrt(2 * abs(area_off) / math.sin(angle))  # 计算边长
            l1, l2 = p1.distance(point_choose), p2.distance(point_choose)
            a1, a2 = float("inf"), float("inf")
            a1 = equal_a * random.uniform(0.9, 1)
            a2 = 2 * abs(area_off) / (a1 * math.sin(angle))
            a1, a2 = (
                (min(a1, a2), max(a1, a2)) if l1 < l2 else (max(a1, a2), min(a1, a2))
            )  # 保证截取的边长不超过原边长 # TODO
            # 截取的第一个点坐标为
            l1 = LineString([(p1.x, p1.y), (point_choose.x, point_choose.y)])
            l2 = LineString([(point_choose.x, point_choose.y), (p2.x, p2.y)])
            p1 = l1.interpolate((l1.length - a1) / l1.length, normalized=True)
            p2 = l2.interpolate(a2 / l2.length, normalized=True)
            plotting.plot_points([p1, p2])
            self.points.insert(
                self.points.index(point_choose) + 1, MyPoint(p2.x, p2.y, 4)
            )
            self.points.insert(
                self.points.index(point_choose) + 1, MyPoint(p1.x, p1.y, 4)
            )
            self.points.remove(point_choose)
        self.check_valid()
        self.get_limit()

    # 检查合法性
    def check_valid(self):
        if (
            # not is_convex_polygon(self.points) or
            not self.polygon.is_valid
            or not self.polygon.is_simple
            # or not self.polygon_is_in_area()
        ):
            my_print("invalid")
            self.reset()
            self.move_point()
        else:
            self.update()

    def polygon_is_in_area(self):
        """判断多边形是否在指定区域内"""
        for p in self.points:
            if p.x < 0 or p.x > 600 or p.y < 0 or p.y > 400:
                return False
        return True

    # 找到多边形中与指定向量夹角最小的边
    def get_edge_parallel(self, limit, point, flag):
        min_edge = None
        min_angle = float("inf")
        for i in range(len(self.points)):
            p1 = self.points[i]
            p2 = self.points[i + 1 if i < len(self.points) - 1 else 0]
            if p1 == point or p2 == point:
                continue
            vector2 = compute_unit_vector((p1.x - p2.x, p1.y - p2.y))
            angle = compute_angle(limit, vector2)
            angle = angle if angle < math.pi / 2 else math.pi - angle
            if angle < min_angle and (p1.type != 0 or p2.type != 0):
                if flag and (p1.type == 1 or p2.type == 1):
                    continue
                min_angle = angle
                min_edge = (p1, p2)
        if min_edge == None:
            for i in range(len(self.points)):
                p1 = self.points[i]
                p2 = self.points[i + 1 if i < len(self.points) - 1 else 0]
                if p1 == point or p2 == point:
                    if p1.type != 0 and p2.type != 0:
                        min_edge = (p1, p2)
        return min_edge

    # 计算两向量夹角
    def compute_angle(self, v1, v2):
        v1 = np.array(v1)
        v2 = np.array(v2)
        v1 = v1 / np.linalg.norm(v1)
        v2 = v2 / np.linalg.norm(v2)
        return np.arccos(np.dot(v1, v2))

    # 找到多边形中与指定点相邻的满足条件的一条边
    def get_suitable_edge_of_point(self, p):
        """返回多边形中与指定点相邻且满足指定条件的边"""
        p1, p2 = self.get_two_edges_of_point(p)
        if p.limit is not None:  # 如果该点有限制向量, 则只能沿着该向量移动
            return (
                (p, p2)
                if self.is_parallel(p.limit, (p2.x - p.x, p2.y - p.y))
                else (p1, p)
            )
        else:  # 改点无限制向量, 找到与该点相邻的边, 任选一边
            return (p, p2) if random.random() > 0.5 else (p1, p)

    # 找到多边形中与指定点相邻的两条边
    def get_two_edges_of_point(self, p):
        """返回多边形中与指定点相邻的两条边"""
        for i in range(len(self.points)):
            if self.points[i].pos == p.pos:
                p1 = self.points[i - 1 if i > 0 else len(self.points) - 1]
                p2 = self.points[i + 1 if i < len(self.points) - 1 else 0]
                return p1, p2

    def is_parallel(self, v1, v2):
        if 1.0 - abs(np.cos(compute_angle(v1, v2))) < 1e-6:
            return True
        return False

    def get_limit(self):
        # 并得到单位向量
        self.up_limit = self.get_up_limit()
        self.right_limit = self.get_right_limit()
        my_print(f"right limit: {self.right_limit}")

    # 得到多边形位置上处于最上面的边
    def get_up_limit(self):
        p = self.points[0]
        for i in range(len(self.points)):
            if self.points[i].y > p.y:
                p = self.points[i]
        p1, p2 = self.get_two_edges_of_point(p)
        if self.points.index(p1) == 0:
            return LineString([(p.x, p.y), (p2.x, p2.y)])
        # 判断与x轴夹角最小的边
        angle_1 = compute_angle((0, 1), (p1.x - p.x, p1.y - p.y))
        angle_2 = compute_angle((0, 1), (p2.x - p.x, p2.y - p.y))
        if angle_1 < angle_2:
            return LineString([(p1.x, p1.y), (p.x, p.y)])
        else:
            return LineString([(p.x, p.y), (p2.x, p2.y)])

    # 得到多边形位置上处于最右边的边
    def get_right_limit(self):
        p = self.points[0]
        for i in range(len(self.points)):
            if self.points[i].x > p.x:
                p = self.points[i]
        p1, p2 = self.get_two_edges_of_point(p)
        if self.points.index(p1) == 0:
            return LineString([(p.x, p.y), (p2.x, p2.y)])
        # 判断与y轴夹角最小的边
        angle_1 = compute_angle((1, 0), (p1.x - p.x, p1.y - p.y))
        angle_2 = compute_angle((1, 0), (p2.x - p.x, p2.y - p.y))
        if angle_1 < angle_2:
            return LineString([(p1.x, p1.y), (p.x, p.y)])
        else:
            return LineString([(p.x, p.y), (p2.x, p2.y)])

    def __str__(self) -> str:
        p_0 = []  # 不可动点
        p_1 = []  # 可切除点
        p_2_3 = []  # 沿指定向量可动点
        p_4 = []  # 完全可动点
        for p in self.points:
            if p.type == 0:
                p_0.append(p.pos)
            if p.type == 1:
                p_1.append(p.pos)
            if p.type == 2 or p.type == 3:
                p_2_3.append(p.pos)
            else:
                p_4.append(p.pos)
        return f"p_0: {p_0}\np_1: {p_1}\np_2_3: {p_2_3}\np_4: {p_4}"


class Group:
    def __init__(self, Areas=None, minS=30, Width=600, Height=400, ax=None):
        super().__init__()
        self.Areas = (
            [
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
            if Areas == None
            else Areas
        )
        self.minS = minS
        self.Width = Width
        self.Height = Height
        self.ax = ax
        self.P = []
        self.round = 0

    def change_areas(self):
        ...

    def init_polygon(
        self,
        point_origin=MyPoint(0, 0, 0),
        limit_vector=((1, 0), (0, 1)),
        area=15300,
        type=True,
    ):
        p = self.get_origin_polygon(point_origin, limit_vector, area, type)
        l = LinearRing([(p.x, p.y) for p in p])
        if not l.is_valid or not l.is_simple:
            my_print("invalid")
        return MyPolygon(p)

    def next(self):
        limit_x = (
            [(1, 0), (0, 0)]
            if (self.round // 4) == 0
            else self.P[self.round - 4].up_limit
        )
        limit_y = (
            [(0, 0), (0, 1)]
            if (self.round % 4) == 0
            else self.P[self.round - 1].right_limit
        )
        if self.round == len(self.Areas) - 1:
            # 最后一个参照物平移一位
            limit_x = self.P[self.round - 3].up_limit
            limit_y = self.P[self.round - 4].right_limit
        point_origin, limit_vector = compute_limit(
            limit_x,
            limit_y,
            self.minS,
        )
        my_print(f"point_origin: {point_origin} --- limie_vector: {limit_vector}")
        # 判断生成的点是否与其他图形重合
        if self.round // 4 > 0 and self.round % 4 != 0:
            p = Point(point_origin[0], point_origin[1])
            flag_step = 5
            while flag_step > 0:
                for i in range(len(self.P)):
                    polygon: Polygon = self.P[self.round - 5].polygon
                    if polygon.distance(p) <= 30:
                        my_print("重合")
                        p = Point(p.x + 5, p.y + 5)
                        flag_step -= 1
                        continue
                flag_step = 0
            point_origin = (p.x, p.y)

        if self.round // 4 != 2:  # 如果不是第三行
            p = self.init_polygon(
                MyPoint(point_origin[0], point_origin[1], 0),
                limit_vector,
                self.Areas[self.round],
                type=True if self.round == 0 else False,
            )
        else:
            p = self.init_3_row_polygon(
                point_orign=MyPoint(point_origin[0], point_origin[1], 0),
                limit_vector=limit_vector,
                area=self.Areas[self.round],
            )

        self.P.append(p)

        # 随机移动
        step = 1 if random.random() > 0.5 else 2
        for i in range(step):
            p.move_point()
        self.round += 1

    def init_3_row_polygon(
        self, point_orign, limit_vector=[[1, 0], [0, 1]], area=15300
    ):
        p1 = (point_orign.x, point_orign.y)
        p2 = lines_intersection(
            [(p1[0], p1[1]), (p1[0] + limit_vector[1][0], p1[1] + limit_vector[1][1])],
            [(0, self.Height), (self.Width, self.Height)],
        )
        p2 = MyPoint(p2[0], p2[1], 0)
        p3 = MyPoint(p2.x + 100, p2.y, 0)
        p4 = lines_intersection(
            [(p1[0], p1[1]), (p1[0] + limit_vector[0][0], p1[1] + limit_vector[0][1])],
            [(p3.x, 0), (p3.x, p3.y)],
        )
        p = [
            MyPoint(p1[0], p1[1], 0),
            MyPoint(p2.x, p2.y, 0),
            MyPoint(p3.x, p3.y, 3, limit_x=(1, 0)),
            MyPoint(p4[0], p4[1], 3, limit_x=compute_unit_vector(limit_vector[0])),
        ]
        my_print(f"p1: {p1} --- p2: {p2} --- p3: {p3} --- p4: {p4}")
        return MyPolygon(p)

    def get_origin_polygon(
        self,
        point_origin=MyPoint(0, 0, 0),
        limit_vector=[[1, 0], [0, 1]],
        area=15300,
        type=False,
    ):
        """计算原始多边形"""
        # type: 0: 完全不可动 1: 只可切除 2: y轴可动 3: x轴可动 4: 完全可动
        angle = compute_angle(limit_vector[0], limit_vector[1])  # 计算两向量夹角
        edge_equal_length = np.sqrt(area / np.sin(angle))  # 边长
        r = 0.1  # 随机系数
        e1 = random.uniform(1 - r, 1 + r) * edge_equal_length  # 随机边长1
        e2 = area / (e1 * np.sin(angle))  # 随机边长2
        e1 = e2 = edge_equal_length
        p1 = MyPoint(x=point_origin.x, y=point_origin.y, type=1 if not type else 0)
        if p1.y + e2 > self.Width:
            e1, e2 = e2, e1
        p2 = self.compute_point(
            point_origin.x,
            point_origin.y,
            2,
            e1,
            limit_vector[0],
            limit_vector[1],
        )
        p4 = self.compute_point(
            point_origin.x,
            point_origin.y,
            3,
            e2,
            limit_vector[0],
            limit_vector[1],
        )
        p3 = MyPoint(p4.x + p2.x - p1.x, p4.y + p2.y - p1.y, 4)
        return [p1, p2, p3, p4]

    def compute_point(
        self,
        x,
        y,
        type: int = 0,
        edge=100,
        limit_x: tuple = None,
        limit_y: tuple = None,
    ):
        """计算新的点"""
        limit = compute_unit_vector(limit_x if type == 3 else limit_y)
        x = x + limit[0] * edge
        y = y + limit[1] * edge
        return MyPoint(x, y, type=type, limit_x=limit_x, limit_y=limit_y)


if __name__ == "__main__":
    group = Group()

    for _ in range(len(group.Areas)):
        group.next()
        plt.waitforbuttonpress()
        plt.show()
    # 实际面积为包含所有多边形的最小矩形面积
    PolygonCollection = GeometryCollection([p.polygon for p in group.P])
    set_area_sum = oriented_envelope(PolygonCollection).area
    # 计算面积和
    get_area_sum = sum([p.area for p in group.P])
    my_print(f"set_area_sum: {set_area_sum} --- get_area_sum: {get_area_sum}")
    my_print(f"area ratio: {get_area_sum / set_area_sum * 100:.2f}%")

    plt.ioff()

    plt.show()

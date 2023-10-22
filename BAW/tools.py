import numpy as np
from shapely import (
    LineString,
)
import random
import math


class MY_FLAG:
    flag = False

    def __init__(self):
        super().__init__()


# 计算单位向量
def compute_unit_vector(vector):
    """计算 vector 单位向量"""
    vector_m = np.linalg.norm(vector)  # 计算向量 vector 的模
    return (vector[0] / vector_m, vector[1] / vector_m)


# 计算与 p1 -> p2 方向的垂直向量
def compute_vertical_vector(p1, p2):
    """计算与 p1 -> p2 方向的垂直向量"""
    v = (p1[0] - p2[0], p1[1] - p2[1])
    v_m = np.linalg.norm(v)  # 计算向量 v 的模
    if v_m == 0:
        v_m = 1e-10
    return (v[1] / v_m, -v[0] / v_m)


# 计算两个向量的夹角
def compute_angle(vector1: tuple = (0, 1), vector2: tuple = (1, 0)):
    """计算两个向量的夹角"""
    dot = vector1[0] * vector2[0] + vector1[1] * vector2[1]  # 计算点积
    mag_1 = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)  # 计算向量 vector1 的模
    mag_2 = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)  # 计算向量 vector2 的模
    try:
        if mag_1 == 0:
            # 取极小值
            mag_1 = 1e-10
        if mag_2 == 0:
            mag_2 = 1e-10
        cos = dot / (mag_1 * mag_2)  # 计算 cos 值
        if cos > 1:
            angle = 0
        elif cos < -1:
            angle = np.pi
        else:
            angle = math.acos(cos)  # 计算夹角
    except:
        print("dot: ", dot)
        print("mag_1: ", mag_1)
        print("mag_2: ", mag_2)
        print("cos: ", dot / (mag_1 * mag_2))
        print("vector1: ", vector1)
        print("vector2: ", vector2)
    angle = angle if angle <= np.pi else 2 * np.pi - angle
    return angle


def get_random_point_in_line(line: LineString):
    """在 line 上随机取一点"""
    p = line.interpolate(random.uniform(0.2, 0.8), normalized=True)
    p = line.interpolate(0.5, normalized=True)
    return (p.x, p.y)


# 平移线段
def line_vertical_translation(line, minS):
    v = compute_vertical_vector(line.coords[0], line.coords[1])  # 计算垂直向量
    # 计算平移后的线
    return [(l[0] + v[0] * minS, l[1] + v[1] * minS) for l in line.coords]


# 计算两条线的交点
def lines_intersection(l1: list[tuple], l2: list[tuple]) -> tuple:
    """计算两条线的交点"""
    x1, y1, x2, y2 = l1[0][0], l1[0][1], l1[1][0], l1[1][1]
    x3, y3, x4, y4 = l2[0][0], l2[0][1], l2[1][0], l2[1][1]

    # 计算斜率，确保不除以0
    if x2 - x1 == 0:
        slope1 = float("inf")
    else:
        slope1 = (y2 - y1) / (x2 - x1)

    if x4 - x3 == 0:
        slope2 = float("inf")
    else:
        slope2 = (y4 - y3) / (x4 - x3)

    # 计算交点
    if slope1 == float("inf"):
        x_intersection = x1
        y_intersection = slope2 * (x1 - x3) + y3
    elif slope2 == float("inf"):
        x_intersection = x3
        y_intersection = slope1 * (x3 - x1) + y1
    else:
        x_intersection = (y3 - y1 + slope1 * x1 - slope2 * x3) / (slope1 - slope2)
        y_intersection = slope1 * (x_intersection - x1) + y1
    p = (x_intersection, y_intersection)
    return p


# 分别平移两条线, 得到两条线的交点
def compute_limit(l1, l2, minS):
    # 判断是否需要平移
    if l1 == [(1, 0), (0, 0)]:
        l1 = [(0, 0), (1, 0)]
    else:
        l1 = line_vertical_translation(LineString(l1), minS)

    if l2 == [(0, 0), (0, 1)]:
        l2 = [(0, 0), (0, 1)]
    else:
        l2 = line_vertical_translation(LineString(l2), minS)

    point = lines_intersection(l1, l2)
    # 得到 l1, l2 所代表方向的单位向量
    v1 = compute_unit_vector((l1[1][0] - l1[0][0], l1[1][1] - l1[0][1]))
    v2 = compute_unit_vector((l2[1][0] - l2[0][0], l2[1][1] - l2[0][1]))
    v1_m = np.linalg.norm(v1)
    v2_m = np.linalg.norm(v2)
    v1 = (v1[0] / v1_m, v1[1] / v1_m)
    if v1[0] < 0:
        v1 = (-v1[0], -v1[1])
    v2 = (v2[0] / v2_m, v2[1] / v2_m)
    if v2[1] < 0:
        v2 = (-v2[0], -v2[1])
    return point, (v1, v2)


# 判断是否是凸多边形
def is_convex_polygon(points):
    # 检查多边形的边数，至少需要3个点
    points = [p.pos for p in points]
    if len(points) < 3:
        return False

    def cross_product(p1, p2, p3):
        # 计算叉积
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    def angle_between(p1, p2, p3):
        # 计算角度
        v1 = np.array(p1) - np.array(p2)
        v2 = np.array(p3) - np.array(p2)
        dot_product = np.dot(v1, v2)
        magnitudes = np.linalg.norm(v1) * np.linalg.norm(v2)
        return np.arccos(dot_product / magnitudes) * 180 / np.pi

    # 检查多边形的每个内角
    for i in range(len(points)):
        p1, p2, p3 = (
            points[i],
            points[(i + 1) % len(points)],
            points[(i + 2) % len(points)],
        )
        cross = cross_product(p1, p2, p3)
        angle = angle_between(p1, p2, p3)
        if cross < 0 or angle >= 180:
            return False

    return True


# 计算两点之间的斜率
def calculate_slope(point1, point2):
    if point2[0] - point1[0] == 0:
        return float("inf")
    return (point2[1] - point1[1]) / (point2[0] - point1[0])


def find_parallel_edges(polygon_points):
    points = [p.pos for p in polygon_points]
    parallel_edges = []

    n = len(points)
    for i in range(n):
        point1 = points[i]
        point2 = points[(i + 1) % n]

        for j in range(i + 2, i + n - 1):
            point3 = points[j % n]
            point4 = points[(j + 1) % n]

            slope1 = calculate_slope(point1, point2)
            slope2 = calculate_slope(point3, point4)

            if slope1 == slope2:
                parallel_edges.append([point1, point2, point3, point4])
                return parallel_edges

    return parallel_edges


def my_print(*args, **kwargs):
    if MY_FLAG.flag:
        print(*args, **kwargs)

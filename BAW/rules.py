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
)
import random
import math
from shapely.ops import nearest_points


# 生成指定面积的正多边形
def generate_regular_polygon(num_sides: int = 5, target_area: float = 1000) -> Polygon:
    """生成指定边数和面积的正多边形

    Args:
        num_sides (int): 指定边数
        target_area (float): 指定面积

    Returns:
        Polygon: 正多边形
    """
    edge_length = math.sqrt(
        (4 * target_area) / num_sides * math.tan(math.pi / num_sides)
    )  # 边长
    r = edge_length / (2 * math.sin(math.pi / num_sides))  # 外接圆半径

    vertices = []
    for i in range(num_sides):
        angle = 2 * math.pi / num_sides * i  # 角度
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        vertices.append((x, y))

    # 判断是否逆时针
    if LinearRing(vertices).is_ccw:
        vertices.reverse()
    polygon = Polygon(vertices)
    polygon = affinity.rotate(
        polygon, random.uniform(0, 360), use_radians=True
    )  # 旋转随机角度

    return polygon


# 判断多边形是否存在平行边
def edges_not_parallel(polygon: Polygon) -> float:
    """_summary_判断多边形是否存在平行边

    Args:
        polygon (Polygon): 输入多边形

    Returns:
        bool: 是否存在平行边
    """
    coords = list(polygon.exterior.coords)
    num_edges = len(coords) - 1
    num_parallel_edges = 0

    points = MultiPoint()

    for i in range(num_edges):
        x1, y1 = coords[i]
        x2, y2 = coords[i + 1]

        slope = (y2 - y1) / (x2 - x1) if x2 != x1 else float("inf")
        temp = Point(slope, 0).buffer(0.0001)
        if points.intersects(temp):
            num_parallel_edges += 1
        else:
            points = points.union(temp)

    return num_parallel_edges


# 判断是否与相邻的多边形临边平行
def nearest_edges_parallel(polygon1, polygon2):
    nearest_points_poly1, nearest_points_poly2 = nearest_points(polygon1, polygon2)

    nearest_line = LineString([nearest_points_poly1, nearest_points_poly2])

    x1, y1 = nearest_points_poly1.x, nearest_points_poly1.y
    x2, y2 = nearest_points_poly2.x, nearest_points_poly2.y

    if x2 != x1:
        slope = (y2 - y1) / (x2 - x1)
    else:
        slope = float("inf")

    nearest_edge_poly1 = nearest_line.distance(polygon1.exterior)
    nearest_edge_poly2 = nearest_line.distance(polygon2.exterior)

    if nearest_edge_poly1 == nearest_edge_poly2 and slope != float("inf"):
        return True

    return False


# 判断两多边形距离是否小于阈值
def distance_large_than_threshold(
    polygon1: Polygon, polygon2: Polygon, threshold: float
) -> bool:
    """判断两多边形距离是否小于阈值

    Args:
        polygon1 (Polygon): 多边形1
        polygon2 (Polygon): 多边形2
        threshold (float): 距离阈值

    Returns:
        bool: 是否满足阈值要求
    """
    nearest_points_poly1, nearest_points_poly2 = nearest_points(polygon1, polygon2)

    distance = nearest_points_poly1.distance(nearest_points_poly2)

    if distance >= threshold:
        return True

    return False


# 计算所有多边形的最小旋转矩形
def get_min_bounding_rectangles(polygons: GeometryCollection) -> Polygon:
    """计算所有多边形的最小旋转矩形

    Args:
        polygons ([Polygon]): 多边形列表

    Returns:
        Polygon: 最小旋转矩形
    """
    return oriented_envelope(polygons)


def level_down(level, off=0):
    match level:
        case 0 | 1:
            return 0
        case 2 | 3:
            return 1
        case 4:
            return level - off - 1


def get_type_list(x, y, maxX, maxY):
    level = [1, 2, 4, 3]
    if x == maxX:
        level[2] = level_down(level[2], 1)
        level[3] = level_down(level[3], 1)
    if y == maxY:
        level[2] = level_down(level[1], 0)
        level[3] = level_down(level[2], 0)
    # if x == 0 and y == 0:
    #     level[0] = 0
    # if x == 0 and y == maxY:
    #     level[1] = 0
    # if y==maxY and x==maxX:
    #     level[2] = 0
    # if y==0 and x== maxX:
    #     level[3] = 0
    return np.array(level)


class MyPoint:
    def __init__(self, x, y, type: int = 0, limit_x=None, limit_y=None):
        super().__init__()
        self.x = x
        self.y = y
        self.type = type  # 0: 完全不可动 1: 只可切除 2: y轴可动 3: x轴可动 4: 完全可动
        self.limit_x = limit_x
        self.limit_y = limit_y

    def distance(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

    def slope(self, p):
        if self.x == p.x:
            return float("inf")
        return (self.y - p.y) / (self.x - p.x)

    def __str__(self):
        return f"({self.x}, {self.y})"


def get_point(
    x, y, type: int = 0, limit_x: tuple = None, limit_y: tuple = None, area=0
):
    if type == 2 or type == 3:
        angle = np.arccos(
            np.dot(limit_x, limit_y)
            / (np.linalg.norm(limit_x) * np.linalg.norm(limit_y))
        )  # 两向量夹角
        edge_length = np.sqrt(area / np.sin(angle))  # 边长
        if type == 2:  # 限制y轴
            v_m = np.linalg.norm(limit_y)  # 计算向量 limit_y 的模
            scaled_vector = (
                limit_y[0] * edge_length / v_m,
                limit_y[1] * edge_length / v_m,
            )
            offset = (x + scaled_vector[0], y + scaled_vector[1])
            return MyPoint(
                x=offset[0], y=offset[1], type=type, limit_x=limit_x, limit_y=limit_y
            )
        if type == 3:  # 限制x轴
            v_m = np.linalg.norm(limit_x)
            scaled_vector = (
                limit_x[0] * edge_length / v_m,
                limit_x[1] * edge_length / v_m,
            )
            offset = (x + scaled_vector[0], y + scaled_vector[1])
            return MyPoint(
                x=offset[0], y=offset[1], type=type, limit_x=limit_x, limit_y=limit_y
            )
    return MyPoint(x, y, type=type, limit_x=limit_x, limit_y=limit_y)


def get_origin_polygon(
    type_list=[1, 2, 4, 3],
    points_origin=MyPoint(0, 0, 0),
    limit_vector=[[1, 0], [0, 1]],
    area=15300,
):
    p1 = MyPoint(0, 0, type_list[0])
    p2 = get_point(
        points_origin.x,
        points_origin.y,
        type_list[1],
        limit_vector[0],
        limit_vector[1],
        area,
    )
    p4 = get_point(
        points_origin.x,
        points_origin.y,
        type_list[3],
        limit_vector[0],
        limit_vector[1],
        area,
    )
    p3 = MyPoint(p4.x + p2.x - p1.x, p4.y + p2.y - p1.y, type_list[2])
    return [p1, p2, p3, p4]


if __name__ == "__main__":
    print("hello")
    l = get_origin_polygon()
    for i in l:
        print(i)

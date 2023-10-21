# Created by Hao JIN on Sept. 30, 2023

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import seaborn as sns; sns.set()  // seaborn 库用来美化图表; sns.set() 用来设置图表样式
plt.ion()
import matplotlib.patches as patches
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from shapely.geometry import Polygon, LineString, MultiLineString, Point
from shapely.affinity import translate, scale  # translate 库用来平移多边形; scale 库用来缩放多边形
from shapely.ops import orient  # orient 库用来判断多边形的方向
import math
import random

from gui.main import Ui_MainWindow


# Constant
TEST_BENCH = "testbench.csv"
MIN_DISTANCE = 30


###############################################################################
# Main Window
###############################################################################
class MainWindow(QMainWindow, Ui_MainWindow):
    ###########################################################################
    # Initialization
    ###########################################################################
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # load the testbench parameters
        self.load_testbench()
        self.on_comboBox_select(0)

        # matplotlib
        self.fig, self.ax = plt.subplots()

        # init the layout
        self.init_raster()
        self.init_layout()

        self.comboBox.currentIndexChanged.connect(
            self.on_comboBox_select
        )  # Connect a function to the combo box selection change
        self.pushButton_init_layout.clicked.connect(self.init_layout)
        self.pushButton_manual_optimize.clicked.connect(self.manual_optimize)

    ###########################################################################
    # Methods
    ###########################################################################
    def perturb_point(self, point):
        return (point[0] + random.uniform(-5, 5), point[1] + random.uniform(-5, 5))

    def get_coords_from_bottom_left(self, pentagon):
        coords = list(pentagon.exterior.coords)[
            :-1
        ]  # Exclude the last coordinate since it's the same as the first

        # Identify the bottom-left vertex (smallest y-value and then smallest x-value)
        bottom_left = min(coords, key=lambda v: (v[1], v[0]))
        index_bottom_left = coords.index(bottom_left)

        # Rearrange the vertices to start from the bottom-left vertex and go in counterclockwise order
        reordered_coords = coords[index_bottom_left:] + coords[:index_bottom_left]

        return reordered_coords

    def scale_pentagon_to_area(self, pentagon, desired_area):
        # Calculate the current area
        original_area = pentagon.area

        # Calculate the scale factor
        scale_factor = math.sqrt(desired_area / original_area)

        # Calculate the centroid of the pentagon
        centroid = pentagon.centroid

        # Create a new pentagon by scaling each vertex relative to the centroid
        scaled_coords = [
            (
                centroid.x + scale_factor * (x - centroid.x),
                centroid.y + scale_factor * (y - centroid.y),
            )
            for x, y in pentagon.exterior.coords[:-1]
        ]

        return Polygon(scaled_coords)

    def is_ccw(self, polygon):
        coords = list(
            polygon.exterior.coords[:-1]
        )  # Exclude the repeated last coordinate
        n = len(coords)
        area = 0.5 * sum(
            (
                coords[i][0] * coords[(i + 1) % n][1]
                - coords[(i + 1) % n][0] * coords[i][1]
            )
            for i in range(n)
        )
        return area > 0

    def mirror_across_centroid(self, pentagon):
        centroid_x = pentagon.centroid.x
        mirrored_coords = [
            (2 * centroid_x - x, y) for x, y in pentagon.exterior.coords[:-1]
        ]

        # Ensure counterclockwise order
        mirrored_polygon = Polygon(mirrored_coords)
        if not self.is_ccw(mirrored_polygon):
            mirrored_coords = mirrored_coords[::-1]

        # Find the index of the bottom-leftmost vertex
        bl_index = min(enumerate(mirrored_coords), key=lambda v: (v[1][0], v[1][1]))[0]

        # Reorder the coordinates starting from the bottom-leftmost vertex
        reordered_coords = mirrored_coords[bl_index:] + mirrored_coords[:bl_index]

        return Polygon(reordered_coords)

    def compute_angle(self, A, B, C):
        # Vectors
        AB = [B[0] - A[0], B[1] - A[1]]
        BC = [C[0] - B[0], C[1] - B[1]]

        # Dot product
        dot_product = AB[0] * BC[0] + AB[1] * BC[1]

        # Magnitudes
        mag_AB = math.sqrt(AB[0] ** 2 + AB[1] ** 2)
        mag_BC = math.sqrt(BC[0] ** 2 + BC[1] ** 2)

        # Angle in radians
        angle = math.acos(dot_product / (mag_AB * mag_BC))

        # Convert to degrees
        angle_deg = math.degrees(angle)
        return angle_deg

    def get_angles(self, pentagon):
        coords = list(
            pentagon.exterior.coords[:-1]
        )  # Exclude the repeated last coordinate
        angles = []

        for i in range(5):
            A = coords[i - 1]
            B = coords[i]
            C = coords[(i + 1) % 5]
            angles.append(self.compute_angle(A, B, C))

        return angles

    def adjust_for_parallelism_and_distance(
        self, p1, p2, side_index_p1, side_index_p2, min_distance
    ):
        coords_p1 = list(p1.exterior.coords[:-1])
        coords_p2 = list(p2.exterior.coords[:-1])

        # Get the sides
        side1 = [coords_p1[side_index_p1], coords_p1[(side_index_p1 + 1) % 5]]
        side2 = [coords_p2[side_index_p2], coords_p2[(side_index_p2 - 1) % 5]]

        # Determine direction of side1
        dx1, dy1 = side1[1][0] - side1[0][0], side1[1][1] - side1[0][1]

        # Adjust side2 to be parallel to side1
        coords_p2[(side_index_p2 - 1) % 5] = (
            coords_p2[side_index_p2][0] + dx1,
            coords_p2[side_index_p2][1] + dy1,
        )
        adjusted_side2 = LineString(
            [coords_p2[side_index_p2], coords_p2[(side_index_p2 - 1) % 5]]
        )

        # Calculate the distance between the sides
        distance = LineString(side1).distance(adjusted_side2)

        # Adjust the coordinates of side2's vertices outward if the distance is less than the minimum
        if distance < min_distance:
            print("adjust")  #
            # Calculate how much to adjust
            adjust_amount = min_distance - distance
            adjust_factor = adjust_amount / ((dx1**2 + dy1**2) ** 0.5)

            # Adjust side2's coordinates
            coords_p2[side_index_p2] = (
                coords_p2[side_index_p2][0] + adjust_factor * dx1,
                coords_p2[side_index_p2][1] + adjust_factor * dy1,
            )
            coords_p2[(side_index_p2 - 1) % 5] = (
                coords_p2[(side_index_p2 - 1) % 5][0] + adjust_factor * dx1,
                coords_p2[(side_index_p2 - 1) % 5][1] + adjust_factor * dy1,
            )

            adjusted_p2 = Polygon(coords_p2)
            return adjusted_p2
        else:
            return Polygon(coords_p2)

    def manual_optimize(self):
        self.ax.clear()
        self.init_raster()

        # S1
        # Start with the first vertex as the most bottom-left
        coords = self.get_coords_from_bottom_left(self.S1_pentagon)
        # make the top parallel to x
        coords[2] = (coords[2][0], coords[3][1])
        # perturb vertex
        coords[0] = self.perturb_point(coords[0])
        coords[1] = self.perturb_point(coords[1])
        self.S1_pentagon = Polygon(coords)
        # rescale to keep the area
        self.S1_pentagon = self.scale_pentagon_to_area(self.S1_pentagon, self.S1)
        # move the top left to top left corner
        self.S1_pentagon = self.move_pentagon_to_location(
            self.S1_pentagon, 3, (0, self.H)
        )
        # Plotting
        self.plot_pentagon(self.S1_pentagon, f"S1={self.S1_pentagon.area:.0f}")
        self.ax.plot(
            *self.S1_pentagon.buffer(30).exterior.xy, color="blue", linestyle="--"
        )
        self.label_S1.setText(
            ", ".join(
                map(self.str_format, self.get_coords_from_bottom_left(self.S1_pentagon))
            )
        )
        angles = self.get_angles(self.S1_pentagon)
        print(f"angles of S1: {angles}, {np.sum(angles)}")

        # T2
        # Start with the first vertex as the most bottom-left
        coords = self.get_coords_from_bottom_left(self.T2_pentagon)
        # make the bottom parallel to x
        coords[0] = (coords[0][0], coords[4][1])
        # perturb vertex
        coords[1] = self.perturb_point(coords[1])
        coords[2] = self.perturb_point(coords[2])
        self.T2_pentagon = Polygon(coords)
        # rescale to keep the area
        self.T2_pentagon = self.scale_pentagon_to_area(self.T2_pentagon, self.T2)
        # move the bottom left to bottom left corner
        self.T2_pentagon = self.move_pentagon_to_location(self.T2_pentagon, 4, (0, 0))
        # Plotting
        self.plot_pentagon(self.T2_pentagon, f"T2={self.T2_pentagon.area:.0f}")
        self.ax.plot(
            *self.T2_pentagon.buffer(30).exterior.xy, color="blue", linestyle="--"
        )
        self.label_T2.setText(
            ", ".join(
                map(self.str_format, self.get_coords_from_bottom_left(self.T2_pentagon))
            )
        )
        angles = self.get_angles(self.T2_pentagon)
        print(f"angles of T2: {angles}, {np.sum(angles)}")

        # T5
        # mirror
        self.T5_pentagon = self.mirror_across_centroid(self.T5_pentagon)
        # Start with the first vertex as the most bottom-left
        coords = self.get_coords_from_bottom_left(self.T5_pentagon)
        # make the top parallel to x
        coords[3] = (coords[3][0], coords[2][1])
        # perturb vertex
        coords[0] = self.perturb_point(coords[0])
        coords[4] = self.perturb_point(coords[4])
        self.T5_pentagon = Polygon(coords)
        # rescale to keep the area
        self.T5_pentagon = self.scale_pentagon_to_area(self.T5_pentagon, self.T5)
        # move the top right to top right corner
        self.T5_pentagon = self.move_pentagon_to_location(
            self.T5_pentagon, 2, (self.W, self.H)
        )
        # Plotting
        self.plot_pentagon(self.T5_pentagon, f"T5={self.T5_pentagon.area:.0f}")
        self.ax.plot(
            *self.T5_pentagon.buffer(30).exterior.xy, color="blue", linestyle="--"
        )
        self.label_T5.setText(
            ", ".join(
                map(self.str_format, self.get_coords_from_bottom_left(self.T5_pentagon))
            )
        )
        angles = self.get_angles(self.T5_pentagon)
        print(f"angles of T5: {angles}, {np.sum(angles)}")

        # S6
        # mirror
        self.S6_pentagon = self.mirror_across_centroid(self.S6_pentagon)
        # Start with the first vertex as the most bottom-left
        coords = self.get_coords_from_bottom_left(self.S6_pentagon)
        # make the top parallel to x
        coords[0] = (coords[0][0], coords[1][1])
        # perturb vertex
        coords[3] = self.perturb_point(coords[3])
        coords[4] = self.perturb_point(coords[4])
        self.S6_pentagon = Polygon(coords)
        # rescale to keep the area
        self.S6_pentagon = self.scale_pentagon_to_area(self.S6_pentagon, self.S6)
        # move the top right to top right corner
        self.S6_pentagon = self.move_pentagon_to_location(
            self.S6_pentagon, 1, (self.W, 0)
        )
        # Plotting
        self.plot_pentagon(self.S6_pentagon, f"S6={self.S6_pentagon.area:.0f}")
        self.ax.plot(
            *self.S6_pentagon.buffer(30).exterior.xy, color="blue", linestyle="--"
        )
        self.label_S6.setText(
            ", ".join(
                map(self.str_format, self.get_coords_from_bottom_left(self.S6_pentagon))
            )
        )
        angles = self.get_angles(self.S6_pentagon)
        print(f"angles of S6: {angles}, {np.sum(angles)}")

        # S2
        # mirror
        self.S2_pentagon = self.mirror_across_centroid(self.S2_pentagon)
        # Start with the first vertex as the most bottom-left
        coords = self.get_coords_from_bottom_left(self.S2_pentagon)
        # perturb vertex
        coords[0] = self.perturb_point(coords[0])
        coords[3] = self.perturb_point(coords[3])
        coords[4] = self.perturb_point(coords[4])
        self.S2_pentagon = Polygon(coords)
        # adjust to parallel
        self.S2_pentagon = self.adjust_for_parallelism_and_distance(
            self.S1_pentagon, self.S2_pentagon, 4, 3, MIN_DISTANCE
        )
        self.S2_pentagon = self.adjust_for_parallelism_and_distance(
            self.S3_pentagon, self.S2_pentagon, 2, 2, MIN_DISTANCE
        )
        # self.S2_pentagon = self.adjust_to_parallel(self.T2_pentagon, self.S2_pentagon,2, 0)
        # adjust the distance
        # self.S2_pentagon = self.adjust_distance(self.S1_pentagon, self.S2_pentagon, 4, 3, MIN_DISTANCE)
        # self.S2_pentagon = self.adjust_distance(self.T2_pentagon, self.S2_pentagon, 2, 4, MIN_DISTANCE)

        # rescale to keep the area
        self.S2_pentagon = self.scale_pentagon_to_area(self.S2_pentagon, self.S2)

        # Plotting
        self.plot_pentagon(self.S2_pentagon, f"S2={self.S2_pentagon.area:.0f}")
        self.label_S2.setText(
            ", ".join(
                map(self.str_format, self.get_coords_from_bottom_left(self.S2_pentagon))
            )
        )

        # pentagon = self.generate_pentagon(self.S2)
        # specified_center_coords = (self.W/8, 3*self.H/6)
        # self.S2_pentagon = self.plot_pentagon_with_center(pentagon, specified_center_coords, f"S2={self.S2}")
        # self.label_S2.setText(', '.join(map(self.str_format, self.get_vertexes(self.S2_pentagon))))

        # S3
        pentagon = self.generate_pentagon(self.S3)
        specified_center_coords = (3 * self.W / 8, 3 * self.H / 6)
        self.S3_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"S3={self.S3}"
        )
        self.label_S3.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.S3_pentagon)))
        )

        # S4
        pentagon = self.generate_pentagon(self.S4)
        specified_center_coords = (5 * self.W / 8, 3 * self.H / 6)
        self.S4_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"S4={self.S4}"
        )
        self.label_S4.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.S4_pentagon)))
        )

        # S5
        pentagon = self.generate_pentagon(self.S5)
        specified_center_coords = (7 * self.W / 8, 3 * self.H / 6)
        self.S5_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"S5={self.S5}"
        )
        self.label_S5.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.S5_pentagon)))
        )

        # T1
        pentagon = self.generate_pentagon(self.T1)
        specified_center_coords = (3 * self.W / 8, 5 * self.H / 6)
        self.T1_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"T1={self.T1}"
        )
        self.label_T1.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.T1_pentagon)))
        )

        # T3
        pentagon = self.generate_pentagon(self.T3)
        specified_center_coords = (3 * self.W / 8, self.H / 6)
        self.T3_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"T3={self.T3}"
        )
        self.label_T3.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.T3_pentagon)))
        )

        # T4
        pentagon = self.generate_pentagon(self.T4)

        if self.T3 + self.S6 < self.T1 + self.T5:
            specified_center_coords = (5 * self.W / 8, self.H / 6)
        else:
            specified_center_coords = (5 * self.W / 8, 5 * self.H / 6)

        self.T4_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"T4={self.T4}"
        )
        self.label_T4.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.T4_pentagon)))
        )

        self.cal_area_ratio()
        plt.show()

    def cal_area_ratio(self):
        area_ratio = (
            self.S1_pentagon.area
            + self.S2_pentagon.area
            + self.S3_pentagon.area
            + self.S4_pentagon.area
            + self.S5_pentagon.area
            + self.S6_pentagon.area
            + self.T1_pentagon.area
            + self.T2_pentagon.area
            + self.T3_pentagon.area
            + self.T4_pentagon.area
            + self.T5_pentagon.area
        ) / (self.W * self.H)

        self.lineEdit_ratio_real.setText(f"{100*area_ratio:.2f}")

    def move_pentagon_to_location(self, pentagon, vertex_index, new_location):
        # Get the current coordinates of the specified vertex
        current_location = list(pentagon.exterior.coords)[vertex_index]

        # Calculate the translation required
        dx = new_location[0] - current_location[0]
        dy = new_location[1] - current_location[1]

        # Translate the pentagon
        translated_pentagon = translate(pentagon, xoff=dx, yoff=dy)

        return translated_pentagon

    def get_vertexes(self, pentagon):
        return list(pentagon.exterior.coords)[:-1]

    # def rescale_pentagon(self, pentagon, target_area, vertex):
    #     # Adjust size to match the target area
    #     factor = math.sqrt(target_area / pentagon.area)
    #     pentagon = scale(pentagon, xfact=factor, yfact=factor, origin=vertex)

    #     return pentagon

    def angle_between_lines(self, line1, line2):
        p1, p2 = line1.coords
        p3, p4 = line2.coords
        v1 = (p2[0] - p1[0], p2[1] - p1[1])
        v2 = (p4[0] - p3[0], p4[1] - p3[1])
        dot = v1[0] * v2[0] + v1[1] * v2[1]
        mag1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
        mag2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
        angle = math.acos(dot / (mag1 * mag2))
        return math.degrees(angle)

    def plot_pentagon_with_offset(self, vertices, offset):
        # Create the pentagon from vertices
        pentagon = Polygon(vertices)

        # Create the offset shape
        offset_shape = pentagon.buffer(offset)

        # Plotting
        self.ax.plot(*pentagon.exterior.xy, color="red")
        self.ax.plot(*offset_shape.exterior.xy, color="blue", linestyle="--")
        plt.show()

    def generate_pentagon(self, area):
        # Calculate side length from area
        s = math.sqrt(4 * area * math.tan(math.pi / 5) / 5)

        # Calculate the radius of the circumscribed circle
        r = s / (2 * math.sin(math.pi / 5))

        # Generate the regular pentagon coordinates
        coords = []
        for i in range(5):
            angle = 2 * math.pi * i / 5
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            coords.append((x, y))
        p = Polygon(coords)
        print(p.area)
        return Polygon(coords)

    def plot_pentagon(self, pentagon, string):
        # Get the current centroid of the pentagon
        current_centroid_coords = pentagon.centroid.coords[0]

        # # Calculate the translation required
        # dx = specified_center_coords[0] - current_centroid_coords[0]
        # dy = specified_center_coords[1] - current_centroid_coords[1]

        # # Translate the pentagon
        # translated_pentagon = translate(pentagon, xoff=dx, yoff=dy)

        # Extract x and y coordinates for plotting
        x, y = pentagon.exterior.xy

        # Plotting
        # fig, ax = plt.subplots()
        if string[0] == "S":
            self.ax.fill(
                x, y, alpha=0.5, fc="blue", ec="black"
            )  # fc and ec are facecolor and edgecolor respectively
            self.ax.plot(*current_centroid_coords, "ro")  # red dot for specified center
        elif string[0] == "T":
            self.ax.fill(
                x, y, alpha=0.5, fc="red", ec="black"
            )  # fc and ec are facecolor and edgecolor respectively
            self.ax.plot(
                *current_centroid_coords, "bo"
            )  # blue dot for specified center
        else:
            print("string should begin with S or T")

        # self.ax.set_aspect('equal')
        # ax.grid(True, which='both')

        self.ax.annotate(
            string,
            (current_centroid_coords[0], current_centroid_coords[1]),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

        plt.show()

    def plot_pentagon_with_center(self, pentagon, specified_center_coords, string):
        # Get the current centroid of the pentagon
        current_centroid_coords = pentagon.centroid.coords[0]

        # Calculate the translation required
        dx = specified_center_coords[0] - current_centroid_coords[0]
        dy = specified_center_coords[1] - current_centroid_coords[1]

        # Translate the pentagon
        translated_pentagon = translate(pentagon, xoff=dx, yoff=dy)

        # Extract x and y coordinates for plotting
        x, y = translated_pentagon.exterior.xy

        # Plotting
        # fig, ax = plt.subplots()
        if string[0] == "S":
            self.ax.fill(
                x, y, alpha=0.5, fc="blue", ec="black"
            )  # fc and ec are facecolor and edgecolor respectively
            self.ax.plot(*specified_center_coords, "ro")  # red dot for specified center
        elif string[0] == "T":
            self.ax.fill(
                x, y, alpha=0.5, fc="red", ec="black"
            )  # fc and ec are facecolor and edgecolor respectively
            self.ax.plot(
                *specified_center_coords, "bo"
            )  # blue dot for specified center
        else:
            print("string should begin with S or T")

        # self.ax.set_aspect('equal')
        # ax.grid(True, which='both')

        self.ax.annotate(
            string,
            specified_center_coords,
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

        plt.show()

        return translated_pentagon

    def str_format(self, number):
        return f"({number[0]:.0f}, {number[1]:.0f})"

    def init_layout(self):
        self.ax.clear()
        self.init_raster()

        # S1
        pentagon = self.generate_pentagon(self.S1)  # 产生一个面积为S1的五边形
        specified_center_coords = (self.W / 8, 5 * self.H / 6)
        self.S1_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"S1={self.S1}"
        )
        self.label_S1.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.S1_pentagon)))
        )

        # S2
        pentagon = self.generate_pentagon(self.S2)
        specified_center_coords = (self.W / 8, 3 * self.H / 6)
        self.S2_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"S2={self.S2}"
        )
        self.label_S2.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.S2_pentagon)))
        )

        # S3
        pentagon = self.generate_pentagon(self.S3)
        specified_center_coords = (3 * self.W / 8, 3 * self.H / 6)
        self.S3_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"S3={self.S3}"
        )
        self.label_S3.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.S3_pentagon)))
        )

        # S4
        pentagon = self.generate_pentagon(self.S4)
        specified_center_coords = (5 * self.W / 8, 3 * self.H / 6)
        self.S4_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"S4={self.S4}"
        )
        self.label_S4.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.S4_pentagon)))
        )

        # S5
        pentagon = self.generate_pentagon(self.S5)
        specified_center_coords = (7 * self.W / 8, 3 * self.H / 6)
        self.S5_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"S5={self.S5}"
        )
        self.label_S5.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.S5_pentagon)))
        )

        # S6
        pentagon = self.generate_pentagon(self.S6)
        specified_center_coords = (7 * self.W / 8, self.H / 6)
        self.S6_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"S6={self.S6}"
        )
        self.label_S6.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.S6_pentagon)))
        )

        # T1
        pentagon = self.generate_pentagon(self.T1)
        specified_center_coords = (3 * self.W / 8, 5 * self.H / 6)
        self.T1_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"T1={self.T1}"
        )
        self.label_T1.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.T1_pentagon)))
        )

        # T2
        pentagon = self.generate_pentagon(self.T2)
        specified_center_coords = (self.W / 8, self.H / 6)
        self.T2_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"T2={self.T2}"
        )
        self.label_T2.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.T2_pentagon)))
        )

        # T3
        pentagon = self.generate_pentagon(self.T3)
        specified_center_coords = (3 * self.W / 8, self.H / 6)
        self.T3_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"T3={self.T3}"
        )
        self.label_T3.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.T3_pentagon)))
        )

        # T4
        pentagon = self.generate_pentagon(self.T4)

        if self.T3 + self.S6 < self.T1 + self.T5:
            specified_center_coords = (5 * self.W / 8, self.H / 6)
        else:
            specified_center_coords = (5 * self.W / 8, 5 * self.H / 6)

        self.T4_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"T4={self.T4}"
        )
        self.label_T4.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.T4_pentagon)))
        )

        # T5
        pentagon = self.generate_pentagon(self.T5)
        specified_center_coords = (7 * self.W / 8, 5 * self.H / 6)
        self.T5_pentagon = self.plot_pentagon_with_center(
            pentagon, specified_center_coords, f"T5={self.T5}"
        )
        self.label_T5.setText(
            ", ".join(map(self.str_format, self.get_vertexes(self.T5_pentagon)))
        )

        # print("\n===")
        # print(self.S1_pentagon.area)
        # print(self.S2_pentagon.area)
        # print(self.S3_pentagon.area)
        # print(self.S4_pentagon.area)
        # print(self.S5_pentagon.area)
        # print(self.S6_pentagon.area)
        # print(self.T1_pentagon.area)
        # print(self.T2_pentagon.area)
        # print(self.T3_pentagon.area)
        # print(self.T4_pentagon.area)
        # print(self.T5_pentagon.area)

        self.cal_area_ratio()

    def init_raster(self):
        self.ax.set_aspect("equal")
        self.ax.set_xlim(0, self.W)
        self.ax.set_ylim(0, self.H)

        for i in range(2):
            exec(
                f"hline_{i} = LineString([(0, {i+1}*self.H/3), (self.W, {i+1}*self.H/3)])"
            )
            exec(f"self.ax.plot(*hline_{i}.xy, color='gray', linestyle='--')")

        for i in range(3):
            exec(
                f"vline_{i} = LineString([({i+1}*self.W/4, 0), ({i+1}*self.W/4, self.H)])"
            )
            exec(f"self.ax.plot(*vline_{i}.xy, color='gray', linestyle='--')")

        plt.show()

    def on_comboBox_select(self, index):
        # Set the text of the line edit to the corresponding 'case' based on the selected 'case'
        self.S1 = self.df.loc[index, "S1"]
        self.lineEdit_S1.setText(str(self.S1))

        self.S2 = self.df.loc[index, "S2"]
        self.lineEdit_S2.setText(str(self.S2))

        self.S3 = self.df.loc[index, "S3"]
        self.lineEdit_S3.setText(str(self.S3))

        self.S4 = self.df.loc[index, "S4"]
        self.lineEdit_S4.setText(str(self.S4))

        self.S5 = self.df.loc[index, "S5"]
        self.lineEdit_S5.setText(str(self.S5))

        self.S6 = self.df.loc[index, "S6"]
        self.lineEdit_S6.setText(str(self.S6))

        self.T1 = self.df.loc[index, "T1"]
        self.lineEdit_T1.setText(str(self.T1))

        self.T2 = self.df.loc[index, "T2"]
        self.lineEdit_T2.setText(str(self.T2))

        self.T3 = self.df.loc[index, "T3"]
        self.lineEdit_T3.setText(str(self.T3))

        self.T4 = self.df.loc[index, "T4"]
        self.lineEdit_T4.setText(str(self.T4))

        self.T5 = self.df.loc[index, "T5"]
        self.lineEdit_T5.setText(str(self.T5))

        self.gap = self.df.loc[index, "gap"]
        self.lineEdit_gap.setText(str(self.gap))

        self.W = self.df.loc[index, "W"]
        self.lineEdit_W.setText(str(self.W))

        self.H = self.df.loc[index, "H"]
        self.lineEdit_H.setText(str(self.H))

        self.ratio_spec = self.df.loc[index, "ratio_spec_(%)"]
        self.pushButton_init_layout.clicked.connect(self.init_reset)

    def load_testbench(self):
        self.df = pd.read_csv(TEST_BENCH)
        # self.df["init_ratio"] = self.df.loc[:, 'S1':'T5'].sum(axis=1)/(self.df['W']*self.df['H'])
        print(self.df.head(20))

        self.comboBox.clear()
        self.comboBox.addItems(
            self.df["case"].tolist()
        )  # Populate combo box with 'case' column
        # print(self.df.head(10))


###############################################################################
# Class Resonator
###############################################################################
class Resonator:
    """a BAW resonator with basic shape of"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

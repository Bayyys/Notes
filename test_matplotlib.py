import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3D
from scipy.spatial.transform import Rotation


def plot_skeleton(lengths, angles):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(len(lengths)):
        # 绘制骨骼的起点坐标
        if i == 0:
            start_point = np.array([0, 0, 0])
        else:
            start_point = end_point

        # 计算骨骼的终点坐标
        end_point = calculate_end_point(start_point, lengths[i], angles[i])

        # 绘制骨骼
        ax.add_line(Line3D((start_point[0], end_point[0]),
                            (start_point[1], end_point[1]),
                            (start_point[2], end_point[2])))

        # 绘制骨骼的终点坐标
        ax.scatter(end_point[0], end_point[1], end_point[2], c='r')

    # 设置坐标轴范围
    ax.set_xlim([-sum(lengths), sum(lengths)])
    ax.set_ylim([-sum(lengths), sum(lengths)])
    ax.set_zlim([-sum(lengths), sum(lengths)])

    # 设置坐标轴标签
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # 显示图形
    plt.show()


# 给定一个点的坐标, 例如：(2, 2, 2), 线段的长度, 例如：10, 旋转角度, 例如：[0, 45, 0], 求终点坐标
def calculate_end_point(start_point, length, angles):
    # 根据 roll、pitch 和 yaw 计算旋转矩阵
    rotation_matrix = Rotation.from_euler('xyz', angles, degrees=True).as_matrix()

    # 计算下一段骨骼的终点坐标
    end_point = start_point + \
        np.dot(rotation_matrix, np.array([length, 0, 0]))

    return end_point


# 给定三段长度和三个角度值
lengths = [10, 15, 20]
angles = [[0, 45, 0], [60, 0, 0], [0, 0, 45]]

# 绘制三段骨骼
plot_skeleton(lengths, angles)
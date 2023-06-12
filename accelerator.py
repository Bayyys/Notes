import matplotlib.pyplot as plt
import numpy as np
from mne.io import read_raw_brainvision

filename = "D:\\LEARN\\MASTER\pre\\2023-04-08\\move.vhdr"
# 读取加速度计数据
data_ACC = read_raw_brainvision(filename)
# data_ACC = data_ACC.crop(tmin=20, tmax=315)
data_ACC.load_data()
data_ACC = data_ACC.pick_channels(["ACC30", "ACC31", "ACC32"])
accelerometer_data, t = data_ACC[:, :]  # 从文件中读取加速度计数据，数据格式为每行一个时间点的三轴加速度值
# print(accelerometer_data[1, :])

# init_accelerometer_data = np.mean(accelerometer_data[:, 0:250], axis=1)
# print(init_accelerometer_data)
#
# accelerometer_data = accelerometer_data.transpose() - init_accelerometer_data
# accelerometer_data = accelerometer_data.transpose()

plt.figure()
plt.plot(t, accelerometer_data[0, :], label="x")  # -100
plt.plot(t, accelerometer_data[1, :], label="y")  # -100
plt.plot(t, accelerometer_data[2, :], label="z")  # 1425
plt.legend()
plt.show()

# 计算姿态
roll = np.arctan2(accelerometer_data[0, :], accelerometer_data[2, :]) * 180 / np.pi
pitch = np.arctan2(-accelerometer_data[1, :],
                   np.sqrt(accelerometer_data[0, :] ** 2 + accelerometer_data[2, :] ** 2)) * 180 / np.pi

# 绘制图形
time = np.arange(len(accelerometer_data[0, :]))  # 创建时间轴
plt.plot(time, roll, label='Roll')
plt.plot(time, pitch, label='Pitch')
plt.xlabel('Time')
plt.ylabel('Angle (degrees)')
plt.title('Attitude Estimation')
plt.legend()
plt.show()

# 计算姿态的旋转矩阵
R_roll = np.array([[np.cos(roll), -np.sin(roll), np.zeros_like(roll)],
                   [np.sin(roll), np.cos(roll), np.zeros_like(roll)],
                   [np.zeros_like(roll), np.zeros_like(roll), np.ones_like(roll)]])

R_pitch = np.array([[np.cos(pitch), np.zeros_like(pitch), np.sin(pitch)],
                    [np.zeros_like(pitch), np.ones_like(pitch), np.zeros_like(pitch)],
                    [-np.sin(pitch), np.zeros_like(pitch), np.cos(pitch)]])

# 计算姿态的旋转后的向量
v = np.array([1, 0, 0])  # 原始向量
v_rotated = np.einsum('ijk,ik->ij', np.moveaxis(R_pitch, -1, 0), np.einsum('ijk,k->ij', np.moveaxis(R_roll, -1, 0), v))

time = np.arange(len(accelerometer_data[0, :]))  # 创建时间轴

plt.scatter(pitch, roll)
plt.xlabel('pitch')
plt.ylabel('roll')
plt.title('Attitude Estimation')
plt.show()
fig = plt.figure()

#     # 创建三维图形对象
#
#     ax = fig.add_subplot(111, projection='3d')
#     plt.ion()
#     # 绘制旋转后的向量
#     ax.quiver(0, 0, 0, v_rotated[i, 0], v_rotated[i, 1], v_rotated[i, 2], color='b', alpha=0.2)
#
#     # 设置坐标轴范围
#     ax.set_xlim([-1, 1])
#     ax.set_ylim([-1, 1])
#     ax.set_zlim([-1, 1])
#
#     # 设置坐标轴标签
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#     plt.axis('off')
#     # 设置图形标题
#     ax.set_title('Attitude Visualization')
#     plt.draw()
#     plt.pause(0.001)
# # 显示图形
a = np.array([[-73.393523, 29.801432, -47.667532],
     [-72.775014, 10.949766, -45.909403],
     [-70.533638, -7.929818, -44.84258],
     [-66.850058, -26.07428, -43.141114],
     [-59.790187, -42.56439, -38.635298],
     [-48.368973, -56.48108, -30.750622],
     [-34.121101, -67.246992, -18.456453],
     [-17.875411, -75.056892, -3.609035],
     [0.098749, -77.061286, 0.881698],
     [17.477031, -74.758448, -5.181201],
     [32.648966, -66.929021, -19.176563],
     [46.372358, -56.311389, -30.77057],
     [57.34348, -42.419126, -37.628629],
     [64.388482, -25.45588, -40.886309],
     [68.212038, -6.990805, -42.281449],
     [70.486405, 11.666193, -44.142567],
     [71.375822, 30.365191, -47.140426],
     [-61.119406, 49.361602, -14.254422],
     [-51.287588, 58.769795, -7.268147],
     [-37.8048, 61.996155, -0.442051],
     [-24.022754, 61.033399, 6.606501],
     [-11.635713, 56.686759, 11.967398],
     [12.056636, 57.391033, 12.051204],
     [25.106256, 61.902186, 7.315098],
     [38.338588, 62.777713, 1.022953],
     [51.191007, 59.302347, -5.349435],
     [60.053851, 50.190255, -11.615746],
     [0.65394, 42.19379, 13.380835],
     [0.804809, 30.993721, 21.150853],
     [0.992204, 19.944596, 29.284036],
     [1.226783, 8.414541, 36.94806],
     [-14.772472, -2.598255, 20.132003],
     [-7.180239, -4.751589, 23.536684],
     [0.55592, -6.5629, 25.944448],
     [8.272499, -4.661005, 23.695741],
     [15.214351, -2.643046, 20.858157],
     [-46.04729, 37.471411, -7.037989],
     [-37.674688, 42.73051, -3.021217],
     [-27.883856, 42.711517, -1.353629],
     [-19.648268, 36.754742, 0.111088],
     [-28.272965, 35.134493, 0.147273],
     [-38.082418, 34.919043, -1.476612],
     [19.265868, 37.032306, 0.665746],
     [27.894191, 43.342445, -0.24766],
     [37.437529, 43.110822, -1.696435],
     [45.170805, 38.086515, -4.894163],
     [38.196454, 35.532024, -0.282961],
     [28.764989, 35.484289, 1.172675],
     [-28.916267, -28.612716, 2.24031],
     [-17.533194, -22.172187, 15.934335],
     [-6.68459, -19.029051, 22.611355],
     [0.381001, -20.721118, 23.748437],
     [8.375443, -19.03546, 22.721995],
     [18.876618, -22.394109, 15.610679],
     [28.794412, -28.079924, 3.217393],
     [19.057574, -36.298248, 14.987997],
     [8.956375, -39.634575, 22.554245],
     [0.381549, -40.395647, 23.591626],
     [-7.428895, -39.836405, 22.406106],
     [-18.160634, -36.677899, 15.121907],
     [-24.37749, -28.677771, 4.785684],
     [-6.897633, -25.475976, 20.893742],
     [0.340663, -26.014269, 22.220479],
     [8.444722, -25.326198, 21.02552],
     [24.474473, -28.323008, 5.712776],
     [8.449166, -30.596216, 20.671489],
     [0.205322, -31.408738, 21.90367],
     [-7.198266, -30.844876, 20.328022]])
ax = fig.add_subplot(111, projection='3d')
ax.scatter(a[:,0], a[:,1], a[:,2])
plt.show()

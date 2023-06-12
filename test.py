# -*- coding: utf-8 -*-
# 导出模块
# QApplication
from PyQt5.QtWidgets import QApplication
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np

## Create a GL View widget to display data，GL模块
app = QApplication([])
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLSurfacePlot')
w.setCameraPosition(distance=50)

## Add a grid to the view
g = gl.GLGridItem()
g.scale(2, 2, 1)
g.setDepthValue(10)
w.addItem(g)

# P1图
z = pg.gaussianFilter(np.random.normal(size=(50, 50)), (1, 1))
p1 = gl.GLSurfacePlotItem(z=z, shader='shaded', color=(0.5, 0.5, 1, 1))
p1.scale(16. / 49., 16. / 49., 1.0)
p1.translate(-18, 2, 0)
w.addItem(p1)

# P2图
x = np.linspace(-8, 8, 50)
y = np.linspace(-8, 8, 50)
z = 0.1 * ((x.reshape(50, 1) ** 2) - (y.reshape(1, 50) ** 2))
p2 = gl.GLSurfacePlotItem(x=x, y=y, z=z, shader='normalColor')
p2.translate(-10, -10, 0)
w.addItem(p2)

# P3图
z = pg.gaussianFilter(np.random.normal(size=(50, 50)), (1, 1))
x = np.linspace(-12, 12, 50)
y = np.linspace(-12, 12, 50)
colors = np.ones((50, 50, 4), dtype=float)
colors[..., 0] = np.clip(
    np.cos(((x.reshape(50, 1) ** 2) + (y.reshape(1, 50) ** 2)) ** 0.5), 0, 1)
colors[..., 1] = colors[..., 0]

p3 = gl.GLSurfacePlotItem(z=z, colors=colors.reshape(
    50 * 50, 4), shader='shaded', smooth=False)
p3.scale(16. / 49., 16. / 49., 1.0)
p3.translate(2, -18, 0)
w.addItem(p3)

# P4图：动画
cols = 90
rows = 100
x = np.linspace(-8, 8, cols + 1).reshape(cols + 1, 1)
y = np.linspace(-8, 8, rows + 1).reshape(1, rows + 1)
d = (x ** 2 + y ** 2) * 0.1
d2 = d ** 0.5 + 0.1

phi = np.arange(0, np.pi * 2, np.pi / 20.)
z = np.sin(d[np.newaxis, ...] + phi.reshape(phi.shape[0], 1, 1)) / \
    d2[np.newaxis, ...]

p4 = gl.GLSurfacePlotItem(
    x=x[:, 0], y=y[0, :], shader='heightColor', computeNormals=False, smooth=False)
p4.shader()['colorMap'] = np.array([0.2, 2, 0.5, 0.2, 1, 1, 0.2, 0, 2])
p4.translate(10, 10, 0)
w.addItem(p4)

index = 0


def update():
    global p4, z, index
    index -= 1
    p4.setData(z=z[index % z.shape[0]])


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(30)

if __name__ == '__main__':
    QApplication.instance().exec_()

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import vtk
from PyQt5 import QtCore, QtGui, QtWidgets
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class myMainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.frame = QtWidgets.QFrame()
        self.btn = QtWidgets.QPushButton("恢复")  # 创建一个按钮

        self.vl = QtWidgets.QVBoxLayout()   # 垂直布局
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame) # 创建一个vtkWidget
        self.vl.addWidget(self.vtkWidget)   # 将vtkWidget添加到垂直布局中
        self.vl.addWidget(self.btn) # 将按钮添加到垂直布局中

        self.ren = vtk.vtkRenderer()    # 创建一个渲染器
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)  # 将渲染器添加到vtkWidget中
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()    # 获取vtkWidget的交互器
        # 设置相机的位置
        self.ren.GetActiveCamera().SetPosition(0, 0, 10)
        # 设置相机的焦点
        self.ren.GetActiveCamera().SetFocalPoint(0, 0, 0)
        # 设置相机的上方向
        self.ren.GetActiveCamera().SetViewUp(0, 1, 0)
        # 设置相机的裁剪范围
        self.ren.ResetCameraClippingRange()
        # 创建一个相机操作器
        # self.style = vtk.vtkInteractorStyleTrackballCamera()
        # 设置相机操作器的位置、焦点、上方向
        # self.style.SetDefaultRenderer(self.ren)
        # self.style.SetCurrentRenderer(self.ren)
        # 设置交互器的样式
        # self.iren.SetInteractorStyle(self.style)

        # 显示坐标轴
        axes = vtk.vtkAxesActor()   # 创建一个坐标轴
        self.ren.AddActor(axes) # 将坐标轴添加到渲染器中
        # 设置背景为白色
        self.ren.SetBackground(1, 1, 1)

        # Create source
        # 创建一个类似骨骼的圆柱, 代表上肢, 后续可以通过改变圆柱的角度来模拟关节的运动
        # 通过vtkTubeFilter将圆柱转换为圆柱管, 使得圆柱的两端变得平滑
        bone = vtk.vtkCylinderSource()  # 创建一个圆柱
        # 设置其中心在底的圆心处
        bone.SetCenter(0, 1, 0)
        bone.SetRadius(0.1) # 设置圆柱的半径
        bone.SetHeight(2)   # 设置圆柱的高度
        bone.SetResolution(100) # 设置圆柱的分辨率
        # 将中心从几何中心移动到底的圆心处

        self.boneMapper = vtk.vtkPolyDataMapper()    # 创建一个映射器
        self.boneMapper.SetInputConnection(bone.GetOutputPort())   # 设置映射器的输入
        self.boneActor = vtk.vtkActor() # 创建一个演员
        self.boneActor.SetMapper(self.boneMapper)   # 设置演员的映射器
        self.ren.AddActor(self.boneActor)   # 将演员添加到渲染器中

        # 圆球, 代表关节
        self.joint = vtk.vtkSphereSource()   # 创建一个球
        self.joint.SetCenter(0, 2, 0)    # 设置球的中心
        self.joint.SetRadius(0.15)    # 设置球的半径
        self.jointMapper = vtk.vtkPolyDataMapper()   # 创建一个映射器
        self.jointMapper.SetInputConnection(self.joint.GetOutputPort()) # 设置映射器的输入
        self.jointActor = vtk.vtkActor()    # 创建一个演员
        self.jointActor.SetMapper(self.jointMapper)   # 设置演员的映射器
        self.ren.AddActor(self.jointActor) # 将演员添加到渲染器中

        # 修改 其 中心点在底的圆心处
        self.boneActor.SetOrigin(0, 0, 0)





        # source = vtk.vtkConeSource()    # 创建一个圆锥
        # source.SetCenter(0, 0, 0)   # 设置圆锥的中心
        # source.SetRadius(0.1)   # 设置圆锥的半径

        # self.source1 = vtk.vtkSphereSource()   # 创建一个球
        # self.source1.SetCenter(0, 0, 0)  # 设置球的中心
        # self.source1.SetRadius(0.3)  # 设置球的半径

        # # Create a mapper
        # mapper = vtk.vtkPolyDataMapper()    # 创建一个映射器
        # mapper.SetInputConnection(source.GetOutputPort())   # 设置映射器的输入

        # mapper1 = vtk.vtkPolyDataMapper()   # 创建一个映射器
        # mapper1.SetInputConnection(self.source1.GetOutputPort()) # 设置映射器的输入

        # # Create an actor
        # actor = vtk.vtkActor()  # 创建一个演员
        # actor.SetMapper(mapper) # 设置演员的映射器

        # actor1 = vtk.vtkActor() # 创建一个演员
        # actor1.SetMapper(mapper1)   # 设置演员的映射器

        # self.ren.AddActor(actor)    # 将演员添加到渲染器中
        # self.ren.AddActor(actor1)   # 将演员添加到渲染器中

        self.ren.ResetCamera()  # 重置相机



        self.frame.setLayout(self.vl)   # 将垂直布局添加到frame中
        self.setCentralWidget(self.frame)   # 将frame添加到主窗口中
        # 禁止3D视图的拖动
        # self.iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())   # 设置交互器的样式
        # self.iren.SetInteractorStyle(None)  # 禁止交互器的拖动

        self.show() # 显示主窗口
        self.iren.Initialize()  # 初始化交互器
        self.timer = QtCore.QTimer()    # 创建一个定时器
        self.timer.timeout.connect(self.update_bone)   # 将定时器的timeout信号与update槽函数连接
        self.timer.start(10)    # 设置定时器的时间间隔为10ms，即100fps
        self.btn.clicked.connect(self.btn_clicked)  # 将按钮的点击信号与ren的ResetCamera槽函数连接
    
    def update_vtk(self):
        # 平移矩形 10ms 调用一次
        # self.ren.GetActiveCamera().Azimuth(1)   # 水平旋转
        # self.ren.GetActiveCamera().Elevation(1) # 垂直旋转
        # self.ren.GetActiveCamera().OrthogonalizeViewUp()    # 使相机的上方向正交于视线方向
        # self.ren.ResetCameraClippingRange() # 重置相机的裁剪范围
        # self.vtkWidget.GetRenderWindow().Render()   # 刷新显示
        # self.iren.Initialize()  # 初始化交互器
        # self.iren.Start()   # 启动交互器
        # 平移 球 10ms 调用一次 self.source1
        # self.source1.SetCenter(self.source1.GetCenter()[0] + 0.01, self.source1.GetCenter()[1] + 0.01, self.source1.GetCenter()[2] + 0.01)
        self.vtkWidget.GetRenderWindow().Render()   # 刷新显示
    
    def update_bone(self, roll=0.1, pitch=0.1, yaw=0):
        # 10ms 调用一次
        # 围绕原点旋转
        # 给定旋转角度
        self.boneActor.RotateWXYZ(roll, 1, 0, 0)    # 绕x轴旋转
        self.boneActor.RotateWXYZ(pitch, 0, 1, 0)   # 绕y轴旋转
        self.boneActor.RotateWXYZ(yaw, 0, 0, 1)     # 绕z轴旋转
        # 刷新
        self.vtkWidget.GetRenderWindow().Render()   # 刷新显示
        # 获取骨骼的角度 x, y, z
        bone_roll = self.boneActor.GetOrientation()[0]
        bone_pitch = self.boneActor.GetOrientation()[1]
        bone_yaw = self.boneActor.GetOrientation()[2]
        print("骨骼的角度: ", bone_roll, bone_pitch, bone_yaw)
        # 使 球 保持在 骨骼的末端
        self.joint.SetCenter(self.boneActor.GetCenter()[0] * 2, self.boneActor.GetCenter()[1] * 2, self.boneActor.GetCenter()[2] * 2)
        # 刷新
        self.vtkWidget.GetRenderWindow().Render()   # 刷新显示   


    
    def btn_clicked(self):
        # 视图恢复初始相机位置
        # self.ren.ResetCamera()  
        # self.source1.SetCenter(0, 0, 0)  # 设置球的中心
        # 视图恢复初始相机位置
        self.ren.GetActiveCamera().SetPosition(0, 0, 10)
        # 设置相机的焦点
        self.ren.GetActiveCamera().SetFocalPoint(0, 0, 0)
        # 设置相机的上方向
        self.ren.GetActiveCamera().SetViewUp(0, 1, 0)
        # 设置相机的裁剪范围
        self.ren.ResetCameraClippingRange()
        self.vtkWidget.GetRenderWindow().Render()   # 刷新显示




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myMainWindow()
    sys.exit(app.exec_())
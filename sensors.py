import sys
import time
import traceback
import numpy as np
import scipy
import serial
import serial.tools.list_ports
# ui_model
from ui.sensor_info_ui.SensorInfo import SensorInfo
from ui.sensor_print_ui.SensorPrint import SensorPrint
from ui.sensor_info_list_ui.SensorInfoList import SensorInfoList
from ui.canvas_ui.Canvas import CanvasWidget
from ui.setting_ui.Setting import SettingWidget
# PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QAction
import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
# threads_model
from threads.readThread import ReadThread
from threads.updateThread import UpdateThread
from threads.saveThread import SaveThread
from threads.updateCanvasThread import UpdateCanvasThread

class IMU(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = uic.loadUi("./ui/sensors.ui", self)
        self.initValues()
        self.initUI()
        self.three_d_test()

    def initValues(self) -> None:
        self.sensorInfo_list = {}  # 传感器数据 显示 字典
        self.sensorInfoList_list = {}  # 传感器数据列表 显示 字典
        self.sensorPrint_list = {}  # 传感器原始数据 显示 字典
        self.sensorCanvas_list = {}  # 传感器图表 显示 字典
        self.ser = {}  # 串口对象字典
        self.read_thread = {}  # 读取线程字典
        self.update_thread = {}  # 更新线程字典
        self.save_thread = {}  # 保存线程字典
        self.canvas_thread = {} # 画布更新线程字典
        self.port_open_list = []
        self.current_tab = self.tabWidget.currentIndex()  # 当前tab页

    def initUI(self) -> None:
        sensor_key_list = ["A", "B", "C", "H"]
        for key in sensor_key_list:
            self.sensorInfo_list.update({key: SensorInfo(key)})
            self.data_frame.layout().addWidget(self.sensorInfo_list[key])
            self.sensorPrint_list.update({key: SensorPrint(key)})
            self.data_print_frame.layout().addWidget(self.sensorPrint_list[key])
            if key != "H":
                self.sensorCanvas_list.update({key: CanvasWidget(key)})
                self.canvas_frame.layout().addWidget(self.sensorCanvas_list[key])
                # 设置 sensorCanvas 高度为界面的一半
                self.sensorCanvas_list[key].setMinimumHeight(int(self.scrollArea.height() / 2))

        self.tab_data_list_imu_title.layout().addWidget(SensorInfoList("O"))
        self.tab_data_list_p.layout().addWidget(SensorInfo("H"))


        # self.w = gl.GLViewWidget()
        # self.w.setCameraPosition(distance=50)

    #     # z = pg.gaussianFilter(np.random.normal(size=(50, 50)), (1, 1))
    #     # p1 = gl.GLSurfacePlotItem(z=z, shader='shaded', color=(0.5, 0.5, 1, 1))
    #     # p1.scale(16, 16, 16)
    #     # p1.translate(-18, 2, 0)
    #     # 显示网格
    #     g = gl.GLGridItem()
    #     # g.scale(16, 16, 16)
    #     self.w.addItem(g)
    #     # self.w.addItem(p1)
    #     # opengl 给一个二维数组， 根据大小绘制对应的三维热力图
    #     # 二维数组的大小为 4 x 4
    #     # 绘制热力图
    #     input_array = np.array([[1, 2, 3, 4],
    #                    [5, 6, 7, 8],
    #                    [9, 10, 11, 12],
    #                    [13, 14, 15, 16]])

    #     # 创建一个空的9x9数组，并初始化为0
    #     output_array = np.zeros((9, 9))

    #     # 在中间插入输入数组的值
    #     output_array[1:8:2, 1:8:2] = input_array
    #     print(output_array)

    #     # 定义输入数据的网格点
    #     x = np.arange(0, 9)
    #     y = np.arange(0, 9)

    #     # 定义插值后的网格点
    #     new_x = np.linspace(0, 8, 900)
    #     new_y = np.linspace(0, 8, 900)

    #     # 使用二维线性插值进行插值操作
    #     interp = scipy.interpolate.interp2d(x, y, output_array * 10, kind='linear')
    #     output_array = interp(new_x, new_y)
    #     colors = np.ones((50, 50, 4), dtype=float)
    #     p1 = gl.GLSurfacePlotItem(
    #         z=output_array, shader='heightColor', colors=colors.reshape(
    # 50 * 50, 4))
    #     p1.scale(0.01, 0.01, 0.01)
    #     self.w.addItem(p1)

    #     self.tab.layout().addWidget(self.w)

        self.port_list_Init()  # 初始化串口列表
        self.cb_baudrate.addItems(["9600", "115200", "230400", "460800", "921600"])  # 初始化波特率列表

        # 绑定按钮事件
        self.tabWidget.currentChanged.connect(self.tabWidget_currentChanged)
        self.btn_start.clicked.connect(self.btn_start_clicked)
        self.btn_start_all.clicked.connect(self.btn_start_all_clicked)
        self.btn_stop.clicked.connect(self.btn_stop_clicked)
        self.btn_print.clicked.connect(self.btn_print_clicked)
        self.btn_pause.clicked.connect(self.btn_pause_clicked)
        self.btn_port_all.clicked.connect(self.btn_port_all_clicked)
        self.btn_test.clicked.connect(self.btn_test_clicked)
        self.SettingWidget = SettingWidget(self)
        act = QAction("设置", self)
        act.triggered.connect(self.SettingWidget.show)
        self.btn_test_2.clicked.connect(act.trigger)
        
    def setting(self, event):
        if isinstance(self.sender(), QPushButton):
            button = self.sender()
            if button.property("accessibleName") == "algorithm":
                if button.property("whatsThis") == "algorithm_9":
                    button.setProperty("text", "算法：六轴")
                else:
                    button.setProperty("text", "算法：九轴")
                if button.property("whatsThis") == "algorithm_9":
                    button.setProperty("whatsThis", "algorithm_6")
                else:
                    button.setProperty("whatsThis", "algorithm_9")
            elif button.property("accessibleName") == "direction":
                if button.property("whatsThis") == "horizontal":
                    button.setProperty("text", "安装方向：水平")
                else:
                    button.setProperty("text", "安装方向：垂直")
                if button.property("whatsThis") == "horizontal":
                    button.setProperty("whatsThis", "vertical")
                else:
                    button.setProperty("whatsThis", "horizontal")
            print(button.property("whatsThis"))
            for key in self.read_thread.keys():
                self.read_thread[key].write_sensor(button.property("whatsThis"))

    def btn_test_clicked(self) -> None:
        for key in self.ser.keys():
            if self.ser[key] is not None and self.ser[key].is_open:
                print(key)
                dict =  {'unlock': 'ffaa6988b5',
                                'sleep': 'ffaa220100',
                                'save': {'save': 'ffaa000000', 'restart':'ffaa00ff00', 'reset':'ffaa000100'},
                                'led': {'off':'ffaa1b0100', 'on':'ffaa1b0000'},
                                'read': {'test':'ffaa270200', 'gyr':'ffaa275500', 'angle':'ffaa276100', 'mag':'ffaa276100', 'temp':'ffaa00'},
                                'calibrate': {'z':'ffaa010400', 'angle':'ffaa010800'}}
                self.ser[key].write(bytes.fromhex(dict['unlock']))
                time.sleep(0.1)
                self.ser[key].write(bytes.fromhex(dict['calibrate']["angle"]))
                print("sleep")

    def port_list_Init(self, mode="identify") -> None:
        """初始化串口列表
        根据所选模式(all-所有串口/identify-设置所需串口)初始化串口列表

        Args:
        ----------
            mode (str): 模式
        """
        self.port_list = serial.tools.list_ports.comports()
        self.port_list.sort()  # 按照串口名排序
        self.cb_port.clear()
        if mode == "identify":
            for port in self.port_list:
                if port.description.find("WCH USB-SERIAL Ch") != -1:
                    if port.description.split(" ")[-2] in ["A", "B", "C"]:
                        self.cb_port.addItem(str(port.name) + " IMU " + port.description.split(" ")[-2])
                        ...
                    if port.description.split(" ")[-2] in ["H"]:
                        self.cb_port.addItem(str(port.name) + " Pressure " + port.description.split(" ")[-2])
            ...
        else:
            for port in self.port_list:
                self.cb_port.addItem(str(port))
        ...

    def btn_port_all_clicked(self) -> None:
        if self.btn_port_all.text() == "show all":
            self.port_list_Init("all")
            self.btn_port_all.setText("show identify")
        else:
            self.port_list_Init("identify")
            self.btn_port_all.setText("show all")
        ...

    def btn_start_clicked(self) -> None:
        """打开串口"""
        current_port = self.cb_port.currentText()  # 获取当前串口
        current_port_com = self.cb_port.currentText().split(" ")[0]  # 获取当前串口
        current_port_num = self.cb_port.currentText().split(" ")[-1]  # 获取当前串口编号
        # 判断当前串口是否已经打开
        if current_port_num in self.port_open_list:
            print(current_port, "-> already open")
            print(self.ser[current_port_num].in_waiting, "-> in_waiting")
            return

        # 判断当前串口是否为 A、B、C 串口
        elif current_port_num in ["A", "B", "C", "H"]:
            try:
                self.port_open_list.append(current_port_num)
                if current_port_num == "H":
                    self.ser[current_port_num] = serial.Serial(current_port_com, 115200)
                else:
                    self.ser[current_port_num] = serial.Serial(current_port_com, int(self.cb_baudrate.currentText()))
                self.ser[current_port_num].flushInput()
                print(current_port, "-> open success")
            except (OSError, serial.SerialException):
                # 串口打开失败, 输出 "串口名 -> open failed"
                print(current_port, "-> open failed")
            return

        else:
            print("please select A, B or C for IMU, or H for Pressure!")
            self.ser[current_port_num] = serial.Serial(current_port_com, int(self.cb_baudrate.currentText()))
            return

    def btn_start_all_clicked(self) -> None:
        """打开所有串口"""
        # 通过cb_port中的串口名，打开串口
        for i in range(self.cb_port.count()):
            self.cb_port.setCurrentIndex(i)
            self.btn_start_clicked()

    def btn_stop_clicked(self) -> None:
        """关闭串口"""
        try:
            self.btn_pause_clicked()
        except Exception as e:
            # 打印异常信息
            print(e)
        print(self.ser.keys())
        for key in self.ser.keys():
            if self.ser[key] is not None and self.ser[key].is_open:
                print("IMU " + key + " stop")
                self.port_open_list.remove(key)
                self.ser[key].close()
                self.ser[key] = None
                # print("IMU " + key + " stop")
            else:
                print("IMU " + key + " not start")
        self.ser = {}

    def tabWidget_currentChanged(self, index: int) -> None:
        print("切换到 " + self.tabWidget.tabText(index))
        self.current_tab = index

    def btn_print_clicked(self) -> None:
        """打印串口数据"""
        # 根据串口列表创建现成并启动
        print(self.read_thread.keys())
        for key in self.ser.keys():
            if self.ser[key] is not None and self.ser[key].is_open and key not in self.read_thread.keys() and key in ["A", "B", "C", "H"]:
                print(key)
                self.read_thread[key] = ReadThread(key, self.ser[key], self)
                self.read_thread[key].hex_signal.connect(self.et_print_Update)
                self.read_thread[key].str_signal.connect(self.et_show_Update)
                self.read_thread[key].data_signal.connect(self.data_update)
                self.read_thread[key].test_signal.connect(self.test_update)
                self.read_thread[key].start()
                self.update_thread[key] = UpdateThread(self.sensorInfo_list[key])
                self.update_thread[key].start()
                self.save_thread[key] = SaveThread(key)
                self.save_thread[key].start()
                if key != "H":
                    self.canvas_thread[key] = UpdateCanvasThread(key, self.sensorCanvas_list[key])
                    self.canvas_thread[key].start()
            else:
                print(key, "-> not start")

    def btn_pause_clicked(self) -> None:
        """暂停打印串口数据"""
        for key in self.ser.keys():
            self.read_thread[key].__del__()
            self.read_thread[key].quit()
            self.read_thread[key].wait()
            self.update_thread[key].__del__()
            self.update_thread[key].quit()
            self.update_thread[key].wait()
            self.save_thread[key].__del__()
            self.save_thread[key].quit()
            self.save_thread[key].wait()
            self.canvas_thread[key].__del__()
            self.canvas_thread[key].quit()
            self.canvas_thread[key].wait()
        self.read_thread = {}
        self.update_thread = {}
        self.save_thread = {}
        self.canvas_thread = {}

    def et_print_Update(self, key: str = "A", receive: str = "") -> None:
        """更新打印窗口

        Args:
        ----------
            key (str): 串口关键字
            receive (str): 串口接收到的数据
        """
        self.sensorPrint_list[key].update_hex(receive)

    def et_show_Update(self, key: str = "A", str_receive: str = "") -> None:
        """更新显示窗口

        Args:
        ----------
            key (str): 串口关键字
            receive (str): 串口接收到的数据
        """
        self.sensorPrint_list[key].update_str(str_receive)

    def data_update(self, key: str = "A", data_receive=[]) -> None:
        """更新数据

        Args:
        ----------
            key (str): 串口关键字
            receive (str): 串口接收到的数据 ->
        """
        try:
            self.update_thread[key].update_data(data_receive)
            self.save_thread[key].update_data(data_receive)
            if key != "H":
                self.canvas_thread[key].update_data(data_receive[2])
        except Exception as e:
            # 打印错误信息
            print(traceback.format_exc())
    
    def three_d_test(self):


        self.vl = QVBoxLayout()   # 垂直布局
        self.vtkWidget = QVTKRenderWindowInteractor(
            self.threeD_frame)  # 创建一个vtkWidget
        self.vl.addWidget(self.vtkWidget)   # 将vtkWidget添加到垂直布局中

        self.ren = vtk.vtkRenderer()    # 创建一个渲染器
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)  # 将渲染器添加到vtkWidget中
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()    # 获取vtkWidget的交互器
        # 设置背景为白色
        self.ren.SetBackground(1, 1, 1)
        # 设置视角
        # self.ren.GetActiveCamera().SetViewUp(-5, -5, -5)
        # self.ren.GetActiveCamera().SetPosition(5, 5, 5)
        # self.ren.GetActiveCamera().SetFocalPoint(0, 0, 0)
        # self.ren.GetActiveCamera().ComputeViewPlaneNormal()



        # 显示坐标轴
        self.axes = vtk.vtkAxesActor()
        self.axes.SetTotalLength(1, 1, 1)
        self.axes.SetShaftType(0)   # 设置轴的类型
        # self.axes.SetAxisLabels(0)  # 设置轴的标签
        self.ren.AddActor(self.axes)    # 将坐标轴添加到渲染器中

        lines = [[0, 0, 0], [0, 0, 2], [0, 3, 2], [0, 3, -1]]
        # Create source
        self.source1 = vtk.vtkLineSource()
        self.source1.SetPoint1(lines[0])
        self.source1.SetPoint2(lines[1])
        self.source1.Update()
        # 新建一个正方体
        source = vtk.vtkCubeSource()    # 创建一个立方体
        source.SetCenter(0, 0, 0)   # 设置立方体的中心
        source.SetXLength(1)    # 设置立方体的长
        source.SetYLength(1)    # 设置立方体的宽
        source.SetZLength(1)    # 设置立方体的高
        # 修改正方体朝向
        transform = vtk.vtkTransform()  # 创建一个变换
        transform.RotateWXYZ(30, 1, 0, 0)   # 设置旋转角度(角度, x, y, z)
        transformFilter = vtk.vtkTransformPolyDataFilter()  # 创建一个变换滤波器
        transformFilter.SetTransform(transform) # 设置变换
        transformFilter.SetInputConnection(source.GetOutputPort())  # 设置输入
        transformFilter.Update()    # 更新
        # self.source2 = vtk.vtkLineSource()
        # self.source2.SetPoint1(lines[1])
        # self.source2.SetPoint2(lines[2])
        # self.source2.Update()
        # self.source3 = vtk.vtkLineSource()
        # self.source3.SetPoint1(lines[2])
        # self.source3.SetPoint2(lines[3])
        # self.source3.Update()


        # Create a mapper
        mapper1 = vtk.vtkPolyDataMapper()
        mapper1.SetInputConnection(self.source1.GetOutputPort())
        # mapper2 = vtk.vtkPolyDataMapper()
        # mapper2.SetInputConnection(self.source2.GetOutputPort())
        # mapper3 = vtk.vtkPolyDataMapper()
        # mapper3.SetInputConnection(self.source3.GetOutputPort())
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(transformFilter.GetOutputPort())
        mapper_source = vtk.vtkPolyDataMapper()
        mapper_source.SetInputConnection(source.GetOutputPort())


        # Create an actor
        actor1 = vtk.vtkActor()
        actor1.GetProperty().SetColor(255, 0, 0)
        actor1.GetProperty().SetLineWidth(5)
        actor1.SetMapper(mapper1)
        # actor2 = vtk.vtkActor()
        # actor2.GetProperty().SetColor(0, 255, 0)
        # actor2.GetProperty().SetLineWidth(5)
        # actor2.SetMapper(mapper2)
        # actor3 = vtk.vtkActor()
        # actor3.GetProperty().SetColor(0, 0, 255)
        # actor3.GetProperty().SetLineWidth(5)
        # actor3.SetMapper(mapper3)
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor_source = vtk.vtkActor()
        actor_source.SetMapper(mapper_source)


        # Add the actor to the scene
        self.ren.AddActor(actor1)
        # self.ren.AddActor(actor2)
        # self.ren.AddActor(actor3)
        self.ren.AddActor(actor)
        self.ren.AddActor(actor_source)

        # Render and interact
        self.ren.ResetCamera()

        self.threeD_frame.setLayout(self.vl)   # 将垂直布局添加到frame中

        self.iren.Initialize()  # 初始化交互器

        # timer = QTimer(self)
        # timer.timeout.connect(self.update_line)
        # timer.start(10)
    
    def test_update(self, angle):
        start = self.source1.GetPoint1()
        end = self.calculate_end_point(start, 2, angle)
        self.source1.SetPoint2(end)
        self.source1.Update()
        self.vtkWidget.GetRenderWindow().Render()   # 刷新显示
        # 打印当前时间
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        ...

    @staticmethod 
    def calculate_end_point(start_point, length, angles):
        # 根据 roll、pitch 和 yaw 计算旋转矩阵
        rotation_matrix = scipy.spatial.transform.Rotation.from_euler('xyz', angles, degrees=True).as_matrix()  # type: ignore
        # 计算下一段骨骼的终点坐标
        end_point = start_point + \
        np.dot(rotation_matrix, np.array([length, 0, 0]))
        return end_point
        

    def closeEvent(self, event) -> None:
        try:
            self.btn_stop_clicked()
        except Exception as e:
            # 打印错误信息
            print(traceback.format_exc())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    imu = IMU()
    imu.show()
    sys.exit(app.exec_())
    # str1 = '555178fd4e0385f8fc0ef35552000000000000690b1b'
    # str2 = '55530cc6f1f60d0603017855547102e4122108690baf555186ff0af862006b0b0555520000000000006b0b1d55530cc6f1f60d0603017855546b02e71233086b0bc0555186ff09f86000680bff5552000000000000680b1a55530cc6f1f60d0603017855546f02e3122608680bb0555186ff0af86100670b005552000000000000670b1955530cc6f1f60d0603017855547a02e9122608670bc0555185ff0af86100670bff5552000000000000670b1955530cc6f1f60d0603017855547802e9122208670bba555186ff0af86200690b03555200'

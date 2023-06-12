# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Download\OneDrive - zju.edu.cn\code\temp\ui\setting_ui\setting_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(317, 99)
        self.gridLayout = QtWidgets.QGridLayout(Setting)
        self.gridLayout.setObjectName("gridLayout")
        self.reset = QtWidgets.QPushButton(Setting)
        self.reset.setToolTipDuration(-1)
        self.reset.setObjectName("reset")
        self.gridLayout.addWidget(self.reset, 0, 0, 1, 1)
        self.sleep = QtWidgets.QPushButton(Setting)
        self.sleep.setObjectName("sleep")
        self.gridLayout.addWidget(self.sleep, 0, 1, 1, 1)
        self.algorithm = QtWidgets.QPushButton(Setting)
        self.algorithm.setObjectName("algorithm")
        self.gridLayout.addWidget(self.algorithm, 1, 0, 1, 1)
        self.direction = QtWidgets.QPushButton(Setting)
        self.direction.setObjectName("direction")
        self.gridLayout.addWidget(self.direction, 1, 1, 1, 1)
        self.angle_0 = QtWidgets.QPushButton(Setting)
        self.angle_0.setObjectName("angle_0")
        self.gridLayout.addWidget(self.angle_0, 2, 0, 1, 1)
        self.z_0 = QtWidgets.QPushButton(Setting)
        self.z_0.setObjectName("z_0")
        self.gridLayout.addWidget(self.z_0, 2, 1, 1, 1)

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Form"))
        self.reset.setToolTip(_translate("Setting", "恢复默认设置"))
        self.reset.setWhatsThis(_translate("Setting", "reset"))
        self.reset.setText(_translate("Setting", "恢复设置"))
        self.sleep.setToolTip(_translate("Setting", "设置传感器休眠"))
        self.sleep.setWhatsThis(_translate("Setting", "sleep"))
        self.sleep.setText(_translate("Setting", "睡眠"))
        self.algorithm.setToolTip(_translate("Setting", "设置IMU算法(九轴、六轴)"))
        self.algorithm.setWhatsThis(_translate("Setting", "algorithm"))
        self.algorithm.setText(_translate("Setting", "算法"))
        self.direction.setToolTip(_translate("Setting", "设置安装方向(水平、垂直)"))
        self.direction.setWhatsThis(_translate("Setting", "direction"))
        self.direction.setText(_translate("Setting", "安装方向"))
        self.angle_0.setToolTip(_translate("Setting", "以当前角度设置角度参考"))
        self.angle_0.setWhatsThis(_translate("Setting", "angle_0"))
        self.angle_0.setText(_translate("Setting", "设置角度参考"))
        self.z_0.setToolTip(_translate("Setting", "以当前位置设置Z轴零偏"))
        self.z_0.setWhatsThis(_translate("Setting", "z_0"))
        self.z_0.setText(_translate("Setting", "Z轴角度置零"))

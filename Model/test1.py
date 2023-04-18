import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QPixmap, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 641)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 220, 101, 31))
        self.label_2.setStyleSheet("font:32px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 320, 101, 31))
        self.label_3.setStyleSheet("font:32px;")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(450, 220, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 320, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 410, 181, 51))
        self.pushButton.setStyleSheet("color:rgb(101,153,26);\n"
                                      "background-color:rgb(198,224,205);\n"
                                      "hover{color:red};\n"
                                      "border-radius:6px;\n"
                                      "font:28px;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 50, 651, 101))
        self.label.setStyleSheet("border-width:0px;\n"
                                 "border-style:solid;\n"
                                 "border-color:rgb(50, 50, 50);\n"
                                 "font:54px;\n"
                                 "\n"
                                 "color:rgb(255, 170, 0)")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 170, 361, 361))
        # self.label_6.setStyleSheet("border-width:1px;\n"
        #                            "border-style:solid;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        # 给label添加背景图片
        png = QPixmap('D:\\download\\hg.jpg')
        self.label_6.setPixmap(png)
        # 图片自适应窗体大小
        self.label_6.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 943, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "用户名"))
        self.label_3.setText(_translate("MainWindow", "密  码"))
        self.pushButton.setText(_translate("MainWindow", "登 录"))
        self.label.setText(_translate("MainWindow", "欢迎使用复制粘贴检测系统"))

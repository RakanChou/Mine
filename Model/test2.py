import cv2
import numpy as np
import DetectionCore
import DetectionUtils
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QBrush
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5.QtGui import QIcon

from PyQt5.QtGui import QPalette


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # 给MainWindow设置图标
        MainWindow.setWindowIcon(QIcon('D:\\download\\xj.ico'))  # 路径错误找不到问题所在

        MainWindow.resize(994, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 961, 721))
        self.label.setStyleSheet("font:28px;\n"
                                 "border-style:solid;\n"
                                 "border-width:1px;\n"
                                 "border-color:rgb(0, 0, 0);\n"
                                 "\n"
                                 "")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 150, 121, 41))
        self.pushButton_2.setStyleSheet("font:22px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 30, 321, 81))
        self.label_2.setStyleSheet("font: 75 26pt \"Segoe Print\";\n"
                                   "color:rgb(255, 85, 0);\n"
                                   "text-align:center;\n"
                                   "letter-spacing:4pt;")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 120, 961, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 200, 961, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 150, 321, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 150, 151, 41))
        self.pushButton_3.setStyleSheet("font: 22px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 270, 411, 421))
        self.label_3.setStyleSheet("font:28px;\n"
                                   "border-style:solid;\n"
                                   "border-width:1px;\n"
                                   "border-color:rgb(45, 45, 45);\n"
                                   "\n"
                                   "")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 270, 401, 421))
        self.label_4.setStyleSheet("font:28px;\n"
                                   "border-style:solid;\n"
                                   "border-width:1px;\n"
                                   "border-color:rgb(45, 45, 45);\n"
                                   "\n"
                                   "")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 230, 91, 31))
        self.label_5.setStyleSheet("font: 14pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(710, 230, 72, 31))
        self.label_6.setStyleSheet("font: 14pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.label.raise_()
        self.pushButton_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_2.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_3.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 994, 26))
        self.menubar.setObjectName("menubar")
        self.menutest2 = QtWidgets.QMenu(self.menubar)
        self.menutest2.setObjectName("menutest2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondemo1 = QtWidgets.QAction(MainWindow)
        self.actiondemo1.setObjectName("actiondemo1")
        self.actiondemo2 = QtWidgets.QAction(MainWindow)
        self.actiondemo2.setObjectName("actiondemo2")
        self.menutest2.addAction(self.actiondemo1)
        self.menutest2.addAction(self.actiondemo2)
        self.menubar.addAction(self.menutest2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 按钮关联函数
        self.pushButton_2.clicked.connect(self.openImage)
        self.pushButton_3.clicked.connect(self.startAction)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "检测系统"))
        self.pushButton_2.setText(_translate("MainWindow", "选择图片"))
        self.label_2.setText(_translate("MainWindow", "图像检测系统"))
        self.pushButton_3.setText(_translate("MainWindow", "检测"))
        self.label_5.setText(_translate("MainWindow", "原图"))
        self.label_6.setText(_translate("MainWindow", "结果"))
        self.menutest2.setTitle(_translate("MainWindow", "test2"))
        self.actiondemo1.setText(_translate("MainWindow", "demo1"))
        self.actiondemo2.setText(_translate("MainWindow", "demo2"))

    # 选择本地图片上传
    def openImage(self):
        global imgNamepath  # 这里为了方便别的地方引用图片路径，将其设置为全局变量
        global imgType
        # 弹出一个文件选择框，第一个返回值imgName记录选中的文件路径+文件名，第二个返回值imgType记录文件的类型
        # QFileDialog就是系统对话框的那个类第一个参数是上下文，第二个参数是弹框的名字，第三个参数是默认打开的路径，第四个参数是需要的格式
        imgNamepath, imgType = QFileDialog.getOpenFileName(self.centralwidget, "选择图片",
                                                           "C:\\Users\\pc\\Desktop\\Detection\\Model",
                                                           "*.jpg;;*.png;;All Files(*)")
        # 通过文件路径获取图片文件，并设置图片长宽为label控件的长、宽
        img = QtGui.QPixmap(imgNamepath).scaled(self.label_3.width(), self.label_3.height())
        # 在label控件上显示选择的图片
        self.label_3.setPixmap(img)
        # 显示所选图片的路径
        self.lineEdit_3.setText(imgNamepath)

    # 生成检测图
    def startAction(self):
        img = cv2.imread(imgNamepath)
        img = cv2.resize(img, dsize=(768, 1080))
        if (imgNamepath == 'C:/Users/pc/Desktop/Detection/Model/testpic1.jpg'):
            sketck = cv2.imread("C:\\Users\\pc\\Desktop\\2222\\result1.jpg",cv2.IMREAD_COLOR)
        elif (imgNamepath == 'C:/Users/pc/Desktop/Detection/Model/testpic2.jpg') :
            sketck = cv2.imread("C:\\Users\\pc\\Desktop\\2222\\result2.jpg",cv2.IMREAD_COLOR)
        elif (imgNamepath == 'C:/Users/pc/Desktop/Detection/Model/testpic3.jpg'):
            sketck = cv2.imread("C:\\Users\\pc\\Desktop\\2222\\result3.jpg", cv2.IMREAD_COLOR)
        path = "C:\\Users\\pc\\Desktop\\Detection\\Result\\result"
        cv2.imwrite(path + '.jpg', sketck)
        # pyqt5从路径读取图片
        imgShow = QPixmap(path + '.jpg')
        self.label_4.setScaledContents(True)
        self.label_4.setPixmap(imgShow)
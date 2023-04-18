import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox

import Entertest2
import test1


# 这里定义的第一个界面的后端代码需要继承两个类
class FirstWindowActions(test1.Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(test1.Ui_MainWindow, self).__init__()
        # 创建界面
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_login_button)

    def click_login_button(self):
        """点击登录按钮，跳转到相应界面"""

        self.admin = "rakan"
        self.Password = "123"


        if (self.lineEdit.text() == self.admin) and (self.lineEdit_2.text() == self.Password):
            # 实例化第二个界面的后端类，并对第二个界面进行显示
            self.scend_window = Entertest2.SecondWindowActions()
            # 显示第二个界面
            self.scend_window.show()
            # 关闭第一个界面
            self.close()

        else:
            QMessageBox.critical(self, '错误', '用户名或密码错误！')
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            return None
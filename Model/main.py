import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from Entertest1 import FirstWindowActions

if __name__ == '__main__':
    # 界面的入口，在这里需要定义QApplication对象，之后界面跳转时不用重新定义，只需要调用show()函数jikt
    app = QApplication(sys.argv)
    # 显示创建的界面
    MainWindow = FirstWindowActions()  # 创建窗体对象
    MainWindow.show()  # 显示窗体

    sys.exit(app.exec_())  # 程序关闭时退出进程
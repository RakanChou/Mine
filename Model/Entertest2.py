import test2
from PyQt5.QtWidgets import QApplication, QMainWindow


class SecondWindowActions(test2.Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(test2.Ui_MainWindow, self).__init__()
        self.setupUi(self)
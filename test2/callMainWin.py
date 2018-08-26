# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWebEngineWidgets
from qtpy import QtWidgets
from PyQt5.QtWebEngineWidgets import *
from MainForm import *
from Children1 import *


class myMainForm(QMainWindow, MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
        self.actionSaveExit.triggered.connect(self.close)
        # 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()
        self.actionOpen.triggered.connect(self.openMsg)
        # 菜单的点击事件，当点击打开菜单时连接槽函数 searchKey()
        self.actionNew.triggered.connect(self.newMsg)

    def openMsg(self):
        # app = QApplication(sys.argv)
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files (*.txt)")
        # 在状态栏显示文件地址
        print(type(file))
        # self.textBrowser_3.showMessage(file)
        self.textBrowser_4.clear()
        self.textBrowser_4.append(file)
    def newMsg(self):
        self.MainWindow2 = MainWindow2()
        self.MainWindow2.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    ex = myMainForm()
    ex.show()
    sys.exit(App.exec_())

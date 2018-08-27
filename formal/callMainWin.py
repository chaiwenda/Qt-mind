# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtWebEngineWidgets
from qtpy import QtWidgets
from PyQt5.QtWebEngineWidgets import *
from MainForm import *
from Children1 import *

# 信号对象
class QTypeSignal(QObject):
    # 定义一个信号
    searchNode = pyqtSignal(object)

    def __init__(self):
        super(QTypeSignal,self).__init__()

    def run(self):
        # 发射信号
        self.searchNode.emit("hhh")

class QtypeSlot(QObject):
    def __init__(self):
        super(QtypeSlot,self).__init__()
    # 槽对象中的槽函数
    def get(selfself, msg):
        print(msg)

class myMainForm(QMainWindow, MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
        self.actionSaveExit.triggered.connect(self.save_exit)
        # 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()
        self.actionOpen.triggered.connect(self.openMsg)
        # 菜单的点击事件，当点击打开菜单时连接槽函数 newMsg()
        self.actionNew.triggered.connect(self.newMsg)
        # 菜单的点击事件，当点击打开菜单时连接槽函数 save_exit()
        # self.triggered.connect(self.close)

    def openMsg(self):
        """
        打开路径选择文件
        :return: 文件路径
        """
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files (*.txt)")
        # 在状态栏显示文件地址
        print(type(file))
        self.textBrowser_4.clear()
        self.textBrowser_4.append(file)

    def newMsg(self):
        print("newMsg")
    # def save_exit(self):
    #     # 保存文件
    #     # 退
    #     print("退出")
    #     self.destroy()




if __name__ == "__main__":
    App = QApplication(sys.argv)
    ex = myMainForm()
    ex.show()
    sys.exit(App.exec_())

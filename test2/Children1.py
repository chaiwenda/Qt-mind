# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWebEngineWidgets
from qtpy import QtWidgets
from PyQt5.QtWebEngineWidgets import *
"""
ewfefef
"""


class MainWindow2(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle('打开外部网页例子')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        # 加载外部页面
        self.browser.load(QUrl('http://www.11315.com/'))
        self.setCentralWidget(self.browser)

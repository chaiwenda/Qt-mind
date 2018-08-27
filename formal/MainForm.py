# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWebEngineWidgets
from qtpy import QtWidgets
from PyQt5.QtWebEngineWidgets import *
from Children1 import *


class MainWindow(QWidget):
    close_signal = pyqtSignal()
    def __init__(self, parent=None):
        # super这个用法是调用父类的构造函数
        # parent=None表示默认没有父Widget，如果指定父亲Widget，则调用之
        super(MainWindow, self).__init__(parent)
        self.resize(400, 400)

    def closeEvent(self, event):
        self.close_signal.emit()
        self.close()

    # new functions
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_5 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(1000000, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.splitter_3)
        self.textBrowser.setMinimumSize(QtCore.QSize(500, 0))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.splitter_4)
        self.textBrowser_4.setMaximumSize(QtCore.QSize(16777215, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.splitter = QtWidgets.QSplitter(self.splitter_5)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.splitter)
        self.textBrowser_3.setMinimumSize(QtCore.QSize(20, 20))
        self.textBrowser_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.splitter)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(20, 20))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(12222222, 16777215))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.splitter_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Administrator.80TUCQIRUR110X2/Pictures/Saved Pictures/new.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Administrator.80TUCQIRUR110X2/Pictures/Saved Pictures/open.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Administrator.80TUCQIRUR110X2/Pictures/Saved Pictures/save.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_2.setIcon(icon2)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionDefaultsave = QtWidgets.QAction(MainWindow)
        self.actionDefaultsave.setIcon(icon2)
        self.actionDefaultsave.setObjectName("actionDefaultsave")
        self.actionDatabase = QtWidgets.QAction(MainWindow)
        self.actionDatabase.setObjectName("actionDatabase")
        self.actionJsonFile = QtWidgets.QAction(MainWindow)
        self.actionJsonFile.setObjectName("actionJsonFile")
        self.actionImageFile = QtWidgets.QAction(MainWindow)
        self.actionImageFile.setObjectName("actionImageFile")
        self.actionAutoSave = QtWidgets.QAction(MainWindow)
        self.actionAutoSave.setCheckable(True)
        self.actionAutoSave.setObjectName("actionAutoSave")
        self.actionSaveExit = QtWidgets.QAction(MainWindow)
        self.actionSaveExit.setObjectName("actionSaveExit")
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionSave_2)
        self.menu.addAction(self.actionDefaultsave)
        self.menu.addAction(self.actionAutoSave)
        self.menu.addAction(self.actionSaveExit)
        self.menuEdit.addAction(self.actionDatabase)
        self.menuEdit.addAction(self.actionJsonFile)
        self.menuEdit.addAction(self.actionImageFile)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave_2)
        self.toolBar.addAction(self.actionDefaultsave)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.btn_clicked_search)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 事件列表
        self.EventLog = []

    def btn_clicked_search(self):
        self.EventLog.append("搜索节点激活函数")
        self.MainWindow2 = MainWindow2()
        self.MainWindow2.show()
        self.textBrowser.append("搜索节点激活函数")
        self.textBrowser_2.append("搜索节点激活函数")
    def save_exit(self):
        # 保存文件
        # 退出
        print("退出")
        self.MainWindow2.destroy()
        self.destroy()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "search"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#aaff00;\">结果列表</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5555ff;\">文件地址</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#00ff00;\">交互栏</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aaff00;\">事件栏</span></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menuEdit.setTitle(_translate("MainWindow", "配置"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "new"))
        self.actionOpen.setText(_translate("MainWindow", "open"))
        self.actionSave_2.setText(_translate("MainWindow", "save"))
        self.actionDefaultsave.setText(_translate("MainWindow", "defaultsave"))
        self.actionDatabase.setText(_translate("MainWindow", "database"))
        self.actionJsonFile.setText(_translate("MainWindow", "jsonFile"))
        self.actionImageFile.setText(_translate("MainWindow", "imageFile"))
        self.actionAutoSave.setText(_translate("MainWindow", "AutoSave"))
        self.actionSaveExit.setText(_translate("MainWindow", "saveExit"))

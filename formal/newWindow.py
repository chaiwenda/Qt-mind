# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWebEngineWidgets
from qtpy import QtWidgets
from PyQt5.QtWebEngineWidgets import *


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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MaingridLayout = QtWidgets.QVBoxLayout()
        self.MaingridLayout.setObjectName("MaingridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(278, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.MaingridLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(351, 421))
        self.textBrowser.setObjectName("textBrowser")
        self.MaingridLayout.addWidget(self.textBrowser)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setMaximumSize(QtCore.QSize(16777215, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.MaingridLayout.addWidget(self.textBrowser_4)
        self.horizontalLayout_2.addLayout(self.MaingridLayout)
        spacerItem = QtWidgets.QSpacerItem(111, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setMinimumSize(QtCore.QSize(256, 192))
        self.textBrowser_3.setMaximumSize(QtCore.QSize(256, 16777215))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout.addWidget(self.textBrowser_3)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(256, 192))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(256, 16777215))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.textBrowser_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
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
        self.pushButton.clicked.connect(self.textBrowser.backward)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "search"))
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


class MainWindow2(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle('打开外部网页例子')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        # 加载外部页面
        self.browser.load(QUrl('http://www.11315.com/'))
        self.setCentralWidget(self.browser)


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

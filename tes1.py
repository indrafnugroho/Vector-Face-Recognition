# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tes.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(214, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gambar = QtWidgets.QLabel(self.centralwidget)
        self.gambar.setGeometry(QtCore.QRect(100, 100, 300, 300))
        self.gambar.setText("")
        self.gambar.setObjectName("gambar")
        self.tombolLoad = QtWidgets.QPushButton(self.centralwidget)
        self.tombolLoad.setObjectName("tombolLoad")
        self.tombolEu = QtWidgets.QPushButton(self.centralwidget)
        self.tombolEu.setGeometry(QtCore.QRect(50, 130, 56, 17))
        self.tombolEu.setObjectName("tombolEu")
        self.tombolCos = QtWidgets.QPushButton(self.centralwidget)
        self.tombolCos.setGeometry(QtCore.QRect(60, 200, 56, 17))
        self.tombolCos.setObjectName("tombolCos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 214, 18))
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
        self.tombolLoad.setText(_translate("MainWindow", "Load"))
        self.tombolEu.setText(_translate("MainWindow", "Eucledian"))
        self.tombolCos.setText(_translate("MainWindow", "Cosine"))

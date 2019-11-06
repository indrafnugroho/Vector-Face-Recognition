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
        MainWindow.resize(735, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gambar = QtWidgets.QLabel(self.centralwidget)
        self.gambar.setGeometry(QtCore.QRect(30, 80, 300, 300))
        self.gambar.setText("")
        self.gambar.setObjectName("gambar")
        self.tombolLoad = QtWidgets.QPushButton(self.centralwidget)
        self.tombolLoad.setGeometry(QtCore.QRect(30, 450, 145, 30))
        self.tombolLoad.setObjectName("tombolLoad")
        self.tombolFind = QtWidgets.QPushButton(self.centralwidget)
        self.tombolFind.setGeometry(QtCore.QRect(180, 450, 150, 30))
        self.tombolFind.setObjectName("tombolFind")
        self.tombolEuc = QtWidgets.QRadioButton(self.centralwidget)
        self.tombolEuc.setGeometry(QtCore.QRect(30, 400, 100, 25))
        self.tombolEuc.setObjectName("tombolEuc")
        self.tombolCosi = QtWidgets.QRadioButton(self.centralwidget)
        self.tombolCosi.setGeometry(QtCore.QRect(150, 400, 100, 25))
        self.tombolCosi.setObjectName("tombolCosi")
        self.query = QtWidgets.QLabel(self.centralwidget)
        self.query.setGeometry(QtCore.QRect(30, 20, 150, 38))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(15)
        self.query.setFont(font)
        self.query.setObjectName("query")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(287, 400, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.tombolNext = QtWidgets.QPushButton(self.centralwidget)
        self.tombolNext.setGeometry(QtCore.QRect(490, 400, 60, 60))
        self.tombolNext.setText("")
        self.tombolNext.setObjectName("tombolNext")
        self.gambar2 = QtWidgets.QLabel(self.centralwidget)
        self.gambar2.setGeometry(QtCore.QRect(370, 80, 300, 300))
        self.gambar2.setText("")
        self.gambar2.setObjectName("gambar2")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(370, 20, 150, 38))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(15)
        self.result.setFont(font)
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 18))
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
        self.tombolFind.setText(_translate("MainWindow", "Find"))
        self.tombolEuc.setText(_translate("MainWindow", "Eucledian"))
        self.tombolCosi.setText(_translate("MainWindow", "Cosine"))
        self.query.setText(_translate("MainWindow", "Query"))
        self.result.setText(_translate("MainWindow", "Result"))

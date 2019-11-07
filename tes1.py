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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gambar = QtWidgets.QLabel(self.centralwidget)
        self.gambar.setGeometry(QtCore.QRect(30, 80, 300, 300))
        self.gambar.setText("")
        self.gambar.setObjectName("gambar")
        self.tombolLoad = QtWidgets.QPushButton(self.centralwidget)
        self.tombolLoad.setGeometry(QtCore.QRect(30, 500, 145, 30))
        self.tombolLoad.setObjectName("tombolLoad")
        self.tombolFind = QtWidgets.QPushButton(self.centralwidget)
        self.tombolFind.setGeometry(QtCore.QRect(180, 500, 150, 30))
        self.tombolFind.setObjectName("tombolFind")
        self.tombolEuc = QtWidgets.QRadioButton(self.centralwidget)
        self.tombolEuc.setGeometry(QtCore.QRect(30, 400, 170, 25))
        self.tombolEuc.setObjectName("tombolEuc")
        self.tombolCosi = QtWidgets.QRadioButton(self.centralwidget)
        self.tombolCosi.setGeometry(QtCore.QRect(30, 430, 150, 25))
        self.tombolCosi.setObjectName("tombolCosi")
        self.query = QtWidgets.QLabel(self.centralwidget)
        self.query.setGeometry(QtCore.QRect(30, 52, 150, 38))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(10)
        self.query.setFont(font)
        self.query.setObjectName("query")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(30, 465, 42, 22))
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
        self.result.setGeometry(QtCore.QRect(370, 52, 150, 38))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(10)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.judul = QtWidgets.QLabel(self.centralwidget)
        self.judul.setGeometry(QtCore.QRect(247, 10, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(15)
        self.judul.setFont(font)
        self.judul.setObjectName("judul")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 460, 130, 30))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 18))
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
        self.tombolEuc.setText(_translate("MainWindow", "Euclidian Distance"))
        self.tombolCosi.setText(_translate("MainWindow", "Cosine Similarity"))
        self.query.setText(_translate("MainWindow", "Query"))
        self.result.setText(_translate("MainWindow", "Result"))
        self.judul.setText(_translate("MainWindow", "Face Recognition"))
        self.label.setText(_translate("MainWindow", "Image(s)"))

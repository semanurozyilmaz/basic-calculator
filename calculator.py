# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(469, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_sayi1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sayi1.setGeometry(QtCore.QRect(30, 30, 51, 16))
        self.lbl_sayi1.setObjectName("lbl_sayi1")
        self.lbl_sayi2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sayi2.setGeometry(QtCore.QRect(30, 100, 51, 16))
        self.lbl_sayi2.setObjectName("lbl_sayi2")
        self.line_sayi1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_sayi1.setGeometry(QtCore.QRect(90, 30, 81, 20))
        self.line_sayi1.setText("")
        self.line_sayi1.setObjectName("line_sayi1")
        self.line_sayi2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_sayi2.setGeometry(QtCore.QRect(90, 100, 81, 20))
        self.line_sayi2.setObjectName("line_sayi2")
        self.btn_topla = QtWidgets.QPushButton(self.centralwidget)
        self.btn_topla.setGeometry(QtCore.QRect(20, 170, 56, 21))
        self.btn_topla.setObjectName("btn_topla")
        self.btn_cikar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikar.setGeometry(QtCore.QRect(110, 170, 56, 21))
        self.btn_cikar.setObjectName("btn_cikar")
        self.btn_carp = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carp.setGeometry(QtCore.QRect(200, 170, 56, 21))
        self.btn_carp.setObjectName("btn_carp")
        self.btn_bol = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bol.setGeometry(QtCore.QRect(290, 170, 56, 21))
        self.btn_bol.setObjectName("btn_bol")
        self.lbl_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sonuc.setGeometry(QtCore.QRect(30, 320, 331, 31))
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        self.btn_hesapla = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hesapla.setGeometry(QtCore.QRect(70, 240, 71, 31))
        self.btn_hesapla.setObjectName("btn_hesapla")
        self.btn_temizle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_temizle.setGeometry(QtCore.QRect(240, 240, 71, 31))
        self.btn_temizle.setObjectName("btn_temizle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        MainWindow.setWindowIcon(QIcon('calculator.png'))
        self.lbl_sayi1.setText(_translate("MainWindow", "Say?? 1"))
        self.lbl_sayi2.setText(_translate("MainWindow", "Say?? 2"))
        self.btn_topla.setText(_translate("MainWindow", "+"))
        self.btn_cikar.setText(_translate("MainWindow", "-"))
        self.btn_carp.setText(_translate("MainWindow", "*"))
        self.btn_bol.setText(_translate("MainWindow", "/"))
        self.lbl_sonuc.setText(_translate("MainWindow", "Sonu??:"))
        self.btn_hesapla.setText(_translate("MainWindow", "Hesapla"))
        self.btn_temizle.setText(_translate("MainWindow", "Temizle"))

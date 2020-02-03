# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gercek_calisan import *
from store import *
from satis import *
from PyQt5.QtGui import QIcon
from enter_product import *
from musteri_kayit import *
from statistic import *
from stat_screen import *

class Ui_Form1(object):
    def __init__(self,yetki=1):
        self.yetki=yetki

    def eleman_fnk(self):




        if self.yetki==1:

            self.window=QtWidgets.QDialog()
            self.ui=Ui_Dialog2()
            self.ui.setupUi2(self.window)
            self.window.setWindowIcon(QIcon('satis_icon.png'))
            self.window.setWindowTitle("Staff Member Screen")
            self.window.show()
        else:
            pass


    def ist_fnk(self):
        if self.yetki==1:


            self.window=QtWidgets.QMainWindow()
            self.ui=Window2()
            self.window.setWindowIcon(QIcon('satis_icon.png'))

            self.window.setWindowTitle("Satış Ekranı")
            self.ui.show()
        else:
            pass


    def satis_fnk(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Dialog3()
        self.ui.setupUi3(self.window)
        self.window.setWindowIcon(QIcon('satis_icon.png'))

        self.window.setWindowTitle("Satış Ekranı")
        self.window.show()
    def musteri_fnk(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Dialog4()
        self.window.setWindowIcon(QIcon('satis_icon.png'))


        self.ui.setupUi4(self.window)
        self.window.setWindowTitle("Client Screen")
        self.window.show()
    def urunkayit_fnk(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Dialog5()

        self.ui.setupUi5(self.window)
        self.window.setWindowIcon(QIcon('satis_icon.png'))

        self.window.setWindowTitle("Product Entry")
        self.window.show()
    def depo_fnk(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Dialog6()
        self.ui.setupUi6(self.window)
        self.window.setWindowIcon(QIcon('satis_icon.png'))

        self.window.setWindowTitle("Depot Screen")
        self.window.show()

    def setupUi1(self, Form):
        Form.setObjectName("Form")
        Form.resize(868, 471)
        #btn_must_kayit_2 eleman
        #btn_depo_2 satış
        #btn_urunkayit_2 istatistik
        #btn_must_kayit müsterikayit
        #btn_depo depo
        #btn_urunkayit urunkayit
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(70, 240, 681, 181))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.eleman = QtWidgets.QPushButton(self.splitter_2)
        self.eleman.setStyleSheet("background-image:url(i4.png);\n"
        "background-size:cover;\n"
        "background-repeat:no-repeat")
        Form.setStyleSheet("QWidget{background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.eleman.setText("")
        self.eleman.clicked.connect(self.eleman_fnk)
        self.eleman.setObjectName("eleman")
        self.satis = QtWidgets.QPushButton(self.splitter_2)
        self.satis.setStyleSheet("background-image:url(i5.png);\n"
        "background-size:cover;\n"
        "background-repeat:no-repeat")
        self.satis.setText("")
        self.satis.clicked.connect(self.satis_fnk)
        self.satis.setObjectName("satis")

        self.istatistik = QtWidgets.QPushButton(self.splitter_2)
        self.istatistik.setStyleSheet("background-image:url(i6.png);\n"
        "background-size:cover;\n"
        "background-repeat:no-repeat")
        self.istatistik.setText("")
        self.istatistik.setObjectName("istatistik")
        self.istatistik.clicked.connect(self.ist_fnk)
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("background-color: white;\n"
"border-style:none;\n"
"border-radius:5px;")
        self.label.setGeometry(QtCore.QRect(110, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(14)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(330, 190, 171, 31))
        self.label_2.setStyleSheet("background-color: white;\n"
"border-style:none;\n"
"border-radius:5px;")
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("background-color: white;\n"
"border-style:none;\n"
"border-radius:5px;")
        self.label_3.setGeometry(QtCore.QRect(560, 190, 161, 31))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("background-color: white;\n"
"border-style:none;\n"
"border-radius:5px;")
        self.label_4.setGeometry(QtCore.QRect(120, 430, 151, 31))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setStyleSheet("background-color: white;\n"
"border-style:none;\n"
"text-align:center;\n"                                  
"border-radius:5px;")
        self.label_5.setGeometry(QtCore.QRect(340, 430, 151, 31))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setStyleSheet("background-color: white;\n"
"border-style:none;\n"
"border-radius:5px;")
        self.label_6.setGeometry(QtCore.QRect(570, 430, 161, 31))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(70, 10, 681, 181))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btn_must_kayit = QtWidgets.QPushButton(self.splitter)
        self.btn_must_kayit.setStyleSheet("background-image:url(i1.png);\n"
        "background-size:cover;\n"
        "background-repeat:no-repeat")
        self.btn_must_kayit.setText("")
        self.btn_must_kayit.clicked.connect(self.musteri_fnk)
        self.btn_must_kayit.setObjectName("btn_must_kayit")
        self.btn_depo = QtWidgets.QPushButton(self.splitter)
        self.btn_depo.setStyleSheet("background-image:url(i2.png);\n"
        "background-size:cover;\n"
        "background-repeat:no-repeat")
        self.btn_depo.setText("")
        self.btn_depo.clicked.connect(self.depo_fnk)
        self.btn_depo.setObjectName("btn_depo")
        self.btn_urunkayit = QtWidgets.QPushButton(self.splitter)
        self.btn_urunkayit.clicked.connect(self.urunkayit_fnk)
        self.btn_urunkayit.setStyleSheet("background-image:url(i3.png);\n"
        "background-size:cover;\n"
        "background-repeat:no-repeat")
        self.btn_urunkayit.setText("")
        self.btn_urunkayit.setObjectName("btn_urunkayit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Client Registry"))
        self.label_2.setText(_translate("Form", "DepotProductEntry"))
        self.label_3.setText(_translate("Form", "Product Registry"))
        self.label_4.setText(_translate("Form", "Stuff Registry"))
        self.label_5.setText(_translate("Form", "Selling Screen"))
        self.label_6.setText(_translate("Form", "Statistics"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi1(Form)
    Form.show()
    sys.exit(app.exec_())


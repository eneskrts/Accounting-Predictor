# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urun_giris.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import db_yardim as db
from db2qt import *
class Ui_Dialog5(object):
    def kaydet(self):
        urun_adi=self.lineEdit.text()
        kategori=self.lineEdit_2.text()
        try:
            birim_fiyat=int(self.lineEdit_3.text())
        except:
            self.label_5.setText("Sayı Girin")
        query="insert into urun (fiyat,kategori,urun_adi) values(?,?,?)"
        params=[birim_fiyat,kategori,urun_adi]
        ret=db.calistir(query,param=params)
        if ret==True:
            self.lineEdit.setText(" ")
            self.lineEdit_2.setText(" ")
            self.lineEdit_3.setText(" ")
            self.label_5.setText("Başarıyla Eklendi")
        else:
            self.label_5.setText("Başarısız")
        #print(kategori)
    def setupUi5(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(476, 342)
        Dialog.setStyleSheet("QDialog{background-image:url(depo.jpg)\n"
"\n"
"\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 171, 41))
        self.label_2.setStyleSheet("color:white")
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 171, 41))
        self.label_3.setStyleSheet("color:white")
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 171, 41))
        self.label_4.setStyleSheet("color:white")
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        #####################
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 280, 211, 41))
        self.label_5.setStyleSheet("color:white")
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 110, 121, 31))
        self.lineEdit.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 160, 121, 31))
        self.lineEdit_2.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 220, 121, 31))
        self.lineEdit_3.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 100, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.kaydet)
        self.pushButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:0.613, x2:1, y2:0, stop:0 rgba(190, 120, 125, 225), stop:1 rgba(125, 225, 215, 225));\n"
"color:rgb(255, 255, 255);\n"
"border-style:none;\n"
"border-radius:5px;")
        self.pushButton.setObjectName("pushButton")
        ###################################3
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 220, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.clicked.connect(self.goster)
        self.pushButton_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:0.613, x2:1, y2:0, stop:0 rgba(190, 110, 125, 125), stop:1 rgba(155, 255, 255, 255));\n"
"color:rgb(255, 255, 255);\n"
"border-style:none;color:white;\n"
"border-radius:5px;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def goster(self):
         query="select urun_id,urun_adi,kategori,fiyat from urun"
         self.window=QtWidgets.QDialog()
         col_names=['Ürün ID','Ürün Adı','Kategori','Fiyat']
         sil_q="delete from urun where urun_id=?"

         self.ui=Ui_Dialog9(query,col_names,sil_q)
         self.ui.setupUi9(self.window)
         self.window.show()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Product Register"))
        self.label_2.setText(_translate("Dialog", "Name:"))
        self.label_3.setText(_translate("Dialog", "Category:"))
        self.label_4.setText(_translate("Dialog", "Price:"))
        self.label_5.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Show"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog5()


    ui.setupUi5(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


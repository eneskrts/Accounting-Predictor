# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'satis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import db_yardim as db
import time
from db2qt import *
class Ui_Dialog3(object):
    def kaydet(self):
        print("hello")

        try:

            must_id=int(self.lineEdit_3.text())
            urun_id=int(self.lineEdit.text())
            adet=int(self.lineEdit_2.text())



            q11="select fiyat from urun where urun_id=?"
            param=[urun_id]
            i=db.sorgu(q11,param=param)
            fiyat=i[0][0]
            kazanc=fiyat*adet
            ay=int(time.localtime().tm_mon)
            yil=int(time.localtime().tm_year)
            q2="insert into satislar (adet,kazanc,musteri_id,urun_no,ay,yil) values(?,?,?,?,?,?)"
            param2=[adet,kazanc,must_id,urun_id,ay,yil]
            ret2=db.calistir(q2,param2)
            if ret2==True:
                self.label_5.setText("Başarılı")
                self.lineEdit.setText(" ")
                self.lineEdit_3.setText(" ")
                self.lineEdit_2.setText(" ")
            else:
                self.label_5.setText("Veritabanına Eklenemedi")


        except:
            self.label_5.setText("Bir sorun olustu")

            #if len(res1)<=0:
             #   self.label_5.setText("Ürün Bulunamadı")
            #print([must_id,urun_id,adet])
           # else:
            #    self.label_5.setText("Bulundu")





    def setupUi3(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(656, 472)
        Dialog.setStyleSheet("QDialog{background-image:url(depo.jpg)\n"
"\n"
"\n"
"}")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 110, 111, 31))
        self.lineEdit.setStyleSheet("border-style:none;\n"
"border-radius:5px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 180, 111, 31))
        self.lineEdit_2.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white")
        self.label_4.setObjectName("label_4")
        #240, 240, 141, 51
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(399, 240, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 40, 111, 31))
        self.lineEdit_3.setStyleSheet("border-style:none;\n"
"border-radius:5px;\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.clicked.connect(self.kaydet)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 240, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-style:none;\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0.965174, y1:1, x2:1, y2:0, stop:0 rgba(0, 98, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color:white\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(self.goster)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 240, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-style:none;\n"
"border-radius:5px;\n"
"background-color:qlineargradient(spread:pad, x1:0.965174, y1:1, x2:1, y2:0, stop:0 rgba(85, 0, 127, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color:white")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def goster(self):
         query="select * from satislar"
         self.window=QtWidgets.QDialog()
         col_names=['Satış ID','Adet','Kazanç','Musteri ID','Urun ID','Ay','Yıl']
         sil_q="delete from satislar where satis_id=?"
         self.ui=Ui_Dialog9(query,col_names,sil_q)
         self.ui.setupUi9(self.window)
         self.window.show()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Product ID"))
        self.label_3.setText(_translate("Dialog", "Number"))
        self.label_4.setText(_translate("Dialog", "Client ID"))
        self.label_5.setText(_translate("Dialog", ""))
        self.pushButton_4.setText(_translate("Dialog", "Save"))
        self.pushButton_3.setText(_translate("Dialog", "All Sales"))

#import a_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi3(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


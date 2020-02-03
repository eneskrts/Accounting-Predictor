# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'depo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import  db_yardim as db
from db2qt import *
class Ui_Dialog6(object):
    def kaydet(self):
        try:

            id=int(self.lineEdit.text())
            adet=int(self.lineEdit_2.text())
            query="insert into depo (adet,urn_id) values(?,?)"
            param=[adet,id]
            sonuc=db.calistir(query,param=param)
            if sonuc==True:
                self.label_4.setText("Başarıyla Eklendi")
            else:
                self.label_4.setText("Bir Sorun oldu")
        except:
            self.label_4.setText("Bir sorun oldu")
    def goster(self):
         query="select depo_id,urun.urun_adi,adet,urun.fiyat,urun.kategori from urun,depo where urun.urun_id=depo.urn_id"
         self.window=QtWidgets.QDialog()
         col_names=['DepoNo','Ürün Adı','Adet','Fiyat','Kategori']
         sil_q="delete from depo where depo_id=?"
         self.ui=Ui_Dialog9(query,col_names,sil_q)
         self.ui.setupUi9(self.window)
         self.window.show()



    def setupUi6(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("QDialog{background-image:url(depo.jpg)\n"
"\n"
"\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(120, 180, 219, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white")
        self.label_4.setObjectName("label_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 111, 31))
        self.lineEdit.setStyleSheet("border-style:none;\n"
"border-radius:5px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 150, 111, 31))
        self.lineEdit_2.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 220, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.kaydet)
        self.pushButton.setStyleSheet("border-style:none;\n"
"border-radius:5px;\n"
"background-color:qlineargradient(spread:pad, x1:0.965174, y1:1, x2:1, y2:0, stop:0 rgba(0, 94, 138, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color:white")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.goster)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 220, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-style:none;\n"
"border-radius:5px;\n"
"background-color:qlineargradient(spread:pad, x1:0.99005, y1:0.528, x2:1, y2:0, stop:0.318408 rgba(255, 170, 127, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color:white")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Product Entry"))
        self.label_2.setText(_translate("Dialog", "Product ID"))
        self.label_3.setText(_translate("Dialog", "Number"))
        self.label_4.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "All Products"))

#import a_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog6()
    ui.setupUi6(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


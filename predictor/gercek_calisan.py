# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gercek_calisan.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import db_yardim as db
from db2qt import *
class Ui_Dialog2(object):


    def goruntule(self):
         query="select * from calisan"
         self.window=QtWidgets.QDialog()
         col_names=['Calısan ID','İsim','Soyisim','Doğum Tarihi','Adres','Telefon','Maaş']
         sil_q="delete from calisan where calisan_id=?"
         self.ui=Ui_Dialog9(query,col_names,sil_q)
         self.ui.setupUi9(self.window)
         self.window.show()

    def kaydet(self):
        isim=self.lineEdit.text()
        soy=self.lineEdit_2.text()
        dtarih=self.lineEdit_3.text()
        tel=self.lineEdit_4.text()
        try:
                maas=int(self.lineEdit_5.text())
        except:
                pass
        adres=self.textEdit.toPlainText()
        query="insert into calisan (isim,soyisim,dogum_tarih,adres,telefon,maas) values(?,?,?,?,?,?)"
        params=[isim,soy,dtarih,adres,tel,maas]
        ret=db.calistir(query,params)
        if ret==True:
                self.label_8.setText("Succesfull")
        else:
                self.label_8.setText("Problem Occured")

        print([isim,soy,dtarih,tel,maas,adres])





    def setupUi2(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(601, 631)
        Dialog.setStyleSheet("QDialog{background-image:url(depo.jpg)\n"
"\n"
"\n"
"}")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 80, 171, 31))
        self.lineEdit.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 232, 47))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color:white;\n")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 232, 47))
        self.label_2.setStyleSheet("color:white;\n")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 140, 171, 31))
        self.lineEdit_2.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 232, 47))
        self.label_3.setStyleSheet("color:white;\n")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 210, 171, 31))
        self.lineEdit_3.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("color:white;\n")
        self.label_4.setGeometry(QtCore.QRect(10, 280, 232, 47))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 290, 171, 31))
        self.lineEdit_4.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setStyleSheet("color:white;\n")
        self.label_5.setGeometry(QtCore.QRect(10, 360, 232, 47))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 370, 171, 31))
        self.lineEdit_5.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 440, 232, 47))
        self.label_6.setStyleSheet("color:white;\n")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(110, 440, 171, 87))
        self.textEdit.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.textEdit.setObjectName("textEdit")

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(370, 90, 171, 41))
        self.label_7.setStyleSheet("color:white;\n")
        font = QtGui.QFont()
        font.setFamily("Dubai Light")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: white;\n"
"background-color: rgb(170, 85, 255);\n"
"border-style:none;\n"
"border-radius:5px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(100, 588, 241, 51))
        self.label_8.setStyleSheet("color:white;font-weight:bold;\n")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 230, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.clicked.connect(self.goruntule)
        self.pushButton_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:0.613, x2:1, y2:0, stop:0 rgba(170, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border-radius:5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(self.kaydet)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 550, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:0.613, x2:1, y2:0, stop:0 rgba(170, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-style:none;\n"
"border-radius:5px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(90, 10, 411, 51))
        self.label_9.setStyleSheet("color:white;\n")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.label_2.setText(_translate("Dialog", "Surname"))
        self.label_3.setText(_translate("Dialog", "B.Date"))
        self.label_4.setText(_translate("Dialog", "Phone"))
        self.label_5.setText(_translate("Dialog", "Salary"))
        self.label_6.setText(_translate("Dialog", "Adress"))
        self.label_7.setText(_translate("Dialog", "All Clients"))
        self.label_8.setText(_translate("Dialog", ""))
        self.pushButton_2.setText(_translate("Dialog", "ShowAll"))
        self.pushButton_3.setText(_translate("Dialog", "Save"))
        self.label_9.setText(_translate("Dialog", "Stuff Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi2(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


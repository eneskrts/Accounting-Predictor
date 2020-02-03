# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musteri_kayit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import  sqlite3
from db2qt import *
class Ui_Dialog4(object):
    def all_client(self):

        query="select * from musteri"

        self.window=QtWidgets.QDialog()
        col_names=['MüsteriNo','İsim','Soyisim','Adres','Şirket','Telefon']
        sil_q="delete from musteri where must_id=?"
        self.ui=Ui_Dialog9(query,col_names,sil_q)
        self.ui.setupUi9(self.window)
        self.window.show()





    def setupUi4(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(799, 448)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        Dialog.setFont(font)
        Dialog.setStyleSheet("QDialog{background-image:url(depo.jpg)\n"
"\n"
"\n"
"}")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 10, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 80, 232, 47))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 232, 47))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 150, 171, 31))
        self.lineEdit_2.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 90, 171, 31))
        self.lineEdit.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 380, 232, 47))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white")
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 220, 171, 31))
        self.lineEdit_4.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(130, 360, 171, 87))
        self.textEdit.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 232, 47))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white")
        self.label_4.setObjectName("label_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 280, 171, 31))
        self.lineEdit_6.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 280, 232, 47))
        self.label_msg = QtWidgets.QLabel(Dialog)
        self.label_msg.setGeometry(QtCore.QRect(460,270,400,130))
        self.label_msg.setFont(font)
        self.label_msg.setStyleSheet("color:white")
        self.label_msg.setObjectName("label_msg")
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(320, 160, 232, 47))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 170, 171, 31))
        self.lineEdit_3.setStyleSheet("border-style:none;\n"
"border-radius:5px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.sorgu)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 240, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.613, x2:1, y2:0, stop:0 rgba(141, 141, 141, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border-radius:5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(370, 90, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(self.must_kaydet)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 370, 111, 61))
        self.pushButton_all_client = QtWidgets.QPushButton(Dialog)
        self.pushButton_all_client.clicked.connect(self.all_client)
        self.pushButton_all_client.setGeometry(QtCore.QRect(599, 370, 147, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(14)
        self.pushButton_all_client.setFont(font)
        self.pushButton_all_client.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.613, x2:1, y2:0, stop:0 rgba(141, 141, 141, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border-radius:5px;")
        self.pushButton_all_client.setObjectName("pushButton_all_client")
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.613, x2:1, y2:0, stop:0 rgba(141, 141, 141, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border-radius:5px;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def must_kaydet(self):
        #isim,soyisim,tel ,şirket,adres
        isim=self.lineEdit.text()
        soyisim=self.lineEdit_2.text()
        tel=self.lineEdit_4.text()
        sirket=self.lineEdit_6.text()
        adres=self.textEdit.toPlainText()



        vt=sqlite3.connect('db_1.db')
        im=vt.cursor()

        #print([isim,soyisim,tel,sirket,adres])
        query="""insert into musteri(isim,soyisim,tel,adres,sirket) values(?,?,?,?,?)"""

        try:
            im.execute(query,(isim,soyisim,tel,adres,sirket))
            vt.commit()
            self.label_msg.setText("Başarıyla Eklendi")
            self.lineEdit.setText(" ")
            self.lineEdit_2.setText(" ")
            self.lineEdit_4.setText(" ")

            self.lineEdit_6.setText(" ")
            self.textEdit.setPlainText(" ")
        except:
            self.label_msg.setText("Bir Sorun Oluştu")
    def sorgu(self):
        try:

            id=int(self.lineEdit_3.text())
            #print(id)
            q="select isim,soyisim,tel,sirket,adres from musteri where must_id= ?"
            con=sqlite3.connect('db_1.db')
            im=con.cursor()
            im.execute(q,[id])
            res=im.fetchall()


            isim=res[0][0]
            soy=res[0][1]
            tel=res[0][2]
            sirket=res[0][3]
            adres=res[0][4]
            self.lineEdit.setText(isim)
            self.lineEdit_2.setText(soy)
            self.lineEdit_4.setText(tel)
            self.lineEdit_6.setText(sirket)
            self.textEdit.setPlainText(adres)
                #print(res[0])
            con.close()

        except:
            pass
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_9.setText(_translate("Dialog", "Client Registry"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Surname"))
        self.label_6.setText(_translate("Dialog", "Adress"))
        self.label_4.setText(_translate("Dialog", "PhoneNo"))
        self.label_7.setText(_translate("Dialog", "Company"))
        self.label_3.setText(_translate("Dialog", "Client No"))
        self.pushButton_2.setText(_translate("Dialog", "Check"))
        self.label_5.setText(_translate("Dialog", "Client Check"))
        self.label_msg.setText(_translate("Dialog", ""))
        self.pushButton_all_client.setText(_translate("Dialog", "All Clients"))
        self.pushButton_3.setText(_translate("Dialog", "Save"))

#import a_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog4()
    ui.setupUi4(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_son.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import db_yardim
from homepage import*
class Ui_Dialog(object):


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(535, 336)

        Dialog.setStyleSheet("QDialog{background-image:url(depo.jpg)\n"
"\n"
"\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("")
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(20, 50, 20, 30)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.qwidged_beyaz = QtWidgets.QWidget(self.frame)
        self.qwidged_beyaz.setStyleSheet("formFrame{\n"
"background-color:white;\n"
"}\n"
"\n"
"")
        self.qwidged_beyaz.setObjectName("qwidged_beyaz")
        self.formLayout = QtWidgets.QFormLayout(self.qwidged_beyaz)
        self.formLayout.setContentsMargins(-1, -1, -1, 30)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.qwidged_beyaz)
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setObjectName("label_3")
        self.label_3.move(100,100)


        self.label = QtWidgets.QLabel(self.qwidged_beyaz)
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(14)
        self.label.setFont(font)
        
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.qwidged_beyaz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border-radius:3px;\n"
"  border-color: black;\n"
"\n"
"background-color:white;\n"
"font: italic 12pt \"Sitka Text\";}")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.qwidged_beyaz)
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setObjectName("label_2")
        self.label_3.setGeometry(100,100,150,40)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.qwidged_beyaz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border-radius:3px;\n"
"background-color:white;\n"
"font: italic 12pt \"Sitka Text\";}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.gridLayout.addWidget(self.qwidged_beyaz, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.995, y1:0.585, x2:1, y2:0, stop:0 rgba(0, 255, 127, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"background-color: #944dff;\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  cursor: pointer;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.lgn)
        self.gridLayout_3.addWidget(self.pushButton, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 2, 1, 1)
        #self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        #self.pushButton_2.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(12)
        #self.pushButton_2.setFont(font)
       # self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"

        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def msgbox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
    def lgn(self):
        #vt,im=self.sql_con()
        import sqlite3 as sq
        from PyQt5.QtWidgets import QMessageBox
        import sys

        from PyQt5.QtWidgets import QMessageBox


        self.user=self.lineEdit.text()
        self.password=self.lineEdit_2.text()
        self.vt=sq.connect('db_1.db')
        self.im=self.vt.cursor()
        self.query="select user_id from users where username= ? and password= ?"
        self.im.execute(self.query,(self.user,self.password))
        self.veriler=self.im.fetchall()
        if len(self.veriler)>0:
                self.label_3.setText("Giriş Başarılı")
                self.vt.close()
        #im.execute(query)
                self.window=QtWidgets.QWidget()
                self.yetki()
                self.ui=Ui_Form1(self.yetki_no)

                self.ui.setupUi1(self.window)
                self.window.setWindowTitle("Homepage")
                self.window.setWindowIcon(QIcon('homepage_icon.jpg'))

                self.window.show()
        else:
                self.label_3.setStyleSheet("color:red;font-weight: bold;")
                self.label_3.setText("Hatalı Giriş")
                self.lineEdit_2.setText(" ")
                self.lineEdit.setText(" ")
                self.vt.close()






    def yetki(self):
        q="select yetki from users where username=? and password=?"
        params=[self.user,self.password]
        res=db_yardim.sorgu(q,param=params)
        if res[0][0]!=1:
            self.yetki_no=0
        else:
            self.yetki_no=1

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Username:"))
        self.label_2.setText(_translate("Dialog", "Password:"))
        self.label_3.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "Login"))
        #self.pushButton.clicked.connect(self.lgn)
        #self.pushButton_2.setText(_translate("Dialog", "Forgot Password?"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("Login")
    Dialog.setWindowIcon(QIcon('login_icon.png'))
    Dialog.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grid.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem

#from QTableWidget import QTableWidgetItem
import sqlite3
class Ui_Dialog9(object):
    def __init__(self,query="",col_names=[],sil_q=""):
        self.query=query
        self.col_names=col_names
        self.sil_q=sil_q



    def setupUi9(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(603, 390)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 340, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 350, 113, 21))
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.tikla)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 330, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.sil)
        self.pushButton.setGeometry(QtCore.QRect(340, 330, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(5, 1, 601, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ID:"))
        self.pushButton.setText(_translate("Dialog", "Delete"))
        self.pushButton_2.setText(_translate("Dialog", "Show"))

    def table_doldur(self):
        try:
             while self.tableWidget.rowCount()>0:
                 self.tableWidget.removeRow(0)
             con=sqlite3.connect('db_1.db')
             im=con.cursor()
             im.execute(self.query)
             res=im.fetchall()
             #print(res)
             self.tableWidget.setColumnCount(len(res[0]))
             self.tableWidget.setHorizontalHeaderLabels(self.col_names)

             for rc,user in enumerate(res):
                self.tableWidget.insertRow(rc)
                for col,data in enumerate(user):
                 cell=QTableWidgetItem(str(data))
                 self.tableWidget.setItem(rc,col,cell)

             con.close()
        except:
            pass
    def tikla(self):
        self.table_doldur()
    def sil(self):
        try:

            id=int(self.lineEdit.text())

            #="delete from musteri where must_id=? "
            con=sqlite3.connect('db_1.db')

            con.execute(self.sil_q,[id])
            con.commit()
            self.table_doldur()
        except:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog9()
    ui.setupUi9(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


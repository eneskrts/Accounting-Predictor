# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'istatistik.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import predict

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Canvas(FigureCanvas):
    def plot(self):
        import numpy as np
        x = np.array([50, 30,40])
        labels = ["Apples", "Bananas", "Melons"]
        ax = self.figure.add_subplot(111)
        ax.pie(x, labels=labels)

    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)

        self.plot()





class Ui_Dialog7(object):
        def tahmin(self):
            pass

        def setupUi7(self, Dialog):
            Dialog.setObjectName("Dialog")
            Dialog.resize(723, 526)
            self.label = QtWidgets.QLabel(Dialog)
            self.label.setGeometry(QtCore.QRect(30, 410, 161, 51))
            font = QtGui.QFont()
            font.setFamily("Yu Gothic Light")
            font.setPointSize(12)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.lineEdit = QtWidgets.QLineEdit(Dialog)
            self.lineEdit.setGeometry(QtCore.QRect(140, 420, 121, 31))
            self.lineEdit.setObjectName("lineEdit")
            self.label_b = QtWidgets.QLabel(Dialog)
            self.label_b.setGeometry(QtCore.QRect(30,460, 310, 151))
            font = QtGui.QFont()
            font.setFamily("Yu Gothic Light")
            font.setPointSize(16)
            self.label_b.setFont(font)
            self.label_b.setObjectName("label")
            self.pushButton = QtWidgets.QPushButton(Dialog)
            self.pushButton.clicked.connect(self.tikla)
            self.pushButton.setGeometry(QtCore.QRect(330, 410, 111, 51))
            font = QtGui.QFont()
            font.setFamily("Yu Gothic UI Light")
            font.setPointSize(12)

            self.pushButton.setFont(font)


            self.pushButton.setStyleSheet("border-style:none;\n"
    "border-radius:5px;\n"
    "background-color:qlineargradient(spread:pad, x1:0.965174, y1:1, x2:1, y2:0, stop:0 rgba(0, 94, 138, 255), stop:1 rgba(255, 255, 255, 255));\n"
    "color:white")
            self.pushButton.setObjectName("pushButton")
            self.pushButton.clicked.connect(self.tahmin)
            self.label_2 = QtWidgets.QLabel(Dialog)
            self.label_2.setGeometry(QtCore.QRect(450, 410, 220, 51))
            font = QtGui.QFont()
            font.setFamily("Yu Gothic Light")
            font.setPointSize(18)
            self.label_2.setFont(font)
            self.label_2.setObjectName("label_2")

            self.retranslateUi(Dialog)
            QtCore.QMetaObject.connectSlotsByName(Dialog)
            canvas = Canvas(self, width=8, height=4)
            canvas.move(0,0)


        def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
            self.label.setText(_translate("Dialog", "Ay Girin"))

            self.pushButton.setText(_translate("Dialog", "Tahmin Et"))
            self.label_2.setText(_translate("Dialog", "Tahmin: -"))
            self.label_b.setText(_translate("Dialog", "Başarım: -"))
        def tikla(self):
            try:
                ay_no=int(self.lineEdit.text())
                tahmn=predict.tahmin_et(ay=ay_no)
                basarim=predict.yazdir()
                print(basarim)
                print(tahmn)
                self.label_b.setText("Başarım:%{}".format(round(basarim,4)))
                self.label_2.setText("Tahmin:{}₺".format(round(tahmn,2)))
                #ax = self.figure.add_subplot(111)
                #mon,sat,pred=tahminet.ciz()


            except:
                self.label_b.setText("Bir Problem Oluştu!")





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog7()
    ui.setupUi7(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QLabel,QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot
import numpy as np
 
import predict
 
class Window2(QMainWindow):
    def tikla(self):
        try:
            ay_no=int(self.line_edit1.text())
            tahmn=predict.tahmin_et(ay=ay_no)
            basarim=predict.yazdir()
            print(basarim)
            print(tahmn)
            self.label_2.setText("R Score:%{}".format(round(basarim,4)))
            self.label_3.setText("Predict:{}$".format(round(tahmn,2)))
        except:
            self.label_2.setText("Problem Occured")
    def __init__(self):
        super().__init__()
 
        title = "Sale Prediction"
        top = 400
        left = 400
        width = 900
        height = 500
 
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon('stat.ico'))
        self.setGeometry(top, left, width, height)
 
        self.MyUI(self.window())
 
 
    def MyUI(self,Dialog):
        #Dialog.resize(601, 631)

 
        canvas = Canvas(self, width=8, height=4)
        canvas.move(0,0)
        label_1=QLabel(text="Month:",parent=Dialog)
        label_1.move(100,450)
        self.line_edit1=QLineEdit(Dialog)
        self.line_edit1.move(200,450)
        self.label_2=QLabel(text="Prediction:",parent=Dialog)
       #self.label_2.move(500,450)
        self.label_2.setGeometry(500,450,200,40)
        #self.label_2.width(200,40)
        self.label_3=QLabel(text="Success:%:",parent=Dialog)
        self.label_3.move(700,450)
        self.button = QPushButton("Predict", Dialog)
        self.button.clicked.connect(self.tikla)
        self.button.move(350, 450)
 

 
 
class Canvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot()
 
 
    def plot(self):
        ay,kazanc,tahmn=predict.ciz()
        ax=self.figure.add_subplot(111)
        ax.xlabel=['January','February','March','April','May','June','July','August']
        ax.scatter(ay,kazanc)
        ax.set_xlabel('Months')
        ax.set_ylabel('Sales')
        ax.set_title("Sales Chart by Month")
        ax.plot(ay,tahmn,color='red')


 
 
 
if __name__=='__main__':


    app = QApplication(sys.argv)
    window = Window2()
    window.show()
    app.exec()

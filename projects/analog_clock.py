#!/usr/bin/python

####################
# name: Victoria
#file: analog_clock.py
#date: 6/6/2022
######################

from PyQt5.QtWidgets import *
from PyQt5 import QtCore , QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class clock(QMainWindow):
    def__init__(self):
        super().__init__()
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)
        self.setWindowTitle('Analog_clock')
        self.setGeometry(300, 300, 400, 400)
        self.setStyleSheet("background: black")
        self.hPointer = QtGui.QPolygon([QPoint(6,7),
                                        QPoint(-6,7),
                                        QPoint(0,-50)])# CREATING THE HOUR HAND
        self.mpointer = QPolygon([QPoint(6,7),
                                  QPoint(-6,7),
                                  QPoint(0,-70)]) #CREATING THE MINUTE HAND
        self.spointer = QPolygon([QPoint(1,1),
                                  QPoint(-1,1),
                                  QPoint(0,-90)])#CREATING THE SECOND HAND
        self.bColor = Qt.blue # minute and hour hand colors
        self.sColor = Qt.yellow #second hand color
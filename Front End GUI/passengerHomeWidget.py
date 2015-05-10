# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passengerhomewidget.ui'
#
# Created: Sat May 09 19:45:36 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui

class passengerHomeWidget(QtGui.QWidget):
    myTrips_signal = QtCore.Signal()
    trainSched_signal = QtCore.Signal()
    checkIn_signal = QtCore.Signal()
    purchaseTickets_signal = QtCore.Signal()
    
    def __init__(self):
        super(passengerHomeWidget, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'passengerHomeWidgets'
        self.name = ''
        self.description = ''
        self.createLabels()
    
    def createLabels(self):
        self.setObjectName("passengerHomeWidget")
        self.resize(500,300)
    
        self.passengerHomeLabel = QtGui.QLabel(self)
        self.passengerHomeLabel.setGeometry(QtCore.QRect(180, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passengerHomeLabel.setFont(font)
        self.passengerHomeLabel.setObjectName(("passengerHomeLabel"))
        
        self.myTrips_button = QtGui.QPushButton(self)
        self.myTrips_button.setGeometry(QtCore.QRect(200, 100, 101, 41))
        self.myTrips_button.setObjectName(("myTrips_button"))
        self.myTrips_button.clicked.connect(self.myTripsScreen)
        
        self.trainSched_button = QtGui.QPushButton(self)
        self.trainSched_button.setGeometry(QtCore.QRect(200, 140, 101, 41))
        self.trainSched_button.setObjectName(("trainSched_button"))
        self.trainSched_button.clicked.connect(self.trainSchedScreen)
        
        self.checkIn_button = QtGui.QPushButton(self)
        self.checkIn_button.setGeometry(QtCore.QRect(200, 180, 101, 41))
        self.checkIn_button.setObjectName(("checkIn_button"))
        self.checkIn_button.clicked.connect(self.checkInScreen)
        
        self.purchaseTickets_button = QtGui.QPushButton(self)
        self.purchaseTickets_button.setGeometry(QtCore.QRect(200, 220, 101, 41))
        self.purchaseTickets_button.setObjectName(("purchaseTickets_button"))
        self.purchaseTickets_button.clicked.connect(self.purchaseTicketsScreen)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.passengerHomeLabel.setText(QtGui.QApplication.translate("Form", "Passenger Home", None, QtGui.QApplication.UnicodeUTF8))
        self.myTrips_button.setText(QtGui.QApplication.translate("Form", "My Trips", None, QtGui.QApplication.UnicodeUTF8))
        self.trainSched_button.setText(QtGui.QApplication.translate("Form", "Train Schedule", None, QtGui.QApplication.UnicodeUTF8))
        self.checkIn_button.setText(QtGui.QApplication.translate("Form", "Check In", None, QtGui.QApplication.UnicodeUTF8))
        self.purchaseTickets_button.setText(QtGui.QApplication.translate("Form", "Purchase Tickets", None, QtGui.QApplication.UnicodeUTF8))

    def myTripsScreen(self):
        print "Transitioning to myTripsScreen"
        
    def trainSchedScreen(self):
        print "Transitioning to trainSchedScreen"
    
    def checkInScreen(self):
        print "Transitioning to checkInScreen"
    
    def purchaseTicketsScreen(self):
        print "Transitioning to purchaseTicketsScreen"


def main():
    app = QtGui.QApplication(sys.argv)
    ex = passengerHomeWidget()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

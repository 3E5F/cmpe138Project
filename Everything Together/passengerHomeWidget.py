# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passengerhomewidget.ui'
#
# Created: Sat May 09 19:45:36 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui
from passenger_home import *
from passenger_checkin import *

class passengerHomeWidget(QtGui.QWidget):
    myTrips_signal = QtCore.Signal()
    trainSched_signal = QtCore.Signal()
    checkIn_signal = QtCore.Signal()
    purchaseTickets_signal = QtCore.Signal()
    
    goBack = QtCore.Signal()
    
    def __init__(self, current_user_id):
        super(passengerHomeWidget, self).__init__()
        self.current_user_id = current_user_id
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'passengerHomeWidgets'
        ph=passenger_home()
        ph.check_login(self.current_user_id)
        pc=passenger_checkin(ph.cache_passenger)
        self.p_name=pc.get_passenger_name()
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
        
        self.PassengerNameField = QtGui.QTextEdit(self)
        self.PassengerNameField.setGeometry(QtCore.QRect(140, 60, 211, 31))
        self.PassengerNameField.setAcceptDrops(True)
        self.PassengerNameField.setObjectName(("PassengerNameField"))
        self.PassengerNameField.setReadOnly(True)
        self.PassengerNameField.setText(self.p_name)
        
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

        self.backButton = QtGui.QPushButton(self)
        self.backButton.setGeometry(QtCore.QRect(20, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backButton.setFont(font)
        self.backButton.setObjectName(("backButton"))
        self.backButton.clicked.connect(self.goBackOneScreen)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.passengerHomeLabel.setText(QtGui.QApplication.translate("Form", "Passenger Home", None, QtGui.QApplication.UnicodeUTF8))
        self.myTrips_button.setText(QtGui.QApplication.translate("Form", "My Trip", None, QtGui.QApplication.UnicodeUTF8))
        self.trainSched_button.setText(QtGui.QApplication.translate("Form", "Train Schedule", None, QtGui.QApplication.UnicodeUTF8))
        self.checkIn_button.setText(QtGui.QApplication.translate("Form", "Check In", None, QtGui.QApplication.UnicodeUTF8))
        self.purchaseTickets_button.setText(QtGui.QApplication.translate("Form", "Purchase Tickets", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("Form", "<- Go Back", None, QtGui.QApplication.UnicodeUTF8))

    def myTripsScreen(self):
        print "Transitioning to myTripsScreen"
        self.myTrips_signal.emit()
        
    def trainSchedScreen(self):
        print "Transitioning to trainSchedScreen"
        self.trainSched_signal.emit()
        
    def checkInScreen(self):
        print "Transitioning to checkInScreen"
        self.checkIn_signal.emit()
    
    def purchaseTicketsScreen(self):
        print "Transitioning to purchaseTicketsScreen"
        self.purchaseTickets_signal.emit()
    
    def goBackOneScreen(self):
        print "Going Back one screen"
        self.goBack.emit()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = passengerHomeWidget()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

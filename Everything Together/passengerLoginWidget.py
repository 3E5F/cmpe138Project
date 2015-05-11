# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passengerlogin.ui'
#
# Created: Sat May 09 18:49:08 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui
from passenger_home import *
from passenger_checkin import *
from loggerModule import *

class passengerLoginWidget(QtGui.QWidget):
    submitRequest = QtCore.Signal()
    goBack = QtCore.Signal()
    
    def __init__(self):
        super(passengerLoginWidget, self).__init__()
        self.current_user_id = None
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'passengerLoginWidget'
        self.name = ''
        self.description = ''
        self.createLabels()
    
    def createLabels(self):
        self.setObjectName("passengerLoginWidget")
        self.resize(500,380)
    
        self.passengerLoginLabel = QtGui.QLabel(self)
        self.passengerLoginLabel.setGeometry(QtCore.QRect(180, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passengerLoginLabel.setFont(font)
        self.passengerLoginLabel.setObjectName(("passengerLoginLabel"))
        
        self.enterPassengerIDLabel = QtGui.QLabel(self)
        self.enterPassengerIDLabel.setGeometry(QtCore.QRect(180, 80, 141, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enterPassengerIDLabel.setFont(font)
        self.enterPassengerIDLabel.setObjectName(("enterPassengerIDLabel"))
        
        self.passengerID_input = QtGui.QLineEdit(self)
        self.passengerID_input.setGeometry(QtCore.QRect(170, 100, 158, 31))
        self.passengerID_input.setObjectName(("passengerID_input"))
        
        self.passengerPasswordLabel = QtGui.QLabel(self)
        self.passengerPasswordLabel.setGeometry(QtCore.QRect(210, 150, 71, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passengerPasswordLabel.setFont(font)
        self.passengerPasswordLabel.setObjectName(("passengerPasswordLabel"))
        
        self.passengerPassword_input = QtGui.QLineEdit(self)
        self.passengerPassword_input.setGeometry(QtCore.QRect(170, 180, 158, 31))
        self.passengerPassword_input.setObjectName(("passengerPassword_input"))
        
        self.submitButton = QtGui.QPushButton(self)
        self.submitButton.setGeometry(QtCore.QRect(210, 230, 81, 31))
        self.submitButton.setObjectName(("submitButton"))
        self.submitButton.clicked.connect(self.submitButtonClicked)
        
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
        self.passengerLoginLabel.setText(QtGui.QApplication.translate("Form", "Passenger Login", None, QtGui.QApplication.UnicodeUTF8))
        self.enterPassengerIDLabel.setText(QtGui.QApplication.translate("Form", "Enter Passenger ID", None, QtGui.QApplication.UnicodeUTF8))
        self.passengerPasswordLabel.setText(QtGui.QApplication.translate("Form", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setText(QtGui.QApplication.translate("Form", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("Form", "<- Go Back", None, QtGui.QApplication.UnicodeUTF8))
    
    def submitButtonClicked(self):
        #submit button is clicked
        #Checking if value is valid
        self.passengerID = self.passengerID_input.text()
        logAttempt = 'Trying ID: ' + str(self.passengerID)
        loggerModule(logAttempt)
        print self.passengerID
        ph = passenger_home()
        ph.check_login(self.passengerID)
        
        
        if ph.get_login(): #Checks if the passengerID is valid
            #pc = passenger_checkin(ph.cache_passenger)
            loggerModule('Succeeded')
            self.current_user_id = self.passengerID
            self.passengerHomeScreen()
        else:
            loggerModule('Failed')
            print "Not a valid Passenger ID"
    
    def goBackOneScreen(self):
        print "Going Back one screen"
        self.goBack.emit()
    
    def passengerHomeScreen(self):
        print "Transitioninig to passenger home screen"
        self.submitRequest.emit()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = passengerLoginWidget()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

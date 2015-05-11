# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passengerlogin.ui'
#
# Created: Sat May 09 18:49:08 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui
from conductor_home import *
from loggerModule import *

class conductorLoginWidget(QtGui.QWidget):
    submitRequest = QtCore.Signal()
    goBack = QtCore.Signal()
    
    def __init__(self):
        super(conductorLoginWidget, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'mainMenu'
        self.name = ''
        self.description = ''
        self.createLabels()
    
    def createLabels(self):
        self.setObjectName("conductorLoginWidget")
        self.resize(500,380)
    
        self.conductorLoginLabel = QtGui.QLabel(self)
        self.conductorLoginLabel.setGeometry(QtCore.QRect(180, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.conductorLoginLabel.setFont(font)
        self.conductorLoginLabel.setObjectName(("conductorLoginLabel"))
        
        self.enterConductorIDLabel = QtGui.QLabel(self)
        self.enterConductorIDLabel.setGeometry(QtCore.QRect(180, 80, 141, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enterConductorIDLabel.setFont(font)
        self.enterConductorIDLabel.setObjectName(("enterConductorIDLabel"))
        
        self.conductorID_input = QtGui.QLineEdit(self)
        self.conductorID_input.setGeometry(QtCore.QRect(170, 100, 158, 31))
        self.conductorID_input.setObjectName(("conductorID_input"))
        
        self.conductorPasswordLabel = QtGui.QLabel(self)
        self.conductorPasswordLabel.setGeometry(QtCore.QRect(210, 150, 71, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.conductorPasswordLabel.setFont(font)
        self.conductorPasswordLabel.setObjectName(("conductorPasswordLabel"))
        
        self.conductorPassword_input = QtGui.QTextEdit(self)
        self.conductorPassword_input.setGeometry(QtCore.QRect(170, 180, 158, 31))
        self.conductorPassword_input.setObjectName(("conductorPassword_input"))
        
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
        self.conductorLoginLabel.setText(QtGui.QApplication.translate("Form", "Conductor Login", None, QtGui.QApplication.UnicodeUTF8))
        self.enterConductorIDLabel.setText(QtGui.QApplication.translate("Form", "Enter Conductor ID", None, QtGui.QApplication.UnicodeUTF8))
        self.conductorPasswordLabel.setText(QtGui.QApplication.translate("Form", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setText(QtGui.QApplication.translate("Form", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("Form", "<- Go Back", None, QtGui.QApplication.UnicodeUTF8))
    
    def submitButtonClicked(self):
        self.conductorID = self.conductorID_input.text()
        logAttempt = 'Trying ID: ' + str(self.conductorID)
        print logAttempt
        
        loggerModule(logAttempt)
        
        ch = conductor_home()
        ch.check_login(self.conductorID)
        
        if ch.get_login():
            loggerModule('Succeeded')
            self.current_user_id = self.conductorID
            self.conductorHomeScreen()
        else:
            loggerModule('Failed')
            print "Not a valid Conductor ID"
        
    def conductorHomeScreen(self):
        print "Transitioning to conductor home screen"
        self.submitRequest.emit()
        
    def goBackOneScreen(self):
        print "Going Back one screen"
        self.goBack.emit()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = conductorLoginWidget()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

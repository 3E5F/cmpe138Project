# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passengerhomewidget.ui'
#
# Created: Sat May 09 19:45:36 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui
from conductor_home import *

class conductorHomeWidget(QtGui.QWidget):
    myTrains_signal = QtCore.Signal()
    schedules_signal = QtCore.Signal()
    updateStatus_signal = QtCore.Signal()
    goBack = QtCore.Signal()
    
    def __init__(self, current_user_id):
        super(conductorHomeWidget, self).__init__()
        self.current_user_id = current_user_id
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'conductorHomeWidget'
        self.name = ''
        self.description = ''
        ch = conductor_home()
        ch.check_login(self.current_user_id)
        
        self.c_name = self.current_user_id #PLACEHOLDER
        
        self.createLabels()
    
    def createLabels(self):
        self.setObjectName("conductorHomeWidget")
        self.resize(500,300)
    
        self.conductorHomeLabel = QtGui.QLabel(self)
        self.conductorHomeLabel.setGeometry(QtCore.QRect(180, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.conductorHomeLabel.setFont(font)
        self.conductorHomeLabel.setObjectName(("conductorHomeLabel"))
        
        self.ConductorNameField = QtGui.QTextEdit(self)
        self.ConductorNameField.setGeometry(QtCore.QRect(140, 60, 211, 31))
        self.ConductorNameField.setAcceptDrops(True)
        self.ConductorNameField.setObjectName(("ConductorNameField"))
        self.ConductorNameField.setReadOnly(True)
        self.ConductorNameField.setText(self.c_name)
        
        self.myTrains_button = QtGui.QPushButton(self)
        self.myTrains_button.setGeometry(QtCore.QRect(200, 100, 101, 41))
        self.myTrains_button.setObjectName(("myTrains_button"))
        self.myTrains_button.clicked.connect(self.myTrainsScreen)
        
        self.schedules_button = QtGui.QPushButton(self)
        self.schedules_button.setGeometry(QtCore.QRect(200, 140, 101, 41))
        self.schedules_button.setObjectName(("schedules_button"))
        self.schedules_button.clicked.connect(self.schedulesScreen)
        
        self.updateStatus_button = QtGui.QPushButton(self)
        self.updateStatus_button.setGeometry(QtCore.QRect(200, 180, 101, 41))
        self.updateStatus_button.setObjectName(("updateStatus_button"))
        self.updateStatus_button.clicked.connect(self.updateStatusScreen)
        
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
        self.conductorHomeLabel.setText(QtGui.QApplication.translate("Form", "Conductor Home", None, QtGui.QApplication.UnicodeUTF8))
        self.myTrains_button.setText(QtGui.QApplication.translate("Form", "My Train", None, QtGui.QApplication.UnicodeUTF8))
        self.schedules_button.setText(QtGui.QApplication.translate("Form", "Schedules", None, QtGui.QApplication.UnicodeUTF8))
        self.updateStatus_button.setText(QtGui.QApplication.translate("Form", "Update Status", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("Form", "<- Go Back", None, QtGui.QApplication.UnicodeUTF8))

    def myTrainsScreen(self):
        print "Transitioning to myTrainsScreen"
        self.myTrains_signal.emit()
        
    def schedulesScreen(self):
        print "Transitioning to schedulesScreen"
        self.schedules_signal.emit()
    
    def updateStatusScreen(self):
        print "Transitioning to updateStatusScreen"
        self.updateStatus_signal.emit()
        
    def goBackOneScreen(self):
        print "Going Back one screen"
        self.goBack.emit()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = conductorHomeWidget(70564689)
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

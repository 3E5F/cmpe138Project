# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passengerhomewidget.ui'
#
# Created: Sat May 09 19:45:36 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui

class conductorHomeWidget(QtGui.QWidget):
    myTrains_signal = QtCore.Signal()
    schedules_signal = QtCore.Signal()
    addNotification_signal = QtCore.Signal()
    
    def __init__(self):
        super(conductorHomeWidget, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'conductorHomeWidget'
        self.name = ''
        self.description = ''
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
        
        self.myTrains_button = QtGui.QPushButton(self)
        self.myTrains_button.setGeometry(QtCore.QRect(200, 100, 101, 41))
        self.myTrains_button.setObjectName(("myTrains_button"))
        self.myTrains_button.clicked.connect(self.myTrainsScreen)
        
        self.schedules_button = QtGui.QPushButton(self)
        self.schedules_button.setGeometry(QtCore.QRect(200, 140, 101, 41))
        self.schedules_button.setObjectName(("schedules_button"))
        self.schedules_button.clicked.connect(self.schedulesScreen)
        
        self.addNotification_button = QtGui.QPushButton(self)
        self.addNotification_button.setGeometry(QtCore.QRect(200, 180, 101, 41))
        self.addNotification_button.setObjectName(("addNotification_button"))
        self.addNotification_button.clicked.connect(self.addNotificationScreen)
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.conductorHomeLabel.setText(QtGui.QApplication.translate("Form", "Conductor Home", None, QtGui.QApplication.UnicodeUTF8))
        self.myTrains_button.setText(QtGui.QApplication.translate("Form", "My Trains", None, QtGui.QApplication.UnicodeUTF8))
        self.schedules_button.setText(QtGui.QApplication.translate("Form", "Schedules", None, QtGui.QApplication.UnicodeUTF8))
        self.addNotification_button.setText(QtGui.QApplication.translate("Form", "Add Notification", None, QtGui.QApplication.UnicodeUTF8))

    def myTrainsScreen(self):
        print "Transitioning to myTrainsScreen"
        
    def schedulesScreen(self):
        print "Transitioning to schedulesScreen"
    
    def addNotificationScreen(self):
        print "Transitioning to addNotificationScreen"
    


def main():
    app = QtGui.QApplication(sys.argv)
    ex = conductorHomeWidget()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

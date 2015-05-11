# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passengertrips.ui'
#
# Created: Sun May 10 00:33:43 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PySide import QtCore, QtGui
from passenger_home import *
from passenger_trips import *

class passengerTripsWidget(QtGui.QWidget):
    goBack = QtCore.Signal()
    
    def __init__(self, current_user_id):
        super(passengerTripsWidget, self).__init__()
        self.current_user_id = current_user_id
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'passengerTripsWidget'
        ph = passenger_home()
        ph.check_login(self.current_user_id)
        pt = passenger_trips(ph.cache_passenger)
        
        self.purchase_time=pt.get_purchase_time()
        self.destination = pt.get_destination()
        self.purchase_date = pt.get_purchase_date()
        
        self.createLabels()
    
    def createLabels(self):
        self.setObjectName(("Form"))
        self.resize(500, 300)
        
        self.MyTrip_Label = QtGui.QLabel(self)
        self.MyTrip_Label.setGeometry(QtCore.QRect(220, 20, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MyTrip_Label.setFont(font)
        self.MyTrip_Label.setObjectName(("MyTrip_Label"))
       
        self.purchaseTime_Label = QtGui.QLabel(self)
        self.purchaseTime_Label.setGeometry(QtCore.QRect(160, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.purchaseTime_Label.setFont(font)
        self.purchaseTime_Label.setObjectName(("purchaseTime_Label"))
        
        self.Date_label = QtGui.QLabel(self)
        self.Date_label.setGeometry(QtCore.QRect(160, 126, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Date_label.setFont(font)
        self.Date_label.setObjectName(("Date_label"))
        
        self.Destination_label = QtGui.QLabel(self)
        self.Destination_label.setGeometry(QtCore.QRect(160, 160, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Destination_label.setFont(font)
        self.Destination_label.setObjectName(("Destination_label"))
        
        self.purchaseTime_field = QtGui.QLabel(self)
        self.purchaseTime_field.setGeometry(QtCore.QRect(270, 90, 81, 16))
        self.purchaseTime_field.setObjectName(("purchaseTime_field"))
        
        self.date_field = QtGui.QLabel(self)
        self.date_field.setGeometry(QtCore.QRect(270, 125, 81, 16))
        self.date_field.setObjectName(("date_field"))
        
        self.destination_field = QtGui.QLabel(self)
        self.destination_field.setGeometry(QtCore.QRect(270, 161, 91, 16))
        self.destination_field.setObjectName(("destination_field"))
        
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
        self.MyTrip_Label.setText(QtGui.QApplication.translate("Form", "My Trip", None, QtGui.QApplication.UnicodeUTF8))
        self.purchaseTime_Label.setText(QtGui.QApplication.translate("Form", "Purchase time:", None, QtGui.QApplication.UnicodeUTF8))
        self.Date_label.setText(QtGui.QApplication.translate("Form", "Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.Destination_label.setText(QtGui.QApplication.translate("Form", "Destination:", None, QtGui.QApplication.UnicodeUTF8))
        self.purchaseTime_field.setText(QtGui.QApplication.translate("Form", self.purchase_time, None, QtGui.QApplication.UnicodeUTF8))
        self.date_field.setText(QtGui.QApplication.translate("Form", self.purchase_date, None, QtGui.QApplication.UnicodeUTF8))
        self.destination_field.setText(QtGui.QApplication.translate("Form", self.destination, None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("Form", "<- Go Back", None, QtGui.QApplication.UnicodeUTF8))

    def goBackOneScreen(self):
        print "Going Back one screen"
        self.goBack.emit()
def main():
    app = QtGui.QApplication(sys.argv)
    ex = passengerTripsWidget()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

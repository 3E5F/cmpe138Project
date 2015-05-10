# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat May 09 15:22:54 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui
from mainMenuWidget import mainMenuWidget
from passengerLoginWidget import passengerLoginWidget
from conductorLoginWidget import conductorLoginWidget
from passengerHomeWidget import passengerHomeWidget
from conductorHomeWidget import conductorHomeWidget
from passengerTripsWidget import passengerTripsWidget
from passengerCheckInWidget import passengerCheckInWidget

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(QtCore.QRect(500, 500, 500, 500))
        self.homeButton = QtGui.QPushButton(self)
        self.homeButton.setGeometry(QtCore.QRect(20, 10, 41, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.homeButton.setFont(font)
        
        self.CenterFrameWidget = QtGui.QDockWidget(self)
        self.CenterFrameWidget.setGeometry(QtCore.QRect(0, 50, 500, 450))
        self.CenterFrameWidget.setObjectName("CenterFrameWidget")
        
        self.retranslateUI()
        self.setHomeWidget()        
        
        
    def retranslateUI(self):
        self.homeButton.setText(QtGui.QApplication.translate("Back", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.homeButton.setFlat(False)
        self.homeButton.setEnabled(True)
        self.homeButton.clicked.connect(self.setHomeWidget)
    
    
    def setHomeWidget(self):
        print "Setting widget to home menu"
        self.currentWidget = mainMenuWidget()
        self.currentWidget.pLoginRequest.connect(self.set_passengerLogin_widget)
        self.currentWidget.cLoginRequest.connect(self.set_conductorLogin_widget)
        
        self.CenterFrameWidget.setWidget(self.currentWidget)
    
    def set_passengerLogin_widget(self):
        print "Setting widget to passenger login"
        self.currentWidget = passengerLoginWidget()
        self.currentWidget.submitRequest.connect(self.set_passengerHome_widget)
        self.currentWidget.goBack.connect(self.setHomeWidget)
        self.CenterFrameWidget.setWidget(self.currentWidget) #===========================================================
    
    def set_conductorLogin_widget(self):
        print "Setting widget to conductor login"
        self.currentWidget = conductorLoginWidget()
        self.currentWidget.submitRequest.connect(self.set_conductorHome_widget)
        self.currentWidget.goBack.connect(self.setHomeWidget)
        self.CenterFrameWidget.setWidget(self.currentWidget) #===========================================================
    
    def set_passengerHome_widget(self):
        print "Setting widget to passenger home"
        current_user_id = self.currentWidget.current_user_id
        self.currentWidget = passengerHomeWidget(current_user_id)
        self.currentWidget.myTrips_signal.connect(self.set_myTrips_widget)
        self.currentWidget.trainSched_signal.connect(self.set_trainSched_widget)
        self.currentWidget.checkIn_signal.connect(self.set_checkIn_widget)
        self.currentWidget.purchaseTickets_signal.connect(self.set_purchaseTickets_widget)
        self.currentWidget.goBack.connect(self.set_passengerLogin_widget)
        
        self.CenterFrameWidget.setWidget(self.currentWidget)
        
    
    def set_conductorHome_widget(self):
        print "Setting widget to conductor home"
        self.currentWidget = conductorHomeWidget()
        self.currentWidget.goBack.connect(self.set_conductorLogin_widget)
        self.CenterFrameWidget.setWidget(self.currentWidget)
    
    def set_myTrips_widget(self):
        print "Setting widget to passenger myTrips"
        current_user_id = self.currentWidget.current_user_id
        self.currentWidget = passengerTripsWidget(current_user_id)
        
        self.currentWidget.goBack.connect(self.set_passengerHome_widget)
        self.CenterFrameWidget.setWidget(self.currentWidget)
    
    def set_trainSched_widget(self):
        print "Setting widget to passenger trainSched"
    
    def set_checkIn_widget(self):
        print "Setting widget to passenger checkIn"
        current_user_id = self.currentWidget.current_user_id
        self.currentWidget = passengerCheckInWidget(current_user_id)
        self.currentWidget.goBack.connect(self.set_passengerHome_widget)
        self.CenterFrameWidget.setWidget(self.currentWidget)
        
    def set_purchaseTickets_widget(self):
        print "Setting widget to passenger purchaseTickets"
    
    
def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    ex.setWindowTitle("PalTrain") 
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
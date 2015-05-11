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
from passengerTrainSchedWidget import passengerTrainSchedWidget
from purchaseTicketsWidget import purchaseTicketsWidget
from conductorMyTrainsWidget import conductorMyTrainsWidget
from conductorSchedulesWidget import conductorSchedulesWidget
from conductorUpdateStatusWidget import conductorUpdateStatusWidget
from purchaseReceiptWidget import purchaseReceiptWidget

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        logFile=open('LogFile.txt', 'w')
        logFile.write('Starting Log \n')
        logFile.close()
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
        logFile=open('LogFile.txt', 'a')
        logFile.write('Setting widget to home menu \n')
        logFile.close()
        self.currentWidget = mainMenuWidget()
        self.currentWidget.purchaseTicketRequest.connect(self.set_purchaseTicket_widget)
        self.currentWidget.pLoginRequest.connect(self.set_passengerLogin_widget)
        self.currentWidget.cLoginRequest.connect(self.set_conductorLogin_widget)
        
        self.CenterFrameWidget.setWidget(self.currentWidget)
    
    def set_passengerLogin_widget(self):
        print "Setting widget to passenger login"
        logFile=open('LogFile.txt', 'a')
        logFile.write('Setting widget to passenger login \n')
        logFile.close()
        self.currentWidget = passengerLoginWidget()
        self.currentWidget.submitRequest.connect(self.set_passengerHome_widget)
        self.currentWidget.goBack.connect(self.setHomeWidget)
        self.CenterFrameWidget.setWidget(self.currentWidget) #===========================================================
    
    def set_conductorLogin_widget(self):
        print "Setting widget to conductor login"
        logFile=open('LogFile.txt', 'a')
        logFile.write('Setting widget to conductor login \n')
        logFile.close()
        self.currentWidget = conductorLoginWidget()
        self.currentWidget.submitRequest.connect(self.set_conductorHome_widget)
        self.currentWidget.goBack.connect(self.setHomeWidget)
        self.CenterFrameWidget.setWidget(self.currentWidget) #===========================================================
    
    def set_purchaseTicket_widget(self):
        print "Setting widget to passenger purchaseTickets"
        logFile=open('LogFile.txt', 'a')
        logFile.write('Setting widget to passenger purchaseTickets \n')
        logFile.close()
        self.currentWidget=purchaseTicketsWidget()
        self.currentWidget.purchaseReceipt_signal.connect(self.set_receipt_widget)
        self.currentWidget.goBack.connect(self.setHomeWidget)
        self.CenterFrameWidget.setWidget(self.currentWidget)
    
    def set_receipt_widget(self):
        print "Setting widget to purchase receipt"
        logFile=open('LogFile.txt', 'a')
        logFile.write('Setting widget to purchase receipt \n')
        logFile.close()
        newPassengerID = self.currentWidget.newPassengerID
        self.currentWidget = purchaseReceiptWidget(newPassengerID)
        self.currentWidget.goBack.connect(self.setHomeWidget)
        self.CenterFrameWidget.setWidget(self.currentWidget)
    
    def set_passengerHome_widget(self):
        print "Setting widget to passenger home"
        logFile=open('LogFile.txt', 'a')
        logFile.write('Setting widget to passenger home \n')
        logFile.close()
        current_user_id = self.currentWidget.current_user_id
        self.currentWidget = passengerHomeWidget(current_user_id)
        self.currentWidget.myTrips_signal.connect(self.set_myTrips_widget)
        self.currentWidget.trainSched_signal.connect(self.set_p_trainSched_widget)
        self.currentWidget.checkIn_signal.connect(self.set_p_checkin_widget)
        #self.currentWidget.purchaseTickets_signal.connect(self.set_p_purchaseTickets_widget)
        
        self.currentWidget.goBack.connect(self.set_passengerLogin_widget)
        self.CenterFrameWidget.setWidget(self.currentWidget)
        
    
    def set_conductorHome_widget(self):
        print "Setting widget to conductor home"
        logFile=open('LogFile.txt', 'a')
        logFile.write('Setting widget to conductor home \n')
        logFile.close()
        current_user_id = self.currentWidget.current_user_id
        self.currentWidget = conductorHomeWidget(current_user_id)
        self.currentWidget.myTrains_signal.connect(self.set_c_myTrains_widget)
        self.currentWidget.schedules_signal.connect(self.set_c_schedules)
        self.currentWidget.updateStatus_signal.connect(self.set_c_updateStatus_widget)
        
        self.currentWidget.goBack.connect(self.set_conductorLogin_widget)
        self.CenterFrameWidget.setWidget(self.currentWidget)
    
    def set_myTrips_widget(self):
        print "Setting widget to passenger myTrips"
        logFile=open('LogFile.txt', 'a')
        logFile.write('Setting widget to passenger myTrips \n')
        logFile.close()
        current_user_id = self.currentWidget.current_user_id
        self.currentWidget = passengerTripsWidget(current_user_id)
        
        self.currentWidget.goBack.connect(self.set_passengerHome_widget)
        self.CenterFrameWidget.setWidget(self.currentWidget)
    
    def set_p_trainSched_widget(self):
        print "Setting widget to passenger trainSched"
        logFile=open('LogFile.txt', 'a')
        logFile.write('Setting widget to passenger trainSched \n')
        logFile.close()
        current_user_id = self.currentWidget.current_user_id
        self.currentWidget = passengerTrainSchedWidget(current_user_id)
        
        self.currentWidget.goBack.connect(self.set_passengerHome_widget)
        self.CenterFrameWidget.setWidget(self.currentWidget)
    
    def set_p_checkin_widget(self):
        print "Setting widget to passenger checkIn"
        logFile=open('LogFile.txt', 'a')
        logFile.write('Setting widget to passenger checkIn \n')
        logFile.close()
        current_user_id = self.currentWidget.current_user_id
        self.currentWidget = passengerCheckInWidget(current_user_id)
        
        self.currentWidget.goBack.connect(self.set_passengerHome_widget)
        self.CenterFrameWidget.setWidget(self.currentWidget)
        
    def set_c_myTrains_widget(self):
        print "Setting widget to conductor myTrains"
        logFile=open('LogFile.txt', 'a')
        logFile.write('Setting widget to conductor myTrains \n')
        logFile.close()
        current_user_id = self.currentWidget.current_user_id
        self.currentWidget = conductorMyTrainsWidget(current_user_id)
        
        self.currentWidget.goBack.connect(self.set_conductorHome_widget)
        self.CenterFrameWidget.setWidget(self.currentWidget)
    
    def set_c_schedules(self):
        print "Setting widget to conductor schedules"
        logFile=open('LogFile.txt', 'a')
        logFile.write('Setting widget to conductor schedules \n')
        logFile.close()
        current_user_id = self.currentWidget.current_user_id
        self.currentWidget = conductorSchedulesWidget(current_user_id)
        
        self.currentWidget.goBack.connect(self.set_conductorHome_widget)
        self.CenterFrameWidget.setWidget(self.currentWidget)
    
    def set_c_updateStatus_widget(self):
        print "Setting widget to conductor updateStatus"
        logFile=open('LogFile.txt', 'a')
        logFile.write('Setting widget to conductor updateStatus \n')
        logFile.close()
        current_user_id = self.currentWidget.current_user_id
        self.currentWidget = conductorUpdateStatusWidget(current_user_id)
        
        self.currentWidget.goBack.connect(self.set_conductorHome_widget)
        self.CenterFrameWidget.setWidget(self.currentWidget)
        
    
    
def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    ex.setWindowTitle("Train Database Project") 
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
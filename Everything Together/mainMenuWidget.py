import sys
from PySide import QtCore, QtGui

class mainMenuWidget(QtGui.QWidget):
    pLoginRequest = QtCore.Signal()
    cLoginRequest = QtCore.Signal()
    purchaseTicketRequest = QtCore.Signal()
    
    def __init__(self):
        super (mainMenuWidget, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.widget_type = 'mainMenu'
        self.name = ''
        self.description = ''
        self.createLabels()
    
    def createLabels(self):
        self.setObjectName("Form")
        self.resize(500, 380)
        #self.label = QtGui.QLabel(self)
        #self.label.setGeometry(QtCore.QRect(250, 70, 101, 51))
        #font = QtGui.QFont()
        #font.setPointSize(20)
        #self.label.setFont(font)
        
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 0, 200, 300))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        #self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(("verticalLayout"))
        
        self.PalTrainLabel = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PalTrainLabel.setFont(font)
        self.PalTrainLabel.setObjectName(("PalTrainLabel"))
        self.verticalLayout.addWidget(self.PalTrainLabel)
        
        self.PassengerLoginButton = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PassengerLoginButton.setFont(font)
        self.PassengerLoginButton.setObjectName(("PassengerLoginButton"))
        self.verticalLayout.addWidget(self.PassengerLoginButton)
        
        self.ConductorLoginButton = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ConductorLoginButton.setFont(font)
        self.ConductorLoginButton.setObjectName(("ConductorLoginButton"))
        self.verticalLayout.addWidget(self.ConductorLoginButton)
        
        self.PurchaseButton = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PurchaseButton.setFont(font)
        self.PurchaseButton.setObjectName(("ConductorLoginButton"))
        self.verticalLayout.addWidget(self.PurchaseButton)
        
        
        #Connecting Buttons
        self.PassengerLoginButton.clicked.connect(self.passengerLoginScreen)
        self.ConductorLoginButton.clicked.connect(self.conductorLoginScreen)
        self.PurchaseButton.clicked.connect(self.purchaseScreen)
                
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        

    def retranslateUi(self):
        # self.tab_label.setText(QtGui.QApplication.translate("api_widget", "API", None, QtGui.QApplication.UnicodeUTF8))
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        #self.label.setText(QtGui.QApplication.translate("Form", "PalTrain", None, QtGui.QApplication.UnicodeUTF8))
        self.PalTrainLabel.setText(QtGui.QApplication.translate("Form", "Train Database", None, QtGui.QApplication.UnicodeUTF8))
        self.PassengerLoginButton.setText(QtGui.QApplication.translate("Form", "Passenger Login", None, QtGui.QApplication.UnicodeUTF8))
        self.ConductorLoginButton.setText(QtGui.QApplication.translate("Form", "Conductor Login", None, QtGui.QApplication.UnicodeUTF8))
        self.PurchaseButton.setText(QtGui.QApplication.translate("Form", "Purchase Ticket", None, QtGui.QApplication.UnicodeUTF8))
        
        #self.UpdateButton.setText(QtGui.QApplication.translate("Form", "Update", None, QtGui.QApplication.UnicodeUTF8))
        #self.NameLabel.setText(QtGui.QApplication.translate("Form", "Name               ", None, QtGui.QApplication.UnicodeUTF8))
        #self.DescriptionLabel.setText(QtGui.QApplication.translate("Form", "Description       ", None, QtGui.QApplication.UnicodeUTF8))
    
    def purchaseScreen(self):
        print "Transitioning to purchase screen"
        self.purchaseTicketRequest.emit()
    
    def passengerLoginScreen(self):
        print "Transitioning to passenger login screen"
        self.pLoginRequest.emit()
        
    def conductorLoginScreen(self):
        print "Transitioning to conductor login screen"
        self.cLoginRequest.emit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = mainMenuWidget()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
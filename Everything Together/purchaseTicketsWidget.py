import sys
from PySide import QtCore, QtGui
from passenger_insert import *

class purchaseTicketsWidget(QtGui.QWidget):
    goBack = QtCore.Signal()
    purchaseReceipt_signal = QtCore.Signal()
    
    def __init__(self):
        super(purchaseTicketsWidget, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'purchaseTicketsWidget'
        
        self.createLabels()
    
    def createLabels(self):
        self.setObjectName(("Form"))
        self.resize(500, 300)
        
        self.purchaseTicketsTitle = QtGui.QLabel(self)
        self.purchaseTicketsTitle.setGeometry(QtCore.QRect(188, 20, 150, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.purchaseTicketsTitle.setFont(font)
        self.purchaseTicketsTitle.setObjectName(("purchaseTicketsTitle"))
        
        self.backButton = QtGui.QPushButton(self)
        self.backButton.setGeometry(QtCore.QRect(20, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backButton.setFont(font)
        self.backButton.setObjectName(("backButton"))
        self.backButton.clicked.connect(self.goBackOneScreen)

        #=========================================================================================================
        self.FirstName_Label = QtGui.QLabel(self)
        self.FirstName_Label.setGeometry(QtCore.QRect(100, 130, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FirstName_Label.setFont(font)
        self.FirstName_Label.setObjectName(("FirstName_Label"))
        
        self.LastName_Label = QtGui.QLabel(self)
        self.LastName_Label.setGeometry(QtCore.QRect(100, 170, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LastName_Label.setFont(font)
        self.LastName_Label.setObjectName(("LastName_Label"))
        
        self.Destination_Label = QtGui.QLabel(self)
        self.Destination_Label.setGeometry(QtCore.QRect(100, 210, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Destination_Label.setFont(font)
        self.Destination_Label.setObjectName(("Destination_Label"))
        
        self.FirstName_Input = QtGui.QLineEdit(self)
        self.FirstName_Input.setGeometry(QtCore.QRect(200, 126, 141, 31))
        self.FirstName_Input.setObjectName(("FirstName_Input"))
        
        self.LastName_Input = QtGui.QLineEdit(self)
        self.LastName_Input.setGeometry(QtCore.QRect(200, 165, 141, 31))
        self.LastName_Input.setObjectName(("LastName_Input"))
        
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(200, 209, 141, 21))
        self.comboBox.setObjectName(("comboBox"))
        self.comboBox.addItem((""))
        self.comboBox.addItem((""))
        self.comboBox.addItem((""))
        self.comboBox.addItem((""))
        self.comboBox.addItem((""))
        
        self.PurchaseButton = QtGui.QPushButton(self)
        self.PurchaseButton.setGeometry(QtCore.QRect(210, 250, 81, 31))
        self.PurchaseButton.setObjectName(("PurchaseButton"))
        self.PurchaseButton.clicked.connect(self.purchaseButtonClicked)
        
        #=======================================================================================================


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.purchaseTicketsTitle.setText(QtGui.QApplication.translate("Form", "Purchase Ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("Form", "<- Go Back", None, QtGui.QApplication.UnicodeUTF8))
        
        self.FirstName_Label.setText(QtGui.QApplication.translate("Form", "First Name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LastName_Label.setText(QtGui.QApplication.translate("Form", "Last Name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Destination_Label.setText(QtGui.QApplication.translate("Form", "Destination: ", None, QtGui.QApplication.UnicodeUTF8))

        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form", "New York", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Form", "Gotham", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Form", "Washington DC", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Form", "Olympia", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Form", "Pawnee", None, QtGui.QApplication.UnicodeUTF8))
        
        self.PurchaseButton.setText(QtGui.QApplication.translate("Form", "Purchase", None, QtGui.QApplication.UnicodeUTF8))

    def purchaseButtonClicked(self):
        print "Purchase button clicked."
        userFirstNameInput = self.FirstName_Input.text()
        userLastNameInput = self.LastName_Input.text()
        destination = self.comboBox.currentText()
        
        pi = passenger_insert()
        pi.insert_user(userFirstNameInput, userLastNameInput, destination)
        
        self.newPassengerID = pi.get_passenger_id()
        print "New Passenger ID: " + str(self.newPassengerID)
        self.purchaseReceipt_signal.emit()

    def goBackOneScreen(self):
        print "Going Back one screen"
        self.goBack.emit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = purchaseTicketsWidget() #Using Bruce Wayne to Test Widget as standalone
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

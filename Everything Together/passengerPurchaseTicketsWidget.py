import sys
from PySide import QtCore, QtGui
from passenger_home import *
from passenger_checkin import *

class passengerPurchaseTicketsWidget(QtGui.QWidget):
    goBack = QtCore.Signal()
    
    def __init__(self, current_user_id):
        super(passengerPurchaseTicketsWidget, self).__init__()
        self.current_user_id = current_user_id
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'passengerPurchaseTicketsWidget'
        #ph = passenger_home()
        #ph.check_login(self.current_user_id)
        #pc = passenger_checkin(ph.cache_passenger)
        
        #self.passenger_id=pc.get_ticket_number()
        #self.passenger_name = pc.get_passenger_name()
        
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

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.purchaseTicketsTitle.setText(QtGui.QApplication.translate("Form", "Purchase Ticket", None, QtGui.QApplication.UnicodeUTF8))
    
        self.backButton.setText(QtGui.QApplication.translate("Form", "<- Go Back", None, QtGui.QApplication.UnicodeUTF8))

    def goBackOneScreen(self):
        print "Going Back one screen"
        self.goBack.emit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = passengerPurchaseTicketsWidget(2087219) #Using Bruce Wayne to Test Widget as standalone
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

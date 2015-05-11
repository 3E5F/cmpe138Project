import sys
from PySide import QtCore, QtGui
from passenger_home import *
from passenger_checkin import *

class passengerCheckInWidget(QtGui.QWidget):
    goBack = QtCore.Signal()
    
    def __init__(self, current_user_id):
        super(passengerCheckInWidget, self).__init__()
        self.current_user_id = current_user_id
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'passengerCheckInWidget'
        ph = passenger_home()
        ph.check_login(self.current_user_id)
        pc = passenger_checkin(ph.cache_passenger)
        
        self.passenger_id=pc.get_ticket_number()
        self.passenger_name = pc.get_passenger_name()
        
        self.createLabels()
    
    def createLabels(self):
        self.setObjectName(("Form"))
        self.resize(500, 300)
        
        self.CheckIn_Label = QtGui.QLabel(self)
        self.CheckIn_Label.setGeometry(QtCore.QRect(210, 20, 80, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CheckIn_Label.setFont(font)
        self.CheckIn_Label.setObjectName(("CheckIn_Label"))
       
        self.passenger_id_label = QtGui.QLabel(self)
        self.passenger_id_label.setGeometry(QtCore.QRect(160, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passenger_id_label.setFont(font)
        self.passenger_id_label.setObjectName(("passenger_id_label"))
        
        self.passenger_name_label = QtGui.QLabel(self)
        self.passenger_name_label.setGeometry(QtCore.QRect(160, 126, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passenger_name_label.setFont(font)
        self.passenger_name_label.setObjectName(("passenger_name_label"))
        
        
        
        self.passenger_id_field = QtGui.QLabel(self)
        self.passenger_id_field.setGeometry(QtCore.QRect(270, 90, 81, 16))
        self.passenger_id_field.setObjectName(("passenger_id_field"))
        
        self.passenger_name_field = QtGui.QLabel(self)
        self.passenger_name_field.setGeometry(QtCore.QRect(270, 125, 81, 16))
        self.passenger_name_field.setObjectName(("passenger_name_field"))
        
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(160, 190, 181, 141))
        self.label.setText((""))
        self.label.setPixmap(QtGui.QPixmap(("./qrcode.png")))
        
        
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
        self.CheckIn_Label.setText(QtGui.QApplication.translate("Form", "Check In", None, QtGui.QApplication.UnicodeUTF8))
        self.passenger_id_label.setText(QtGui.QApplication.translate("Form", "Passenger ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.passenger_name_label.setText(QtGui.QApplication.translate("Form", "Passenger Name:", None, QtGui.QApplication.UnicodeUTF8))

        self.passenger_id_field.setText(QtGui.QApplication.translate("Form", self.passenger_id, None, QtGui.QApplication.UnicodeUTF8))
        self.passenger_name_field.setText(QtGui.QApplication.translate("Form", self.passenger_name, None, QtGui.QApplication.UnicodeUTF8))
    
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

import sys
from PySide import QtCore, QtGui
from conductor_home import *

class conductorAddNotificationsWidget(QtGui.QWidget):
    goBack = QtCore.Signal()
    
    def __init__(self, current_user_id):
        super(conductorAddNotificationsWidget, self).__init__()
        self.current_user_id = current_user_id
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'conductorAddNotificationsWidget'
        #ph = passenger_home()
        #ph.check_login(self.current_user_id)
        #pc = passenger_checkin(ph.cache_passenger)
        
        #self.passenger_id=pc.get_ticket_number()
        #self.passenger_name = pc.get_passenger_name()
        
        self.createLabels()
    
    def createLabels(self):
        self.setObjectName(("Form"))
        self.resize(500, 300)
        
        self.addNotification_title = QtGui.QLabel(self)
        self.addNotification_title.setGeometry(QtCore.QRect(185, 20, 150, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addNotification_title.setFont(font)
        self.addNotification_title.setObjectName(("addNotification_title"))
        
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
        self.addNotification_title.setText(QtGui.QApplication.translate("Form", "Add Notification", None, QtGui.QApplication.UnicodeUTF8))
    
        self.backButton.setText(QtGui.QApplication.translate("Form", "<- Go Back", None, QtGui.QApplication.UnicodeUTF8))

    def goBackOneScreen(self):
        print "Going Back one screen"
        self.goBack.emit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = conductorAddNotificationsWidget(70564689) #Using Bruce Wayne to Test Widget as standalone
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

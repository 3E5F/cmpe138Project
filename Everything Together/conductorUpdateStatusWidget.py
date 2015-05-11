import sys
from PySide import QtCore, QtGui
from conductor_home import *
from conductor_train import *
from update_status import *

class conductorUpdateStatusWidget(QtGui.QWidget):
    goBack = QtCore.Signal()
    
    def __init__(self, current_user_id):
        super(conductorUpdateStatusWidget, self).__init__()
        self.current_user_id = current_user_id
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'conductorUpdateStatusWidget'
        self.ch = conductor_home()
        self.ch.check_login(self.current_user_id)
        self.ct = conductor_trains(self.ch.cache_conductor)
        self.ct.query_conductor_information()
        self.myTrainNumber = self.ct.get_conductor_train()
        
        self.createLabels()
    
    def createLabels(self):
        self.setObjectName(("Form"))
        self.resize(500, 300)
        
        self.updateStatus_title = QtGui.QLabel(self)
        self.updateStatus_title.setGeometry(QtCore.QRect(185, 20, 150, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.updateStatus_title.setFont(font)
        self.updateStatus_title.setObjectName(("updateStatus_title"))
        
        
        self.status_Label = QtGui.QLabel(self)
        self.status_Label.setGeometry(QtCore.QRect(150, 100, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.status_Label.setFont(font)
        self.status_Label.setObjectName(("status_Label"))
        
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(200, 99, 141, 21))
        self.comboBox.setObjectName(("comboBox"))
        self.comboBox.addItem((""))
        self.comboBox.addItem((""))
        self.comboBox.addItem((""))
        self.comboBox.addItem((""))
        
        self.updateButton = QtGui.QPushButton(self)
        self.updateButton.setGeometry(QtCore.QRect(210, 150, 81, 31))
        self.updateButton.setObjectName(("updateButton"))
        self.updateButton.clicked.connect(self.updateButtonClicked)
        
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
        self.updateStatus_title.setText(QtGui.QApplication.translate("Form", "Update Status", None, QtGui.QApplication.UnicodeUTF8))
        self.status_Label.setText(QtGui.QApplication.translate("Form", "Status: ", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form", "On-Time", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Form", "Delayed", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Form", "Behind", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Form", "Ahead", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("Form", "<- Go Back", None, QtGui.QApplication.UnicodeUTF8))
        self.updateButton.setText(QtGui.QApplication.translate("Form", "Update", None, QtGui.QApplication.UnicodeUTF8))

    def updateButtonClicked(self):
        print "Update button clicked."
        selectedStatus = self.comboBox.currentText()
        
        us = update_status()
        us.update_train_status(self.myTrainNumber, selectedStatus)
        #print self.myTrainNumber
        #print selectedStatus
        

    def goBackOneScreen(self):
        print "Going Back one screen"
        self.goBack.emit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = conductorUpdateStatusWidget(70564689) #Using Bruce Wayne to Test Widget as standalone
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

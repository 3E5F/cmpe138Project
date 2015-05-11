import sys
from PySide import QtCore, QtGui
from conductor_home import *
from conductor_train import *

class conductorMyTrainsWidget(QtGui.QWidget):
    goBack = QtCore.Signal()
    
    def __init__(self, current_user_id):
        super(conductorMyTrainsWidget, self).__init__()
        self.current_user_id = current_user_id
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'conductorMyTrainsWidget'
        self.ch = conductor_home()
        self.ch.check_login(self.current_user_id)
        self.ct = conductor_trains(self.ch.cache_conductor)
        self.ct.query_conductor_information()
        self.myTrainNumber = self.ct.get_conductor_train()
        
        self.createLabels()
    
    def createLabels(self):
        self.setObjectName(("Form"))
        self.resize(500, 300)
        
        self.conductorMyTrains_title = QtGui.QLabel(self)
        self.conductorMyTrains_title.setGeometry(QtCore.QRect(210, 20, 150, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.conductorMyTrains_title.setFont(font)
        self.conductorMyTrains_title.setObjectName(("conductorMyTrains_title"))
        
        
        self.myTrainNum_Label = QtGui.QLabel(self)
        self.myTrainNum_Label.setGeometry(QtCore.QRect(150, 90, 150, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.myTrainNum_Label.setFont(font)
        self.myTrainNum_Label.setObjectName(("myTrainNum_Label"))
        
        self.myTrainNum_Field = QtGui.QLabel(self)
        self.myTrainNum_Field.setGeometry(QtCore.QRect(300, 90, 110, 16))
        self.myTrainNum_Field.setFont(font)
        self.myTrainNum_Field.setObjectName(("myTrainNum_Field"))
        
        
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
        self.conductorMyTrains_title.setText(QtGui.QApplication.translate("Form", "My Train", None, QtGui.QApplication.UnicodeUTF8))
    
        self.myTrainNum_Label.setText(QtGui.QApplication.translate("Form", "My Train Number ", None, QtGui.QApplication.UnicodeUTF8))
        self.myTrainNum_Field.setText(QtGui.QApplication.translate("Form", str(self.myTrainNumber), None, QtGui.QApplication.UnicodeUTF8))
    
        self.backButton.setText(QtGui.QApplication.translate("Form", "<- Go Back", None, QtGui.QApplication.UnicodeUTF8))

    def goBackOneScreen(self):
        print "Going Back one screen"
        self.goBack.emit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = conductorMyTrainsWidget(70564689) #Using Bruce Wayne to Test Widget as standalone
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

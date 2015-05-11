import sys
from PySide import QtCore, QtGui

class purchaseTicketsWidget(QtGui.QWidget):
    goBack = QtCore.Signal()
    
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
    ex = purchaseTicketsWidget() #Using Bruce Wayne to Test Widget as standalone
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

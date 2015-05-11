import sys
from PySide import QtCore, QtGui
from conductor_home import *
from train_schedule import *

class conductorSchedulesWidget(QtGui.QWidget):
    goBack = QtCore.Signal()
    
    def __init__(self, current_user_id):
        super(conductorSchedulesWidget, self).__init__()
        self.current_user_id = current_user_id
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'conductorSchedulesWidget'
        
        self.ts = train_schedules()
        self.ts.query_train_schedules()
        
        self.createLabels()
    
    def createLabels(self):
        self.setObjectName(("Form"))
        self.resize(500, 300)
        
        self.conductorSchedules_title = QtGui.QLabel(self)
        self.conductorSchedules_title.setGeometry(QtCore.QRect(185, 20, 150, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.conductorSchedules_title.setFont(font)
        self.conductorSchedules_title.setObjectName(("conductorSchedules_title"))
        
        
        self.schedule_table = QtGui.QTableWidget(self)
        self.schedule_table.setGeometry(QtCore.QRect(50, 100, 400, 175))
        self.schedule_table.setObjectName(("schedule_table"))
        self.schedule_table.setRowCount(5)
        self.schedule_table.setColumnCount(5)
        self.schedule_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.schedule_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.schedule_table.horizontalHeader().setVisible(True)
        self.schedule_table.verticalHeader().setVisible(False)
        listOfHeaders = ['Train No', 'Cabin Temp', "Capacity", "Status", "Last Location"]
        self.schedule_table.setHorizontalHeaderLabels(listOfHeaders)
        self.schedule_table.setColumnWidth(0,55)
        self.schedule_table.setColumnWidth(1,70)
        self.schedule_table.setColumnWidth(2,70)
        self.populateTable()
        
        
        self.backButton = QtGui.QPushButton(self)
        self.backButton.setGeometry(QtCore.QRect(20, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backButton.setFont(font)
        self.backButton.setObjectName(("backButton"))
        self.backButton.clicked.connect(self.goBackOneScreen)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def populateTable(self):
        #self.schedule_table.setItem(2,2,QtGui.QTableWidgetItem("hi"))
        for trainNo in xrange(5):
            TrainNumber = str(trainNo+1)
            self.schedule_table.setItem(trainNo, 0, QtGui.QTableWidgetItem(TrainNumber))
            
            CabinTemp = str(self.ts.get_cabin_temp(trainNo+1))
            self.schedule_table.setItem(trainNo, 1, QtGui.QTableWidgetItem(CabinTemp))
            
            Capacity = str(self.ts.get_seat_cap(trainNo+1))
            self.schedule_table.setItem(trainNo, 2, QtGui.QTableWidgetItem(Capacity))
            
            status = self.ts.get_status(trainNo+1)
            self.schedule_table.setItem(trainNo, 3, QtGui.QTableWidgetItem(status))
            
            recentLoc = self.ts.get_recent_location(trainNo+1)
            self.schedule_table.setItem(trainNo, 4, QtGui.QTableWidgetItem(recentLoc))
    
    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.conductorSchedules_title.setText(QtGui.QApplication.translate("Form", "Train Schedules", None, QtGui.QApplication.UnicodeUTF8))
    
        self.backButton.setText(QtGui.QApplication.translate("Form", "<- Go Back", None, QtGui.QApplication.UnicodeUTF8))

    def goBackOneScreen(self):
        print "Going Back one screen"
        self.goBack.emit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = conductorSchedulesWidget(70564689) #Using Bruce Wayne to Test Widget as standalone
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

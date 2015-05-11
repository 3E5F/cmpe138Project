class loggerModule():
    def __init__(self, text):
        self.text=text
        self.log(self.text)
    
    def log(self, text):
        logFile=open('LogFile.txt', 'a')
        logFile.write(text)
        logFile.write('\n')
        logFile.close()
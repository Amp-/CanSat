from PyQt5 import QtCore, QtSerialPort

class Com():

    def __init__(self,portName, baudRate, serialPort):
        self.serial = serialPort
        self.serial.setPortName(portName)
        self.serial.setBaudRate(baudRate)

    def open(self):
        try:
            self.serial.open()
            print(self.serial.isOpen())
        except:
            print(f"Cant opnet {self.serial.portName()}")


    def read(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip('\r\n')
            return text


    def send(self, data):
        self.serial.write(data)

    def togle(self):
        if not self.serial.isOpen():
            if not self.serial.open(QtCore.QIODevice.ReadWrite):
                return False

    def close(self):
        self.serial.close()
from PyQt5 import QtCore, QtWidgets, QtSerialPort
import pyqtgraph as pg
from uart import Com

baudRate=9600
portName = "/dev/ttyACM0"

com = Com(baudRate=baudRate, portName=portName, serialPort=QtSerialPort.QSerialPort())
class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.message_le = QtWidgets.QLineEdit()
        self.send_btn = QtWidgets.QPushButton(
            text="Send",
            clicked=self.send
        )
        self.output_te = QtWidgets.QTextEdit(readOnly=True)
        self.button = QtWidgets.QPushButton(
            text="Connect",
            checkable=True,
            toggled=self.on_toggled
        )
        lay = QtWidgets.QVBoxLayout(self)
        hlay = QtWidgets.QHBoxLayout()
        hlay.addWidget(self.message_le)
        hlay.addWidget(self.send_btn)
        lay.addLayout(hlay)
        lay.addWidget(self.output_te)

        lay.addWidget(self.button)
        self.serial = com.serial
        self.serial.readyRead.connect(lambda: self.receive())

    def receive(self):
            text = com.read()
            self.output_te.append(text)
    def send(self,data):
        com.send(self.message_le.text().encode())
    def on_toggled(self, checked):
        self.button.setText("Disconnect" if checked else "Connect")
        if checked:
            t = com.togle()
            if t == False:
                self.button.setChecked(False)
        else:
            com.close()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
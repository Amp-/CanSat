import random
import serial
import serial.tools.list_ports


class Communication:
    baudrate = ''
    portName = ''
    ports = serial.tools.list_ports.comports()
    ser = serial.Serial()

    def __init__(self):
        self.baudrate = 9600
        print("the available ports are (if none appear, press any letter): ")
        for port in sorted(self.ports):
            print(("{}".format(port)))
        self.portName = '/dev/ttyACM0'
        # self.portName = input("write serial port name (ex: /dev/ttyUSB0): ")
        try:
            self.ser = serial.Serial(self.portName, self.baudrate)
        except serial.serialutil.SerialException:
            print("Can't open : ", self.portName)


    def close(self):
        if(self.ser.isOpen()):
            self.ser.close()
        else:
            print(self.portName, " it's already closed")

    def getData(self):
        value = self.ser.readline()
        value_chain = str(value, "UTF-8").strip()
        if (value_chain != 'Empty' and value_chain != 'Fail'):
            if (len(value_chain)) < 5 :
                return int(value_chain)

    def isOpen(self):
        return self.ser.isOpen()


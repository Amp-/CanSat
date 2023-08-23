import sys
from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
from communications import Communication
from dataBase import data_base
from PyQt5.QtWidgets import QPushButton
from graph import graph_temperature

pg.setConfigOption('background', (33, 33, 33))
pg.setConfigOption('foreground', (197, 198, 199))
# Interface variables
app = QtWidgets.QApplication(sys.argv)
view = pg.GraphicsView()
Layout = pg.GraphicsLayout()
view.setCentralItem(Layout)
view.show()
view.setWindowTitle('Flight monitoring')
view.resize(1200, 700)

# declare object for serial Communication
ser = Communication()
# declare object for storage in CSV
data_base = data_base()
# Fonts for text items
font = QtGui.QFont()
font.setPixelSize(90)

# buttons style
style = "background-color:rgb(29, 185, 84);color:rgb(0,0,0);font-size:14px;"

# Declare graphs
# Button 1
proxy = QtWidgets.QGraphicsProxyWidget()
save_button = QtWidgets.QPushButton('Start storage')
save_button.setStyleSheet(style)
save_button.clicked.connect(data_base.start)
proxy.setWidget(save_button)

# Button 2
proxy2 = QtWidgets.QGraphicsProxyWidget()
end_save_button = QtWidgets.QPushButton('Stop storage')
end_save_button.setStyleSheet(style)
end_save_button.clicked.connect(data_base.stop)
proxy2.setWidget(end_save_button)

# Pressure Graph
# Temperature graph
temperature = graph_temperature()
# Time graph

## Setting the graphs in the layout
# Title at top
text = """
Flight monitoring interface for cansats and OBC's <br>
developed at the Universidad Distrital FJC.
"""
Layout.addLabel(text, col=1, colspan=21)
Layout.nextRow()

# Put vertical label on left side
Layout.addLabel('LIDER - ATL research hotbed',
                angle=-90, rowspan=3)

Layout.nextRow()

lb = Layout.addLayout(colspan=21)
lb.addItem(proxy)
lb.nextCol()
lb.addItem(proxy2)

Layout.nextRow()

l1 = Layout.addLayout(colspan=20, rowspan=2)
l11 = l1.addLayout(rowspan=1, border=(83, 83, 83))

# Altitude, speed
l11.addItem(temperature)
l11.addItem(temperature)
l1.nextRow()
# l1.nextRow()
# l11.addItem(temperature)

# Acceleration, gyro, pressure, temperature
# l12 = l1.addLayout(rowspan=1, border=(83, 83, 83))
# l12.addItem(temperature)

# Time, battery and free fall graphs
l2 = Layout.addLayout(border=(83, 83, 83))
l2.nextRow()


# you have to put the position of the CSV stored in the value_chain list
# that represent the date you want to visualize
def update():
    try:
        value_chain = []
        value_chain = ser.getData()
        print(type(value_chain))
        # pressure.update(value_chain)
        temperature.update(value_chain)
        # print(value_chain)
        # data_base.guardar(value_chain)
    except IndexError:
        print('starting, please wait a moment')


if (ser.isOpen()):
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(500)
else:
    print("something is wrong with the update call")
# Start Qt event loop unless running in interactive mode.

if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()

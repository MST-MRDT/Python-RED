# Basic proto for Qt5 style Gui

import struct
import sys
import time

from PyQt5 import QtWidgets, QtCore, QtGui # Todo, add requirements.txt
from threading import Thread

from RoveComm2 import RoveComm # Todo, add submodule

# =======================================================================
# XBox controller stuff.

total_reads = 10
xbox_values = range(total_reads)

def xbox_generator():
    for value in xbox_values:
        time.sleep(1)
        yield value

# =======================================================================
# RoveComm stuff. Should be its own file later.
board_id = 1
RoveComm = RoveComm(board_id)
data_id = 7

def xbox_listener(callback_fn):
    # reads from xbox controller
    for val in xbox_generator():
        # update GUI
        # call function to do rovecomm stuff
        data_tx = struct.pack("H", val)
        RoveComm.sendTo(127, 0, 0, 1, data_id, data_tx)
        callback_fn("Val is: %s" % val)

def rovecomm_listener():
    for val in range(total_reads):
        print(RoveComm.recieveFrom())
        time.sleep(1)

# ========================================================================
# PyQt stuff.

class MyQThread(QtCore.QThread):
    def __init__(self, thread_fn):
        QtCore.QThread.__init__(self)
        self.thread_fn = thread_fn

    def __del__(self):
        self.wait()

    def run(self):
        self.thread_fn()


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(500, 300)

        self.label = QtWidgets.QLabel()
        self.label.resize(500, 300)
        self.label.setText("No text set.")

        centralWidget = QtWidgets.QWidget(self)
        mainLayout = QtWidgets.QVBoxLayout(centralWidget)
        mainLayout.addWidget(self.label)

        self.xbox_listener = MyQThread(lambda: xbox_listener(self.update_label))
        self.rovecomm_listener = MyQThread(rovecomm_listener)
        self.xbox_listener.start()
        self.rovecomm_listener.start()

    def update_label(self, new_label):
        self.label.setText(new_label)


def main():
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

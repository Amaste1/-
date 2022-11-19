import sys

from PyQt5 import QtGui, QtWidgets

from gameFunction import gameSet


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = gameSet()
    mainWindow.show()
    sys.exit(app.exec())
import sys
from PyQt5.QtWidgets import QApplication

from mainwindow import MainWindow

app=QApplication(sys.argv)
mainWindow=MainWindow()
mainWindow.show()
app.exec()



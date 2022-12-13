from PyQt5.QtWidgets import QApplication,QLabel,QPushButton
from interfaz.mainGrafica import MainWindow
import sys,pickle
from Modulos.clases import Provincia,Municipio,Pais
from Modulos.verificador import ids_municipios

with open('archivo.pickle','rb') as arch:
    arg = pickle.load(arch)

app = QApplication(sys.argv)
mainWindow = MainWindow(arg)

mainWindow.show()
app.exec()

arg.save()


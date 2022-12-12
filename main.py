from PyQt5.QtWidgets import QApplication,QLabel,QPushButton
from interfaz.mainGrafica import MainWindow
import sys,pickle
from Modulos.clases import Provincia,Municipio


with open('archivo.pickle','rb') as arch:
    arg = pickle.load(arch)

app = QApplication(sys.argv)
mainWindow = MainWindow()

lista = list(arg.provincias)


for i in lista:

    prov = QPushButton()
    prov.setText(i.nombre)

    
    prov.clicked.connect(lambda checked ,arg = i:mainWindow.seleccionar_provincia(arg))
    mainWindow.provincias.addWidget(prov)


mainWindow.show()
app.exec()

arg.save()
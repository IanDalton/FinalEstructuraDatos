from PyQt5.QtWidgets import QApplication,QLabel,QPushButton
from interfaz.mainGrafica import MainWindow
import sys,pickle
from Modulos.clases import Provincia,Municipio,Pais
from Modulos.verificador import ids_municipios
try:
    with open('archivo.pickle','rb') as arch:
        arg = pickle.load(arch)
except FileNotFoundError:
    print('Se esta generando los nuevos datos')
    arg = Pais('Argentina')
    for key,item in ids_municipios.items():
        Provincia(key,arg,item[1])

arg.dispositivos = set()

app = QApplication(sys.argv)
mainWindow = MainWindow(arg)

mainWindow.show()
app.exec()

arg.save()

   
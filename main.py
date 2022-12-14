from PyQt5.QtWidgets import QApplication,QLabel,QPushButton
from interfaz.mainGrafica import MainWindow
import sys,pickle,ctypes
from Modulos.clases import Provincia,Municipio,Pais
from Modulos.verificador import ids_municipios

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('bandaloschinos.paisdigital.v1')

try:
    with open('archivo.pickle','rb') as arch:
        arg = pickle.load(arch)
except FileNotFoundError:
    print('Se esta generando los nuevos datos')
    arg = Pais('Argentina')
    for key,item in ids_municipios.items():
        Provincia(key,arg,item[1])


app = QApplication(sys.argv)
mainWindow = MainWindow(arg)


mainWindow.show()
app.exec()

arg.save()

   
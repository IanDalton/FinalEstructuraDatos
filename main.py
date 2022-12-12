from PyQt5.QtWidgets import QApplication,QLabel,QPushButton
from interfaz.mainGrafica import MainWindow
import sys,pickle
from Modulos.clases import Provincia,Municipio
with open('archivo.pickle','rb') as arch:
    arg = pickle.load(arch)

app = QApplication(sys.argv)
mainWindow = MainWindow()




for provincia in arg.provincias:

    prov = QPushButton()
    prov.setText(provincia.nombre)
    prov.clicked.connect(lambda: mainWindow.seleccionar_provincia(provincia))
    prov.setStyleSheet('border:1px solid black;')
    mainWindow.provincias.addWidget(prov)



mainWindow.show()
app.exec()

arg.save()
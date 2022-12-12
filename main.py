from PyQt5.QtWidgets import QApplication,QLabel
from interfaz.mainGrafica import MainWindow
import sys,pickle

with open('archivo.pickle','rb') as arch:
    arg = pickle.load(arch)

app = QApplication(sys.argv)
mainWindow = MainWindow()

for provincia in arg.provincias:
    for muni in provincia.municipios:
        lbl = QLabel()
        lbl.setText(muni.nombre)
        lbl.setStyleSheet('border:1px solid black;')
        mainWindow.municipios.addWidget(lbl)
    prov = QLabel()
    prov.setText(provincia.nombre)
    prov.setStyleSheet('border:1px solid black;')
    mainWindow.provincias.addWidget(prov)


mainWindow.show()
app.exec()

arg.save()
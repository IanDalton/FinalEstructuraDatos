
from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow): #defino la ventana

   def botonCambiarTitulo_click(self):
      nuevoTitulo = self.campoTextoNombreVentana.toPlainText()
      self.setWindowTitle(nuevoTitulo)
      self.campoTextoNombreVentana.clear()

   def __init__(self):
      super().__init__()
      self.setWindowTitle("Sistema de informacion - RED WIFI PAIS DIGITAL")
      self.setGeometry(500,500,1000,700) #posicion y tamaño inicial de la ventana 
      #Layout que dispone los elementos verticalmente -- uno abajo del otro
#QHBoxLayout() -- al costado
      layoutPrincipal = QVBoxLayout()


#Creo un label y lo agrego al layout
      labelSaludo = QLabel("Bienvenidos")
      layoutPrincipal.addWidget(labelSaludo)

      layoutCambioDeNombre = QHBoxLayout()
      layoutCambioDeNombre.addWidget(QLabel("Ingrese el nuevo nombre de la ventana: "))
      self.campoTextoNombreVentana = QTextEdit()
      self.campoTextoNombreVentana.textChanged.connect(self.campoTextoNombreVentana_textChanged)
      layoutCambioDeNombre.addWidget(self.campoTextoNombreVentana)

      layoutPrincipal.addLayout(layoutCambioDeNombre)

      self.botonCambiarTitulo = QPushButton()
      self.botonCambiarTitulo.setText("Cambiar titulo de la ventana")
      self.botonCambiarTitulo.setEnabled(False)
      self.botonCambiarTitulo.clicked.connect(self.botonCambiarTitulo_click)
      layoutPrincipal.addWidget(self.botonCambiarTitulo)

#El widget que contiene al layout es el widget principal de la ventana, para mostrarlo
      widgetLayout = QWidget()
      widgetLayout.setLayout(layoutPrincipal)
      self.setCentralWidget(widgetLayout)


   def campoTextoNombreVentana_textChanged(self):
      texto = self.campoTextoNombreVentana.toPlainText()
      if len(texto) == 0:
         self.botonCambiarTitulo.setEnabled(False)
      else:
         self.botonCambiarTitulo.setEnabled(True)




app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
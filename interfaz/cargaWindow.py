from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle
from PyQt5.QtWidgets import QMessageBox
import pickle 
from .erroresWindow import ErroresWindow
from Modulos.clases import * 


class CargaWindow(QMainWindow):
      def __init__(self,pais:Pais):
            super().__init__()
            self.setWindowTitle("CARGA DE ARCHIVOS")
            self.setGeometry(1300,200,300,100)
            layoutPrincipal = QVBoxLayout()
            self.pais=pais
            self.es_municipio=True
            eleccion = QLabel()
            eleccion.setText("Que tipo de datos va a ingresar?")
            layoutPrincipal.addWidget(eleccion)
            contenido = QHBoxLayout()
            self.router = QPushButton(text="Routers")
            self.router.clicked.connect(self.cambiar_seleccion)
            contenido.addWidget(self.router)
            self.municipio = QPushButton(text= "Municipios")
            self.municipio.setEnabled(False)
            self.municipio.clicked.connect(self.cambiar_seleccion)
            contenido.addWidget(self.municipio)
            layoutPrincipal.addLayout(contenido)

            link = QHBoxLayout()
            text_link = QLabel(text="Link a archivo: ")
            link.addWidget(text_link)
            self.ingresar_link = QTextEdit()
            link.addWidget(self.ingresar_link)
            layoutPrincipal.addLayout(link)


            confirmacion = QPushButton(text="Confirmar datos")
            layoutPrincipal.addWidget(confirmacion)
            confirmacion.clicked.connect(self.cargarDatos_click)
            
            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)
      
      def cambiar_seleccion(self):
            if self.es_municipio:
                  self.router.setEnabled(False)
                  self.municipio.setEnabled(True)
            else:
                  self.router.setEnabled(True)
                  self.municipio.setEnabled(False)
            self.es_municipio = not self.es_municipio
            pass

      def cargarDatos_click(self):
            if self.es_municipio:
                  errores = self.pais.load_data(self.ingresar_link.toPlainText(),"Municipio")
            else:
                  errores =self.pais.load_data(self.ingresar_link.toPlainText(),"Router")
            if len(errores) > 0:
                  print('hay errores') 
                  self.ventanaErrores = ErroresWindow(self.es_municipio,errores,self.pais)
                  self.ventanaErrores.show()
                  self.close()



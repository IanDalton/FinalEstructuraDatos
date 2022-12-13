from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle
from PyQt5.QtWidgets import QMessageBox
import pickle 
from Modulos.clases import * 


class CargaWindow(QMainWindow):
      def __init__(self):
            super().__init__()
            self.setWindowTitle("CARGA DE ARCHIVOS")
            self.setGeometry(1300,200,300,100)
            layoutPrincipal = QVBoxLayout()

            eleccion = QLabel()
            eleccion.setText("Que tipo de datos va a ingresar?")
            layoutPrincipal.addWidget(eleccion)
            contenido = QHBoxLayout()
            self.router = QPushButton(text="Routers")
            contenido.addWidget(self.router)
            self.municipio = QPushButton(text= "Municipios")
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
      
      def cargarDatos_click(self,pais:Pais):
            if self.municipio.clicked:
                  pais.load_data(self.ingresar_link,"Municipio")
            elif self.router.clicked:
                  pais.load_data(self.ingresar_link,"Router")

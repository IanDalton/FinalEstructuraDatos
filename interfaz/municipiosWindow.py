from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle
from Modulos.clases import *

class MunicipiosWindow(QMainWindow):
      def __init__(self,provincia:Provincia):
            super().__init__()
            self.setWindowTitle("INSERTAR MUNICIPIO")
            self.setGeometry(1350,400,300,50)
            self.provincia = provincia
            
            layoutPrincipal = QVBoxLayout()

            id = QHBoxLayout()
            nombre = QHBoxLayout()
            ids = QLabel(text="Id de municipio: ")
            self.id_ingresado = QTextEdit()
            nombres = QLabel(text="Nombre de municipio: ")
            self.nombre_ingresado = QTextEdit()
            id.addWidget(ids)
            id.addWidget(self.id_ingresado)
            nombre.addWidget(nombres)
            nombre.addWidget(self.nombre_ingresado)
            layoutPrincipal.addLayout(id)
            layoutPrincipal.addLayout(nombre)

            confirmar = QPushButton(text="Confirmar datos")
            layoutPrincipal.addWidget(confirmar)

            confirmar.clicked.connect(self.generarMunicipio)

            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)
      
      def generarMunicipio(self):  
            Municipio(self.id_ingresado.toPlainText(),self.nombre_ingresado.toPlainText(),self.provincia)
            self.close()

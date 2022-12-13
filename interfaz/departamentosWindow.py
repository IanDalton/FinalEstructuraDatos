from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle
from Modulos.clases import *


class DepartamentosWindow(QMainWindow):
      def __init__(self,municipio:Municipio):
            super().__init__()
            self.setWindowTitle("INSERTAR DEPARTAMENTO")
            self.setGeometry(1300,200,300,100)
            self.municipio = municipio

            layoutPrincipal = QVBoxLayout()

            id = QHBoxLayout()
            nombre = QHBoxLayout()
            ids = QLabel(text="Id de departamento: ")
            self.id_ingresado = QTextEdit()
            nombres = QLabel(text="Nombre de departamento: ")
            self.nombre_ingresado = QTextEdit()
            id.addWidget(ids)
            id.addWidget(self.id_ingresado)
            nombre.addWidget(nombres)
            nombre.addWidget(self.nombre_ingresado)
            layoutPrincipal.addLayout(id)
            layoutPrincipal.addLayout(nombre)

            confirmar = QPushButton(text="Confirmar datos")
            layoutPrincipal.addWidget(confirmar)

            confirmar.clicked.connect(self.generarDepartamento)

            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)
      
      def generarDepartamento(self):  
            Departamento(self.id_ingresado.toPlainText(),self.nombre_ingresado.toPlainText(),self.municipio)
            self.close()

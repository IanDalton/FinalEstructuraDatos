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
            
            layoutPrincipal = QVBoxLayout()

            id = QHBoxLayout()
            nombre = QHBoxLayout()
            ids = QLabel(text="Id de municipio: ")
            id_ingresado = QTextEdit()
            nombres = QLabel(text="Nombre de municipio: ")
            nombre_ingresado = QTextEdit()
            id.addWidget(ids)
            id.addWidget(id_ingresado)
            nombre.addWidget(nombres)
            nombre.addWidget(nombre_ingresado)
            layoutPrincipal.addLayout(id)
            layoutPrincipal.addLayout(nombre)

            confirmar = QPushButton(text="Confirmar datos")
            layoutPrincipal.addWidget(confirmar)


            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)

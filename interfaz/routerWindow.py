from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle
from Modulos.clases import *

class RouterWindow(QMainWindow): 
      def __init__(self,departamento:Departamento,pais:Pais):
            super().__init__()
            self.setWindowTitle("INSERTAR ROUTER")
            self.setGeometry(1400,300,300,100)
            self.departamento = departamento
            self.pais = pais

            layoutPrincipal = QVBoxLayout()

            id = QHBoxLayout()
            identificador = QHBoxLayout()
            ubicacion = QHBoxLayout()
            latitud = QHBoxLayout()
            longitud = QHBoxLayout()
            pais = QHBoxLayout()

            ids = QLabel(text="Id de router: ")
            font = ids.font()
            font.setBold(True)
            ids.setFont(font)

            self.setFont(font)
            self.id_ingresado = QTextEdit()

            identificadores = QLabel(text="Identificador del router: ")
            self.identificador_ingresado = QTextEdit()

            ubicaciones = QLabel(text="Ubicacion de router: ")
            self.ubicacion_ingresada = QTextEdit()

            latitudes = QLabel(text="Latitud de router: ")
            self.latitud_ingresada = QTextEdit()

            longitudes = QLabel(text="Longitud de router: ")
            self.longitud_ingresada = QTextEdit()
            
            id.addWidget(ids)
            id.addWidget(self.id_ingresado)
            identificador.addWidget(identificadores)
            identificador.addWidget(self.identificador_ingresado)
            ubicacion.addWidget(ubicaciones)
            ubicacion.addWidget(self.ubicacion_ingresada)
            latitud.addWidget(latitudes)
            latitud.addWidget(self.latitud_ingresada)
            longitud.addWidget(longitudes)
            longitud.addWidget(self.longitud_ingresada)

            layoutPrincipal.addLayout(id)
            layoutPrincipal.addLayout(identificador)
            layoutPrincipal.addLayout(ubicacion)
            layoutPrincipal.addLayout(latitud)
            layoutPrincipal.addLayout(longitud)

            confirmar = QPushButton(text="Confirmar datos")
            layoutPrincipal.addWidget(confirmar)

            confirmar.clicked.connect(self.generarRouter)

            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)
      
      def generarRouter(self):  
            Router(self.id_ingresado.toPlainText(),self.identificador_ingresado.toPlainText(),
            self.ubicacion_ingresada.toPlainText(),self.latitud_ingresada.toPlainText(),
            self.longitud_ingresada.toPlainText(),self.pais,self.departamento)
            self.close()


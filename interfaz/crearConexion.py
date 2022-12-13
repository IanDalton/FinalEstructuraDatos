from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle
from Modulos.clases import *

class CrearConexion(QMainWindow):
      def __init__(self,pais:Pais,router:Router):
            super().__init__()
            self.setWindowTitle('Registrar Conexion')
            self.setGeometry(1350,400,300,100)
            layoutPrincipal = QVBoxLayout()

            opciones = QComboBox()
            opciones.addItems(['Seleccionar un dispositivo existente','Crear un nuevo dispositivo'])
            disclaimer = QLabel(text="Ingrese los datos para completar la conexion: ")
            layoutPrincipal.addWidget(disclaimer)
            dispositivos = QVBoxLayout()
            for dispo in pais.dispositivos:
                  btn = QPushButton()
                  btn.setText(dispo.mac)

                  dispositivos.addWidget(btn)

            
            
            
            layoutPrincipal.addLayout(dispositivos)

            self.alta = QFormLayout()
            self.datetime_edit = QDateTimeEdit(self, calendarPopup=True)
            self.datetime_edit.dateTimeChanged.connect(self.update)
            self.alta.addRow('Alta:', self.datetime_edit)
            layoutPrincipal.addLayout(self.alta)

            confirmacion = QPushButton(text="Confirmar datos")
            layoutPrincipal.addWidget(confirmacion)
            confirmacion.clicked.connect(self.generarConexion_click)

            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)
      pass
      def seleccionar_dispo(self):
            pass
      def cargarDatos(self):
            pass
      def generarConexion_click(self):
            pass

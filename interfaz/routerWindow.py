from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle

class RouterWindow(QMainWindow): 
      def __init__(self):
            super().__init__()
            self.setWindowTitle("INSERTAR ROUTER")
            self.setGeometry(1400,300,300,100)

            layoutPrincipal = QVBoxLayout()

            id = QHBoxLayout()
            identificador = QHBoxLayout()
            ubicacion = QHBoxLayout()
            latitud = QHBoxLayout()
            longitud = QHBoxLayout()
            pais = QHBoxLayout()

            ids = QLabel(text="Id de router: ")
            id_ingresado = QTextEdit()

            identificadores = QLabel(text="Nombre de router: ")
            identificador_ingresado = QTextEdit()

            ubicaciones = QLabel(text="Ubicacion de router: ")
            ubicacion_ingresada = QTextEdit()

            latitudes = QLabel(text="Latitud de router: ")
            latitud_ingresada = QTextEdit()

            longitudes = QLabel(text="Longitud de router: ")
            longitud_ingresada = QTextEdit()
            
            id.addWidget(ids)
            id.addWidget(id_ingresado)
            identificador.addWidget(identificadores)
            identificador.addWidget(identificador_ingresado)
            ubicacion.addWidget(ubicaciones)
            ubicacion.addWidget(ubicacion_ingresada)
            latitud.addWidget(latitudes)
            latitud.addWidget(latitud_ingresada)
            longitud.addWidget(longitudes)
            longitud.addWidget(longitud_ingresada)

            layoutPrincipal.addLayout(id)
            layoutPrincipal.addLayout(identificador)
            layoutPrincipal.addLayout(ubicacion)
            layoutPrincipal.addLayout(latitud)
            layoutPrincipal.addLayout(longitud)

            confirmar = QPushButton(text="Confirmar datos")
            layoutPrincipal.addWidget(confirmar)


            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)

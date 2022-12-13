from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle


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
            router = QPushButton(text="Routers")
            contenido.addWidget(router)
            municipio = QPushButton(text= "Municipios")
            contenido.addWidget(municipio)
            layoutPrincipal.addLayout(contenido)

            link = QHBoxLayout()
            text_link = QLabel(text="Link a archivo: ")
            link.addWidget(text_link)
            ingresar_link = QTextEdit()
            link.addWidget(ingresar_link)
            layoutPrincipal.addLayout(link)

            confirmacion = QPushButton(text="Confirmar datos")
            layoutPrincipal.addWidget(confirmacion)
            confirmacion.clicked.connect(self.cargarDatos_click)
            
            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)
      
      def cargarDatos_click():
            pass

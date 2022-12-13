from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from Modulos.clases import Pais

class ErroresWindow(QMainWindow): 
    def __init__(self,es_municipio,errores,pais:Pais):
        super().__init__()
        self.pais = pais
        self.setWindowTitle('MANEJO DE ERRORES')
        self.setGeometry(1350,400,300,100)
        self.se_almacena = True
        self.es_municipio = es_municipio
        self.errores = errores

        layoutPrincipal = QVBoxLayout()

        aviso = QLabel(text=f"En la carga se encontraron {len(self.errores)} errores. Como desea manejarlos?")
        layoutPrincipal.addWidget(aviso)

        opciones = QHBoxLayout()

        self.eliminar = QPushButton(text="Eliminar los registros")
        self.eliminar.clicked.connect(self.cambiar_seleccion)

        self.cargar = QPushButton(text="Almacenar los registros en archivo")
        self.cargar.clicked.connect(self.cambiar_seleccion)
        self.cargar.setEnabled(False)

        opciones.addWidget(self.eliminar)
        opciones.addWidget(self.cargar)
        layoutPrincipal.addLayout(opciones)

        confirmar = QPushButton(text="Confirmar selección")
        layoutPrincipal.addWidget(confirmar)
        confirmar.clicked.connect(self.ejecutarSeleccion_click)

        widgetLayout = QWidget()
        widgetLayout.setLayout(layoutPrincipal)
        self.setCentralWidget(widgetLayout)

    def cambiar_seleccion(self):
        if self.se_almacena:
            self.eliminar.setEnabled(False)
            self.cargar.setEnabled(True)
        else:
            self.eliminar.setEnabled(True)
            self.cargar.setEnabled(False)
        self.se_almacena = not self.se_almacena
        pass

    def ejecutarSeleccion_click(self):
        if self.se_almacena:
            if self.es_municipio:
                self.pais.save_error(self.errores,'Municipios')
            else:
                self.pais.save_error(self.errores,'Routers')
        else:
            pass
        self.close()


    
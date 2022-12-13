from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle
from Modulos.clases import *

class CrearConexion(QMainWindow):
      def __init__(self,pais:Pais,router:Router):
            super().__init__()
            self.pais = pais
            self.router = router
            self.setWindowTitle('Registrar Conexion')
            self.setGeometry(1350,400,300,100)


            layoutPrincipal = QVBoxLayout()
            modo = QHBoxLayout()
            modo.addWidget(QLabel(text='Seleccionar un dispositivo existente'))
            modo.setAlignment(Qt.AlignTop)
            self.opciones = AnimatedToggle()
            self.opciones.toggled.connect(lambda selected:self.seleccionar_dispo() if not self.opciones.isChecked() else self.crear_dispo())
            modo.addWidget(self.opciones)
            modo.addWidget(QLabel(text='Crear un nuevo dispositivo'))

            layoutPrincipal.addLayout(modo)
            

            self.contenido = QHBoxLayout()

            self.contenido.setAlignment(Qt.AlignTop)
            
            self.seleccionar_dispo()
            




            self.confirmacion = QPushButton(text="Confirmar datos")
            layoutPrincipal.addLayout(self.contenido)
            layoutPrincipal.addWidget(self.confirmacion)
            
            self.confirmacion.clicked.connect(self.generarConexion_click)

            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)
      pass
      def clear(self):
            for i in reversed(range(self.contenido.count())):
                  self.contenido.itemAt(i).widget().setParent(None)
      def seleccionar_dispo(self):
            self.clear()
            self.dispositivos = QComboBox()
            self.dispositivos.addItem('Seleccionar un dispositivo...')
            for dispo in self.pais.dispositivos:
                  self.dispositivos.addItem(dispo.mac)
            self.contenido.addWidget(self.dispositivos)
            self.dispositivos.currentIndexChanged.connect(lambda:self.confirmacion.setEnabled(False) if self.dispositivos.currentIndex()==0 else self.confirmacion.setEnabled(True) )
            pass
      def crear_dispo(self):
            self.clear()
            self.contenido.addWidget(QLabel(text='MAC del dispositivo:'))
            self.mac = QTextEdit()
            self.contenido.addWidget(self.mac)
            self.mac.textChanged.connect(lambda: self.confirmacion.setEnabled(False) if self.mac.toPlainText() in self.pais.dispositivos else self.confirmacion.setEnabled(True))
            print('crear')
            pass

      def generarConexion_click(self):
            if self.opciones.isChecked(): # Se esta creando un nuevo dispositivo
                  dispo = Dispositivo(self.mac.toPlainText(),self.pais)
                  dispo.conectar(self.router)
                  
            else:
                  dispo = list(self.pais.dispositivos)[self.dispositivos.currentIndex()-1]
                  dispo.conectar(self.router)
            self.close()

            pass
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle
from Modulos.clases import *

class CrearConexion(QMainWindow):
      def __init__(self,pais:Pais,router:Router,refresh):
            super().__init__()
            self.pais = pais
            self.router = router
            self.refresh = refresh
            self.setWindowTitle('Registrar Conexion')
            
            self.setGeometry(1350,400,300,100)


            layoutPrincipal = QVBoxLayout()
            modo = QHBoxLayout()
            texto = QLabel(text='Seleccionar un dispositivo existente')
            modo.addWidget(texto)

            font = texto.font()
            font.setBold(True)
            texto.setFont(font)
            self.setFont(font)

            modo.setAlignment(Qt.AlignTop)
            self.opciones = AnimatedToggle(checked_color="#843511",pulse_checked_color="#843511")

            self.opciones.toggled.connect(lambda selected:self.seleccionar_dispo() if not self.opciones.isChecked() else self.crear_dispo())
            modo.addWidget(self.opciones)
            creacion = QLabel(text='Crear un nuevo dispositivo')
            modo.addWidget(creacion)
            creacion.setFont(font)

            layoutPrincipal.addLayout(modo)
            

            self.contenido = QHBoxLayout()

            self.contenido.setAlignment(Qt.AlignTop)
            
            self.seleccionar_dispo()
            




            self.confirmacion = QPushButton(text="Confirmar datos")
            self.confirmacion.setEnabled(False)
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
            for dispo in self.pais.dispositivos.values():
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
                  data = self.dispositivos.itemText(self.dispositivos.currentIndex())
                  dispo = self.pais.dispositivos.get(data)
                  dispo.conectar(self.router)
            self.refresh()
            self.close()

            pass

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog,QMessageBox,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle
from PyQt5.QtWidgets import QMessageBox
from .erroresWindow import ErroresWindow
from Modulos.clases import * 


class CargaWindow(QMainWindow):
      def __init__(self,pais:Pais,refresh):
            self.refresh = refresh
            super().__init__()
            self.setWindowTitle("CARGA DE ARCHIVOS")
            self.setGeometry(1300,200,300,100)
            layoutPrincipal = QVBoxLayout()
            self.pais=pais
            self.es_municipio=True
            eleccion = QLabel()
            eleccion.setText("Que tipo de datos va a ingresar?")
            font = eleccion.font()
            font.setBold(True)
            eleccion.setFont(font)
            layoutPrincipal.addWidget(eleccion)
            contenido = QHBoxLayout()

            self.router = QPushButton(text="Routers")
            self.router.setStyleSheet('QPushButton {background-color: #843511; color: white}')
            self.router.setFont(font)
            self.router.clicked.connect(self.cambiar_seleccion)
            contenido.addWidget(self.router)

            self.municipio = QPushButton(text= "Municipios")
            self.municipio.setStyleSheet('QPushButton {background-color: #843511; color: white}')
            self.municipio.setFont(font)
            self.municipio.clicked.connect(self.cambiar_seleccion)
            contenido.addWidget(self.municipio)
            layoutPrincipal.addLayout(contenido)

            

            link = QHBoxLayout()
            text_link = QLabel(text="Link a archivo: ")
            text_link.setFont(font)
            link.addWidget(text_link)
            btn = QPushButton(text='Cargar archivo')
            btn.clicked.connect(self.open)
            self.ingresar_link = QLabel()
            link.addWidget(self.ingresar_link)
            link.addWidget(btn)
            layoutPrincipal.addLayout(link)
            


            self.confirmacion = QPushButton(text="Confirmar datos")
            self.confirmacion.setStyleSheet('QPushButton {background-color: #FFFFFF; color: black}')
            self.confirmacion.setFont(font)
            layoutPrincipal.addWidget(self.confirmacion)
            self.confirmacion.clicked.connect(self.cargarDatos_click)
            self.confirmacion.setEnabled(False)

            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)
      
      def open(self):
            fileName = QFileDialog.getOpenFileName(self, 'OpenFile')
            self.ingresar_link.setText(fileName[0])
            self.confirmacion.setEnabled(True)


      def cambiar_seleccion(self):
            if self.es_municipio:
                  self.router.setEnabled(False)
                  self.municipio.setEnabled(True)
                  
                  self.router.setStyleSheet('QPushButton {background-color: #FCBF49; color: black}')
                  self.municipio.setStyleSheet('QPushButton {background-color: #843511; color: white}')
            else:
                  self.router.setEnabled(True)
                  self.municipio.setEnabled(False)
                  
                  self.municipio.setStyleSheet('QPushButton {background-color: #FCBF49; color: black}')
                  self.router.setStyleSheet('QPushButton {background-color: #843511; color: white}')
            self.es_municipio = not self.es_municipio
            pass

      def cargarDatos_click(self):
            try:
                  with open(self.ingresar_link.text(),'r') as arch:
                        csv.DictReader(arch)
                  if self.es_municipio:
                        errores = self.pais.load_data(self.ingresar_link.text(),"Municipio")
                  else:
                        errores =self.pais.load_data(self.ingresar_link.text(),"Router")
                  if len(errores) > 0:
                        self.ventanaErrores = ErroresWindow(self.es_municipio,errores,self.pais)
                        self.ventanaErrores.show()
                        self.refresh()
                        self.close()
            except:
                  msg = QMessageBox()
                  msg.setIcon(QMessageBox.Warning)
                  msg.setText("El archivo no tiene el formato correcto")
                  msg.setWindowTitle("Error formato archivo")
                  msg.setDetailedText("Tiene que ser un archivo del formato CSV")
                  msg.setStandardButtons(QMessageBox.Ok)
                  msg.exec()



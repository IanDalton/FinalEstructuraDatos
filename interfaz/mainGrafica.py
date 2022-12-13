from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle
from Modulos.clases import *

import pickle

import sys
""" 
dark_theme = QPalette()
dark_theme.setColor(QPalette.Window, QColor(53, 53, 53)
dark_theme.setColor(QPalette.WindowText, Qt.white)
dark_theme.setColor(QPalette.Base, QColor(25, 25, 25))
dark_theme.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_theme.setColor(QPalette.ToolTipBase, Qt.black)
dark_theme.setColor(QPalette.ToolTipText, Qt.white)
dark_theme.setColor(QPalette.Text, Qt.white)
dark_theme.setColor(QPalette.Button, QColor(53, 53, 53))
dark_theme.setColor(QPalette.ButtonText, Qt.white)
dark_theme.setColor(QPalette.BrightText, Qt.red)
dark_theme.setColor(QPalette.Link, QColor(42, 130, 218))
dark_theme.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_theme.setColor(QPalette.HighlightedText, Qt.black)

 """


class MainWindow(QMainWindow): 
      def __init__(self):
            super().__init__()
            self.setWindowTitle("Sistema de informacion - RED WIFI PAIS DIGITAL")
            self.setGeometry(200,200,1000,700)
            layoutPrincipal = QVBoxLayout()
            
            menu = QHBoxLayout()
            contenido = QHBoxLayout()
            
            cargarArchivos = QPushButton()      
            nuevaConexion = QPushButton() 
            preferencias = QPushButton()
            cargarArchivos.setText('Cargar archivos')  #arrastra el archivo
            cargarArchivos.clicked.connect(self.abrirVentanaCarga_click)
            nuevaConexion.setText('Nueva conexion')
            nuevaConexion.clicked.connect(self.abrirVentanaConexion_click)
            preferencias.setText('Preferencias')
            preferencias.setStyleSheet('background-color: darkGrey')
            menu.addWidget(cargarArchivos)
            menu.addWidget(nuevaConexion)
            menu.addWidget(preferencias,2)
            
            layoutPrincipal.addLayout(menu)
            
            layoutPrincipal.addLayout(contenido,2)

            self.provincias = QVBoxLayout()
            """  for provincia in arg.provincias:
                  prov = QLabel()
                  prov.setText(provincia.nombre)
                  provincias.addWidget(prov) """
                  

            contenido.addLayout(self.provincias)
            self.municipios = QVBoxLayout()
            contenido.addLayout(self.municipios)
            self.agregarMunicipios = QPushButton()
            self.agregarMunicipios.setText('Municipio nuevo')
            self.municipios.addWidget(self.agregarMunicipios)
            self.departamentos = QVBoxLayout()
            contenido.addLayout(self.departamentos)
            agregarDepartamentos = QPushButton()
            self.departamentos.addWidget(agregarDepartamentos)
            self.routers = QComboBox()
            self.routers.addItems(["Opción 1", "Opción 2", "Opción 3"])

            """ 
            dispositivos = QVBoxLayout()
            routers.addLayout(dispositivos)
            activable = QHBoxLayout()
            texto1 = QLabel() 
            texto1.setText('Activar')
            activable.addWidget(texto1)
            toggle = AnimatedToggle(checked_color="#FFB000",pulse_checked_color="#44FFB000")
            activable.addWidget(toggle)
            texto2 = QLabel() 
            texto2.setText('Desactivar')
            activable.addWidget(texto2)
            routers.addLayout(activable) """

      #El widget que contiene al layout es el widget principal de la ventana, para mostrarlo
            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)

      
      def limpiar(self,sector:QHBoxLayout):
            print(sector.count())
            try:
                  i=max(range(sector.count()))
                  while i > 0 :
                        sector.itemAt(i).widget().setParent(None)
                        i-=1
            except ValueError:
                  pass
            except AttributeError:
                  pass
      def seleccionar_provincia(self,prov):
            self.limpiar(self.municipios)
            self.limpiar(self.departamentos)
            self.limpiar(self.routers)
            for muni in prov.municipios:
                  lbl = QPushButton()
                  lbl.setText(muni.nombre)
                  lbl.setStyleSheet('border:1px solid black;')
                  lbl.clicked.connect(lambda checked,mun = muni:self.seleccionar_municipio(mun))
                  self.municipios.addWidget(lbl)
      def seleccionar_municipio(self,muni):
            self.limpiar(self.departamentos)
            self.limpiar(self.routers)
            for depto in muni.departamentos:
                  lbl = QPushButton()
                  lbl.setText(depto.nombre)
                  lbl.setStyleSheet('border:1px solid black;')
                  lbl.clicked.connect(lambda checked,dpto = depto:self.seleccionar_departamento(dpto))
                  self.departamentos.addWidget(lbl)
      def seleccionar_departamento(self,depto):
            self.limpiar(self.routers)
            for router in depto.routers:
                  lbl = QPushButton()
                  lbl.setText(str(router))
                  lbl.setStyleSheet('border:1px solid black;')
                  lbl.clicked.connect(lambda checked,rtr = router:self.seleccionar_router(rtr))
                  self.routers.addWidget(lbl)
            pass
      def seleccionar_router(self,router):
            print(router.id)
            pass

      def abrirVentanaCarga_click(self):
            self.cargando_datos = CargaWindow()
            self.cargando_datos.show()

      def abrirVentanaConexion_click(self):
            self.estableciendo_conexion = ConexionWindow()
            self.estableciendo_conexion.show()
            

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


class ConexionWindow(QMainWindow):
      def __init__(self):
            super().__init__()
            self.setWindowTitle("NUEVA CONEXION")
            self.setGeometry(1350,400,300,100)
            layoutPrincipal = QVBoxLayout()

            disclaimer = QLabel(text="Ingrese los datos para completar la conexion: ")
            layoutPrincipal.addWidget(disclaimer)

            dispositivo = QHBoxLayout()
            dispositivo_text = QLabel(text="Dispositivo: ")
            self.dispositivo_box = QTextEdit()
            dispositivo.addWidget(dispositivo_text)
            dispositivo.addWidget(self.dispositivo_box)
            layoutPrincipal.addLayout(dispositivo)

            self.alta = QFormLayout()
            self.datetime_edit = QDateTimeEdit(self, calendarPopup=True)
            self.datetime_edit.dateTimeChanged.connect(self.update)
            self.alta.addRow('Alta:', self.datetime_edit)
            layoutPrincipal.addLayout(self.alta)

            confirmacion = QPushButton(text="Confirmar datos")
            layoutPrincipal.addWidget(confirmacion)
            #confirmacion.clicked.connect(self.generarConexion_click)

            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)
      
      # def generarConexion_click(self):
      #       conexion = Conexion(self.dispositivo_box,Router.generar_ip,self.alta) #FALTA EL ROUTER QUE LO ELIGE EL USUARIO 

class FechaWindow(QMainWindow): 
      def __init__(self):
            super().__init__()
            self.setWindowTitle("CONEXIONES POR HORA - ARGENTINA")
            self.setGeometry(200,200,500,500)

            layoutPrincipal = QVBoxLayout()
            fechas = QHBoxLayout()

            layout1 = QFormLayout()
            self.datetime_edit = QDateTimeEdit(self, calendarPopup=True)
            self.datetime_edit.dateTimeChanged.connect(self.update)
            layout1.addRow('Desde:', self.datetime_edit)
            fechas.addLayout(layout1)

            layout2 = QFormLayout()
            self.datetime_edit = QDateTimeEdit(self, calendarPopup=True)
            self.datetime_edit.dateTimeChanged.connect(self.update)
            layout2.addRow('Hasta:', self.datetime_edit)
            fechas.addLayout(layout2)

            confirmar = QPushButton()
            confirmar.setText("Confirmar fecha y horario")
            fechas.addWidget(confirmar)

            layoutPrincipal.addLayout(fechas)

            
            conexiones = QHBoxLayout()
            dispositivos = QVBoxLayout()
            boton = QPushButton()
            boton.setText("Para eliminar")
            dispositivos.addWidget(boton)
            informacion = QVBoxLayout()
            self.createTable() #agregamos la tabla
            informacion.addWidget(self.tableWidget)
            conexiones.addLayout(dispositivos)
            conexiones.addLayout(informacion) 
            layoutPrincipal.addLayout(conexiones)

            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)

      def update(self):
        value = self.datetime_edit.dateTime()

      def createTable(self):
            self.tableWidget = QTableWidget()
      
            #Fijas la cantidad de filas
            self.tableWidget.setRowCount(5) 
            #Fijas la cantidad de columnas
            self.tableWidget.setColumnCount(2)  
      
            self.tableWidget.setItem(0,0, QTableWidgetItem("Nombre"))
            self.tableWidget.setItem(0,1, QTableWidgetItem("-"))
            self.tableWidget.setItem(1,0, QTableWidgetItem("MAC"))
            self.tableWidget.setItem(1,1, QTableWidgetItem("-"))
            self.tableWidget.setItem(2,0, QTableWidgetItem("Hora alta"))
            self.tableWidget.setItem(2,1, QTableWidgetItem("-"))
            self.tableWidget.setItem(3,0, QTableWidgetItem("Hora baja"))
            self.tableWidget.setItem(3,1, QTableWidgetItem("-"))
            self.tableWidget.setItem(4,0, QTableWidgetItem("Router"))
            self.tableWidget.setItem(4,1, QTableWidgetItem("-"))
      
            #Se va a observar horizontalmente 
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



if __name__ == '__main__':
      app = QApplication(sys.argv)
      main = FechaWindow()
      main.show()
      app.exec()


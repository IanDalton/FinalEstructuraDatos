from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle
from Modulos.clases import *
import pickle
from datetime import datetime

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
      def __init__(self,pais:Pais):
            super().__init__()
            self.pais = pais
            self.provincia = None
            self.municipio = None
            self.departamento = None
            self.router = None

            self.setWindowTitle("Sistema de informacion - RED WIFI PAIS DIGITAL")
            self.setGeometry(200,200,1000,700)
            layoutPrincipal = QVBoxLayout()
            
            menu = QHBoxLayout()
            contenido = QHBoxLayout()


            cargarArchivos = QPushButton()      
            nuevaConexion = QPushButton() 
            preferencias = QComboBox()
            preferencias.addItems(['No mostrar conexiones (default)', 'Mostrar conexiones', 'Filtrar conexiones por hora'])
            preferencias.currentIndexChanged.connect(lambda checked :self.abrirVentanaFechas_click() if preferencias.currentIndex()==2 else None)

            cargarArchivos.setText('Cargar archivos') 
            cargarArchivos.clicked.connect(self.abrirVentanaCarga_click)
            nuevaConexion.setText('Nueva conexion')
            nuevaConexion.clicked.connect(self.abrirVentanaConexion_click)
            preferencias.setStyleSheet('background-color: darkGrey')
            menu.addWidget(cargarArchivos)
            menu.addWidget(nuevaConexion)
            menu.addWidget(preferencias,2)
            
            layoutPrincipal.addLayout(menu)
            
            layoutPrincipal.addLayout(contenido,2)

            self.provincias = QVBoxLayout()
            self.provincias.addWidget(QPushButton())

            for i in pais.provincias:
                  prov = QPushButton()
                  prov.setText(i.nombre)
                  prov.clicked.connect(lambda checked ,arg = i:self.seleccionar_provincia(arg))
                  self.provincias.addWidget(prov)

            contenido.addLayout(self.provincias)
            self.municipios = QVBoxLayout()
            contenido.addLayout(self.municipios)
            self.agregarMunicipios = QPushButton()
            self.agregarMunicipios.setText('Municipio nuevo')
            self.municipios.addWidget(self.agregarMunicipios)
            self.agregarMunicipios.clicked.connect(lambda clicked:self.abrirVentanaMunicipio_click() if self.provincia else None)
            self.departamentos = QVBoxLayout()
            contenido.addLayout(self.departamentos)
            agregarDepartamentos = QPushButton()
            agregarDepartamentos.setText('Departamento nuevo')
            self.departamentos.addWidget(agregarDepartamentos)
            agregarDepartamentos.clicked.connect(lambda clicked:self.abrirVentanaDepartamento_click() if self.municipio else None)
            agregar_router = QPushButton()
            agregar_router.setText('Agregar Router')
            agregar_router.clicked.connect(lambda clicked:self.abrirVentanaRouter_click() if self.departamento else None)
            self.routers = QVBoxLayout()
            self.routers.addWidget(agregar_router)
            contenido.addLayout(self.routers,2)

            self.municipios.setAlignment(Qt.AlignTop)
            self.provincias.setAlignment(Qt.AlignTop)
            self.departamentos.setAlignment(Qt.AlignTop)
            self.routers.setAlignment(Qt.AlignTop)
            
            self.frame = QFrame()
            settings = QVBoxLayout()
            self.frame.setLayout(settings)
            
            self.info = QLabel()
            settings.addWidget(self.info)
            crear_conexion = QPushButton()
            crear_conexion.setText('Registar conexion')
            crear_conexion.clicked.connect(self.agregar_conexion)
            self.activable = QHBoxLayout()
            settings.addLayout(self.activable)
            settings.addWidget(crear_conexion)
            texto1 = QLabel() 
            texto1.setText('Desactivado')
            self.activable.addWidget(texto1)
            self.toggle = AnimatedToggle(checked_color="#FFB000",pulse_checked_color="#44FFB000")
            
            self.activable.addWidget(self.toggle)
            texto2 = QLabel() 
            texto2.setText('Activo')
            self.activable.addWidget(texto2)
            

      #El widget que contiene al layout es el widget principal de la ventana, para mostrarlo
            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)
      
      def agregar_conexion(self):
            self.abrir_ventanaConexion = CrearConexion(self.pais,self.router)
            self.abrir_ventanaConexion.show()


      def limpiar(self,sector:QHBoxLayout):
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
            self.municipio = None
            self.departamento = None
            self.router = None
            self.provincia = prov
            for muni in prov.municipios:
                  lbl = QPushButton()
                  lbl.setText(muni.nombre)
                  lbl.setStyleSheet('border:1px solid black;')
                  lbl.clicked.connect(lambda checked,mun = muni:self.seleccionar_municipio(mun))
                  self.municipios.addWidget(lbl)
      def seleccionar_municipio(self,muni):
            self.limpiar(self.departamentos)
            self.limpiar(self.routers)
            self.router = None
            self.departamento = None
            self.municipio = muni
            for depto in muni.departamentos:
                  lbl = QPushButton()
                  lbl.setText(depto.nombre)
                  lbl.setStyleSheet('border:1px solid black;')
                  lbl.clicked.connect(lambda checked,dpto = depto:self.seleccionar_departamento(dpto))
                  self.departamentos.addWidget(lbl)
      def seleccionar_departamento(self,depto):
            print(self)
            self.limpiar(self.routers)
            self.router = None
            self.departamento = depto
            for i,router in enumerate(depto.routers):
                  lbl = QPushButton()
                  lbl.setText(str(router))
                  lbl.setStyleSheet('border:1px solid black;')
                  lbl.clicked.connect(lambda checked,rtr = router,index=i:self.seleccionar_router(rtr,index))
                  self.routers.addWidget(lbl)
            pass
      def seleccionar_router(self,router:Router,index):
            print(router.id)
            print(index)
            print(self.toggle.isChecked())
            
            self.routers.insertWidget(index+2,self.frame)
            self.router = router
            self.info.setText(f'Desde: {self.router.fecha_alta} Hasta: {self.router.fecha_baja}')
            if (self.router.fecha_baja is None and not self.toggle.isChecked() )or(self.router.fecha_baja and self.toggle.isChecked()):
                  self.toggle.toggle()
            
            self.toggle.toggled.connect(self.modificar_router)
            print(self.provincia,self.municipio,self.departamento,self.router)
            pass
      
      def modificar_router(self):
            if self.toggle.isChecked():
                  self.router.fecha_baja = None
            else:
                  self.router.fecha_baja = datetime.now() if not self.router.fecha_baja else self.router.fecha_baja
            self.info.setText(f'Desde: {self.router.fecha_alta} Hasta: {self.router.fecha_baja}')

      def abrirVentanaCarga_click(self):
            self.cargando_datos = CargaWindow()
            self.cargando_datos.show()

      def abrirVentanaConexion_click(self):
            self.estableciendo_conexion = ConexionWindow()
            self.estableciendo_conexion.show()

      def abrirVentanaFechas_click(self):
            self.abrir_ventanaFechas = FechaWindow(self.pais)
            self.abrir_ventanaFechas.show()
      
      def abrirVentanaMunicipio_click(self):
            self.ventana_agregarMunicipios = MunicipiosWindow(self.provincia)
            self.ventana_agregarMunicipios.show()

      def abrirVentanaDepartamento_click(self):
            self.ventana_agregarDepartamento = DepartamentosWindow(self.municipio)
            self.ventana_agregarDepartamento.show()

      def abrirVentanaRouter_click(self):
            self.ventana_agregarRouter = RouterWindow(self.departamento)
            self.ventana_agregarRouter.show()
            

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
            confirmacion.clicked.connect(self.generarConexion_click)

            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)
      
      def generarConexion_click(self):
            pass

class FechaWindow(QMainWindow): 
      def __init__(self,pais):
            super().__init__()
            self.pais = pais
            self.setWindowTitle("CONEXIONES POR HORA - ARGENTINA")
            self.setGeometry(200,200,500,500)

            layoutPrincipal = QVBoxLayout()
            fechas = QHBoxLayout()

            fecha1 = QFormLayout()
            self.datetime_edit1 = QDateTimeEdit(self, calendarPopup=True)
            self.datetime_edit1.dateTimeChanged.connect(self.update)
            fecha1.addRow('Desde:', self.datetime_edit1)
            fechas.addLayout(fecha1)

            fecha2 = QFormLayout()
            self.datetime_edit2 = QDateTimeEdit(self, calendarPopup=True)
            self.datetime_edit2.dateTimeChanged.connect(self.update)
            fecha2.addRow('Hasta:', self.datetime_edit2)
            fechas.addLayout(fecha2)

            confirmar = QPushButton()
            confirmar.setText("Confirmar fecha y horario")
            fechas.addWidget(confirmar)
            confirmar.clicked.connect(self.filtrarArbol)

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

      def filtrarArbol(self):
            self.pais.conexiones.fechaLimiteInferior(self.datetime_edit1)
            self.pais.conexiones.fechaLimiteSuperior(self.datetime_edit2)

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

class DepartamentosWindow(QMainWindow):
      def __init__(self):
            super().__init__()
            self.setWindowTitle("INSERTAR DEPARTAMENTO")
            self.setGeometry(1300,200,300,100)

            layoutPrincipal = QVBoxLayout()

            id = QHBoxLayout()
            nombre = QHBoxLayout()
            ids = QLabel(text="Id de departamento: ")
            id_ingresado = QTextEdit()
            nombres = QLabel(text="Nombre de departamento: ")
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

if __name__ == '__main__':
      app = QApplication(sys.argv)
      main = FechaWindow()
      main.show()
      app.exec()


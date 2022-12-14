from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QScrollArea,QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle
from Modulos.clases import *
import pickle
from datetime import datetime
from .routerWindow import RouterWindow
from .departamentosWindow import DepartamentosWindow
from .municipiosWindow import MunicipiosWindow
from .crearConexion import CrearConexion
from .cargaWindow import CargaWindow
from .fechaWindow import FechaWindow
from PyQt5.QtGui import QIcon
import sys

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
            cargarArchivos.setStyleSheet('QPushButton {background-color: #75AADB; color: black}')
            font_archivos = cargarArchivos.font()
            font_archivos.setBold(True)
            cargarArchivos.setFont(font_archivos)
            self.preferencias = QComboBox()
            self.preferencias.setStyleSheet('QComboBox {background-color: #75AADB; color: black}')
            self.preferencias.setFont(font_archivos)
            self.preferencias.addItems(['No mostrar conexiones (default)', 'Mostrar conexiones', 'Filtrar conexiones por hora'])
            self.preferencias.currentIndexChanged.connect(lambda checked :self.abrirVentanaFechas_click() if self.preferencias.currentIndex()==2 else None)

            self.setFont(font_archivos)

            self.preferencias.currentIndexChanged.connect(self.refrescar)
            cargarArchivos.setText('Cargar archivos') 
            cargarArchivos.clicked.connect(self.abrirVentanaCarga_click)
            menu.addWidget(cargarArchivos)
            menu.addWidget(self.preferencias,2)
            
            layoutPrincipal.addLayout(menu)
            
            layoutPrincipal.addLayout(contenido,2)

            self.provincias = QVBoxLayout()
            self.provincias.addWidget(QPushButton())

            for i in pais.provincias:
                  prov = QPushButton()
                  prov.setText(i.nombre)
                  prov.clicked.connect(lambda checked ,arg = i:self.seleccionar_provincia(arg))
                  self.provincias.addWidget(prov)

            
            muni_scroll = QScrollArea()
            muni_content = QWidget()
            depto_scroll = QScrollArea()
            depto_content = QScrollArea()
            router_scroll = QScrollArea()
            router_content = QWidget()


            muni_scroll.setWidget(muni_content)
            depto_scroll.setWidget(depto_content)
            router_scroll.setWidget(router_content)

            muni_scroll.setWidgetResizable(True)
            depto_scroll.setWidgetResizable(True)
            router_scroll.setWidgetResizable(True)

            contenido.addLayout(self.provincias)
            contenido.addWidget(muni_scroll,1)
            contenido.addWidget(depto_scroll,1)
            contenido.addWidget(router_scroll,2)
            

            self.municipios = QVBoxLayout()
            self.agregarMunicipios = QPushButton()
            self.agregarMunicipios.setText('Municipio nuevo')
            self.agregarMunicipios.setStyleSheet('QPushButton {background-color: #FCBF49; color: black;}')
            self.agregarMunicipios.setFont(font_archivos)
            self.municipios.addWidget(self.agregarMunicipios)
            self.agregarMunicipios.clicked.connect(lambda clicked:self.abrirVentanaMunicipio_click() if self.provincia else None)
            self.departamentos = QVBoxLayout()
            self.agregarDepartamentos = QPushButton()
            self.agregarDepartamentos.setText('Departamento nuevo')
            self.departamentos.addWidget(self.agregarDepartamentos)
            self.agregarDepartamentos.setStyleSheet('QPushButton {background-color: #FCBF49; color: black;}')
            self.agregarDepartamentos.setFont(font_archivos)
            self.agregarDepartamentos.clicked.connect(lambda clicked:self.abrirVentanaDepartamento_click() if self.municipio else None)
            self.agregar_router = QPushButton()
            self.agregar_router.setText('Agregar Router')
            self.agregar_router.setStyleSheet('QPushButton {background-color: #FCBF49; color: black;}')
            self.agregar_router.setFont(font_archivos)
            self.agregar_router.clicked.connect(lambda clicked:self.abrirVentanaRouter_click() if self.departamento else None)
            self.routers = QVBoxLayout()
            self.routers.addWidget(self.agregar_router)
            

            muni_content.setLayout(self.municipios)
            depto_content.setLayout(self.departamentos)
            router_content.setLayout(self.routers)
            

            self.municipios.setAlignment(Qt.AlignTop)
            self.provincias.setAlignment(Qt.AlignTop)
            self.departamentos.setAlignment(Qt.AlignTop)
            self.routers.setAlignment(Qt.AlignTop)
            
            self.frame = QFrame()
            settings = QVBoxLayout()
            self.frame.setLayout(settings)
            
            self.info = QLabel()
            settings.addWidget(self.info)
            self.crear_conexion = QPushButton()
            self.conexiones = QFrame()
            self.vbox = QVBoxLayout()
            self.conexiones.setLayout(self.vbox)
            settings.addWidget(self.conexiones)


            self.agregar_router.setEnabled(False)
            self.agregarDepartamentos.setEnabled(False)
            self.agregarMunicipios.setEnabled(False)


            self.crear_conexion.setText('Registrar conexion')
            self.crear_conexion.clicked.connect(self.agregar_conexion)
            self.activable = QHBoxLayout()
            settings.addLayout(self.activable)
            settings.addWidget(self.crear_conexion)
            texto1 = QLabel() 
            texto1.setText('Desactivado')
            self.activable.addWidget(texto1)
            self.toggle = AnimatedToggle(checked_color="#843511",pulse_checked_color="#843511")
            
            self.activable.addWidget(self.toggle)
            texto2 = QLabel() 
            texto2.setText('Activo')
            self.activable.addWidget(texto2)
            
            
            
            

      #El widget que contiene al layout es el widget principal de la ventana, para mostrarlo
            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)
      

      def refrescar(self):
            if self.preferencias.currentIndex()==1:
                  self.pais.actualizar_conexiones()
            self.limpiar(self.provincias)
            for i in self.pais.provincias:
                  prov = QPushButton()
                  if self.preferencias.currentIndex()==1:
                        prov.setText(f'{i.total_conectados}\{i.total}  {i.nombre}')
                  else:
                        prov.setText(f'{i.nombre}')
                  prov.clicked.connect(lambda checked ,arg = i:self.seleccionar_provincia(arg))
                  self.provincias.addWidget(prov)
            if not self.provincia:
                  return
            self.seleccionar_provincia(self.provincia,0)
            if not self.municipio:
                  return
            self.seleccionar_municipio(self.municipio,0)
            if not self.departamento:
                  return
            self.seleccionar_departamento(self.departamento,0)
            

      def agregar_conexion(self):
            self.abrir_ventanaConexion = CrearConexion(self.pais,self.router,self.refrescar)
            self.abrir_ventanaConexion.show()
            


      def limpiar(self,sector:QHBoxLayout,limit = 0):
            try:
                  i=max(range(sector.count()))
                  while i > limit :
                        sector.itemAt(i).widget().setParent(None)
                        i-=1
            except ValueError:
                  pass
            except AttributeError:
                  pass
            
      def seleccionar_provincia(self,prov,default = 1):
            self.limpiar(self.municipios)
            self.limpiar(self.departamentos)
            self.limpiar(self.routers)
            if default:
                  self.municipio = None
                  self.departamento = None
                  self.router = None
                  self.agregar_router.setEnabled(False)
                  self.agregarDepartamentos.setEnabled(False)
            self.agregarMunicipios.setEnabled(True)
            self.provincia = prov
            
            for muni in prov.municipios:
                  lbl = QPushButton()
                  if self.preferencias.currentIndex()==1:
                        lbl.setText(f'{muni.total_conectados}\{muni.total}  {muni.nombre}')
                  else:
                        lbl.setText(f'{muni.nombre}')
                  lbl.setStyleSheet('border:1px solid black;')
                  lbl.clicked.connect(lambda checked,mun = muni:self.seleccionar_municipio(mun))
                  self.municipios.addWidget(lbl)
      def seleccionar_municipio(self,muni,default = 1):
            self.limpiar(self.departamentos)
            self.limpiar(self.routers)
            if default:
                  self.router = None
                  self.departamento = None
                  self.agregar_router.setEnabled(False)
            self.agregarDepartamentos.setEnabled(True)
            self.municipio = muni
            for depto in muni.departamentos:
                  
                  lbl = QPushButton()
                  if self.preferencias.currentIndex()==1:
                        lbl.setText(f'{depto.total_conectados}\{depto.total}  {depto.nombre}')
                  else:
                        lbl.setText(f'{depto.nombre}')
                  lbl.setStyleSheet('border:1px solid black;')
                  lbl.clicked.connect(lambda checked,dpto = depto:self.seleccionar_departamento(dpto))
                  self.departamentos.addWidget(lbl)
                  
      def seleccionar_departamento(self,depto,default=1):
            print(self)
            self.limpiar(self.routers)
            if default:
                  self.router = None
            self.agregar_router.setEnabled(True)
            sel_router = None
            self.departamento = depto
            for i,router in enumerate(depto.routers):
                  content = QFrame()
                  hbox = QHBoxLayout()
                  content.setLayout(hbox)
                  btn = QPushButton()
                  btn.setText('EXPANDIR')
                  hbox.addWidget(QLabel(text=f'{router}'),alignment=Qt.AlignLeft)
                  if self.preferencias.currentIndex()==1:
                        hbox.addWidget(QLabel(text=f'{len(router.conexiones)}/{router.conexiones_max}'),alignment=Qt.AlignRight)
                  btn.setStyleSheet('border:1px solid black;')
                  btn.clicked.connect(lambda checked,rtr = router,index=i:self.seleccionar_router(rtr,index))
                  hbox.addWidget(btn,2,alignment=Qt.AlignRight)
                  content.setStyleSheet('border:1px solid black;')
                  if router == self.router and self.router:
                        sel_router = (router,i)

                  self.routers.addWidget(content)
            if sel_router:
                  self.seleccionar_router(sel_router[0],sel_router[1])
            pass


      def seleccionar_router(self,router:Router,index):

            
            self.routers.insertWidget(index+2,self.frame)
            self.router = router
            
            self.info.setText(f'Desde: {self.router.fecha_alta} Hasta: {self.router.fecha_baja}')
            if (self.router.fecha_baja is None and not self.toggle.isChecked() )or(self.router.fecha_baja and self.toggle.isChecked()):
                  self.toggle.toggle()
            
            
            self.limpiar(self.vbox,-1)
            for conexion in router.conexiones:
                  self.vbox.addWidget(QLabel(text=f'MAC:{conexion.mac.mac}   IP:{conexion.ip}'))
            
            self.toggle.toggled.connect(self.modificar_router)
            self.crear_conexion.setEnabled(self.toggle.isChecked())
            print(self.provincia,self.municipio,self.departamento,self.router)
            pass
      
      def modificar_router(self):
            self.crear_conexion.setEnabled(self.toggle.isChecked())
            if self.toggle.isChecked():
                  self.router.fecha_baja = None
            else:
                  self.router.fecha_baja = datetime.now() if not self.router.fecha_baja else self.router.fecha_baja
                  for conexion in self.router.conexiones:
                        conexion.mac.desconectar(self.router)
            self.info.setText(f'Desde: {self.router.fecha_alta} Hasta: {self.router.fecha_baja}')
            self.refrescar()

      def abrirVentanaCarga_click(self):
            self.cargando_datos = CargaWindow(self.pais,self.refrescar)
            self.cargando_datos.show()

      def abrirVentanaFechas_click(self):
            self.abrir_ventanaFechas = FechaWindow(self.pais)
            self.abrir_ventanaFechas.show()
            self.preferencias.setCurrentIndex(0)
            
      
      def abrirVentanaMunicipio_click(self):
            self.ventana_agregarMunicipios = MunicipiosWindow(self.provincia,self.refrescar)
            self.ventana_agregarMunicipios.show()


      def abrirVentanaDepartamento_click(self):
            self.ventana_agregarDepartamento = DepartamentosWindow(self.municipio,self.refrescar)
            self.ventana_agregarDepartamento.show()


      def abrirVentanaRouter_click(self):
            self.ventana_agregarRouter = RouterWindow(self.departamento,self.pais,self.refrescar)
            self.ventana_agregarRouter.show()




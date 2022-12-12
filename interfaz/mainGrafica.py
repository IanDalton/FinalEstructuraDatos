from PyQt5.QtCore import Qt
#from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem
from qtwidgets import AnimatedToggle

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
            self.setGeometry(500,200,1000,700)
            layoutPrincipal = QVBoxLayout()
            #self.setPalette(dark_theme
            
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
            preferencias.setStyleSheet('background-color: red')
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
            self.agregarMunicipios.setText('Agregar municipio')
            self.municipios.addWidget(self.agregarMunicipios)
            self.departamentos = QVBoxLayout()
            contenido.addLayout(self.departamentos)
            agregarDepartamentos = QPushButton()
            agregarDepartamentos.setText('Agregar departamento')
            self.departamentos.addWidget(agregarDepartamentos)

            self.routers = QVBoxLayout()
            contenido.addLayout(self.routers,1)
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
            self.setGeometry(500,200,1000,700)
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
            
            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)

class ConexionWindow(QMainWindow):
      def __init__(self):
            super().__init__()
            self.setWindowTitle("NUEVA CONEXION")
            self.setGeometry(500,200,1000,700)
            layoutPrincipal = QVBoxLayout()

            disclaimer = QLabel(text="Ingrese los datos para completar la conexion: ")
            layoutPrincipal.addWidget(disclaimer)

            dispositivo = QHBoxLayout()
            dispositivo_text = QLabel(text="Dispositivo: ")
            dispositivo_box = QTextEdit()
            dispositivo.addWidget(dispositivo_text)
            dispositivo.addWidget(dispositivo_box)
            layoutPrincipal.addLayout(dispositivo)
            ip = QHBoxLayout()
            ip_text = QLabel(text="Ip: ")
            ip_box = QTextEdit()
            ip.addWidget(ip_text)
            ip.addWidget(ip_box)
            layoutPrincipal.addLayout(ip)
            router = QHBoxLayout()
            router_text = QLabel(text="Router: ")
            router_box = QTextEdit()
            router.addWidget(router_text)
            router.addWidget(router_box)
            layoutPrincipal.addLayout(router)

            alta = QFormLayout()
            self.datetime_edit = QDateTimeEdit(self, calendarPopup=True)
            self.datetime_edit.dateTimeChanged.connect(self.update)
            alta.addRow('Alta:', self.datetime_edit)
            layoutPrincipal.addLayout(alta)

            confirmacion = QPushButton(text="Confirmar datos")
            layoutPrincipal.addWidget(confirmacion)


            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)

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


# #Grafico de torta para cantidad de usuarios en linea
#    def create_piechart(self):  
 
#       series = QPieSeries()
#       series.append("Python", 80)
#       series.append("C++", 70)
#       series.append("Java", 50)
#       series.append("C#", 40)
#       series.append("PHP", 30)
 

#       #adding slice
#       slice = QPieSlice()
#       slice = series.slices()[2]
#       slice.setExploded(True)
#       slice.setLabelVisible(True)
#       slice.setPen(QPen(Qt.darkGreen, 2))
#       slice.setBrush(Qt.green)

#       chart = QChart()
#       chart.legend().hide()
#       chart.addSeries(series)
#       chart.createDefaultAxes()
#       chart.setAnimationOptions(QChart.SeriesAnimations)
#       chart.setTitle("Pie Chart Example")
 
#       chart.legend().setVisible(True)
#       chart.legend().setAlignment(Qt.AlignBottom)
 
#       chartview = QChartView(chart)
#       chartview.setRenderHint(QPainter.Antialiasing)

#       self.setCentralWidget(chartview)

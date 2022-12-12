from PyQt5.QtCore import Qt
#from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget
from qtwidgets import AnimatedToggle
import pickle


import sys

dark_theme = QPalette()
dark_theme.setColor(QPalette.Window, QColor(53, 53, 53))
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



class MainWindow(QMainWindow): 

   def __init__(self):
      super().__init__()
      self.setWindowTitle("Sistema de informacion - RED WIFI PAIS DIGITAL")
      
      self.setGeometry(500,500,1000,700)
      layoutPrincipal = QVBoxLayout()
      #self.setPalette(dark_theme)
#Creo un label y lo agrego al layout
      
      menu = QHBoxLayout()
      contenido = QHBoxLayout()
      

      
      cargarArchivos = QPushButton()      
      nuevaConexion = QPushButton() 
      preferencias = QPushButton()
      cargarArchivos.setText('Cargar archivos')
      nuevaConexion.setText('Nueva conexion')
      preferencias.setText('Preferencias')
      preferencias.setStyleSheet('background-color: red')
      menu.addWidget(cargarArchivos)
      menu.addWidget(nuevaConexion)
      menu.addWidget(preferencias,2)
      
      layoutPrincipal.addLayout(menu)
      
      layoutPrincipal.addLayout(contenido,1)

      self.provincias = QVBoxLayout()
      """  for provincia in arg.provincias:
            prov = QLabel()
            prov.setText(provincia.nombre)
            provincias.addWidget(prov) """
            

      contenido.addLayout(self.provincias)
      self.municipios = QVBoxLayout()
      contenido.addLayout(self.municipios)
      agregarMunicipios = QPushButton()
      agregarMunicipios.setText('Municipio nuevo')
      self.municipios.addWidget(agregarMunicipios)
      departamentos = QVBoxLayout()
      contenido.addLayout(departamentos)
      agregarDepartamentos = QPushButton()
      departamentos.addWidget(agregarDepartamentos)

      routers = QVBoxLayout()
      contenido.addLayout(routers,1)
      
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
      routers.addLayout(activable)

      
#El widget que contiene al layout es el widget principal de la ventana, para mostrarlo
      widgetLayout = QWidget()
      widgetLayout.setLayout(layoutPrincipal)
      self.setCentralWidget(widgetLayout)

      


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


class TercerWindow(QMainWindow): 

   def __init__(self):
      super().__init__()
      self.setWindowTitle("Conexiones por hora")
      
      self.setGeometry(500,500,700,1000)
      layoutPrincipal = QVBoxLayout()
      #self.setPalette(dark_theme)
#Creo un label y lo agrego al layout
      
      contenido = QHBoxLayout() #fijarnos si sirve
      texto1 = QLabel()
      texto1.setText("Desde: ")
      contenido.addWidget(texto1)

      campo1 = QTextEdit()
      contenido.addWidget(campo1)

      texto2 = QLabel()
      texto2.setText("Hasta: ")
      contenido.addWidget(texto2)

      campo2 = QTextEdit()
      contenido.addWidget(campo2)

      layoutPrincipal.addLayout(contenido)

#El widget que contiene al layout es el widget principal de la ventana, para mostrarlo
      widgetLayout = QWidget()
      widgetLayout.setLayout(layoutPrincipal)
      self.setCentralWidget(widgetLayout)
""" 
app2 = QApplication(sys.argv)
TercerWindow = TercerWindow()
TercerWindow.show()
app2.exec()
 """
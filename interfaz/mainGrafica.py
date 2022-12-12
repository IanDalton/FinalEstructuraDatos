from PyQt5.QtCore import Qt
#from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit
from qtwidgets import AnimatedToggle
import pickle


import sys
""" 
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

 """

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
            self.agregarMunicipios = QPushButton()
            self.agregarMunicipios.setText('Municipio nuevo')
            self.municipios.addWidget(self.agregarMunicipios)
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

      

      def seleccionar_provincia(self,prov):
            i=max(range(self.municipios.count()))
            while i >= 1 :
                  self.municipios.itemAt(i).widget().setParent(None)
                  i-=1
            for muni in prov.municipios:
                  print(muni)
                  lbl = QLabel()
                  lbl.setText(muni.nombre)
                  lbl.setStyleSheet('border:1px solid black;')
                  self.municipios.addWidget(lbl)

class SegundaWindow(QMainWindow):
      def __init__(self):
            super().__init__()
            self.setWindowTitle("")
            self.setGeometry(500,500,700,1000)
            layoutPrincipal = QVBoxLayout()
            contenido = QHBoxLayout()

class TercerWindow(QMainWindow): 
      def __init__(self):
            super().__init__()
            self.setWindowTitle("Conexiones por hora")
            
            self.setGeometry(500,500,700,1000)
            layoutPrincipal = QVBoxLayout()
            contenido = QHBoxLayout()

      #self.setPalette(dark_theme)

            layout1 = QFormLayout()
            
            self.datetime_edit = QDateTimeEdit(self, calendarPopup=True)
            self.datetime_edit.dateTimeChanged.connect(self.update)

            self.result_label = QLabel('', self)

            layout1.addRow('Desde:', self.datetime_edit)
            layout1.addRow(self.result_label)

            self.show()
            contenido.addLayout(layout1)

            layout2 = QFormLayout()
            
            self.datetime_edit = QDateTimeEdit(self, calendarPopup=True)
            self.datetime_edit.dateTimeChanged.connect(self.update)

            self.result_label = QLabel('', self)

            layout2.addRow('Hasta:', self.datetime_edit)
            layout2.addRow(self.result_label)

            self.show()
            contenido.addLayout(layout2)

            layoutPrincipal.addLayout(contenido)
            
            conexiones = QHBoxLayout()
            dispositivos = QVBoxLayout()
            informacion = QVBoxLayout()
            conexiones.addLayout(dispositivos)
            conexiones.addLayout(informacion) #Nombre,mac,hora alta,hora baja,router...
            
            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)


      def update(self):
        value = self.datetime_edit.dateTime()
        self.result_label.setText(value.toString("yyyy-MM-dd HH:mm"))

if __name__ == '__main__':
      app = QApplication(sys.argv)
      
      TercerWindows = TercerWindow()
      TercerWindows.show()
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

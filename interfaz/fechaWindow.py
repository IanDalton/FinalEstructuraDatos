from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle
from Modulos.clases import *


class FechaWindow(QMainWindow): 
      def __init__(self,pais:Pais):
            super().__init__()
            self.pais = pais
            self.setWindowTitle("CONEXIONES POR HORA - ARGENTINA")
            self.setGeometry(200,200,500,500)
            self.conexiones = None
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
            self.dispositivos = QVBoxLayout()
            boton = QPushButton()
            boton.setText("Para eliminar")
            self.dispositivos.addWidget(boton)
            informacion = QVBoxLayout()
            self.createTable() #agregamos la tabla
            informacion.addWidget(self.tableWidget)
            conexiones.addLayout(self.dispositivos)
            conexiones.addLayout(informacion) 
            layoutPrincipal.addLayout(conexiones)

            widgetLayout = QWidget()
            widgetLayout.setLayout(layoutPrincipal)
            self.setCentralWidget(widgetLayout)

      def filtrarArbol(self):
            self.limpiar(self.dispositivos,-1)
            self.conexiones = self.pais.conexiones.fechaLimites(self.datetime_edit1.dateTime(),self.datetime_edit2.dateTime())
            
            for conexion in self.conexiones:
                  btn = QPushButton()
                  btn.setText(f'{conexion.alta.strftime("%d/%m/%Y %H:%M")}~{conexion.mac.mac}')
                  btn.clicked.connect(lambda clicked,cn = conexion:self.conexion_seleccionada(cn))
                  self.dispositivos.addWidget(btn)
      
      def conexion_seleccionada(self,conexion:Conexion):
            self.tableWidget.setItem(0,1, QTableWidgetItem("-"))
            self.tableWidget.setItem(1,1, QTableWidgetItem(f"{conexion.mac.mac}"))
            self.tableWidget.setItem(2,1, QTableWidgetItem(f"{conexion.alta}"))
            self.tableWidget.setItem(3,1, QTableWidgetItem(f"{conexion.baja}"))
            self.tableWidget.setItem(4,1, QTableWidgetItem(f"{conexion.router.identificador}"))
            pass
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
      def update(self):
        value = self.datetime_edit1.dateTime()

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

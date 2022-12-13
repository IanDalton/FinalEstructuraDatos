from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFrame,QMainWindow,QVBoxLayout,QLabel,QTextEdit,QPushButton,QHBoxLayout,QApplication,QWidget,QFormLayout,QDateTimeEdit,QTableWidget,QHeaderView,QTableWidgetItem,QComboBox  
from qtwidgets import AnimatedToggle


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

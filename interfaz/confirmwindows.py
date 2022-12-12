from PyQt5.QtWidgets import QMainWindow,QVBoxLayout,QLabel,QWidget,QHBoxLayout,QLineEdit,QPushButton

class ConfirmWindows(QWidget):
    def __init__(self,funcion_borrar):
        super().__init__()
        self.setGeometry(200,200,500,250)
        self.setWindowTitle("¿Quiere eliminar este elemento?")
        
        container=QWidget()
        self.setLayoutscontainer
        
        verticalLayout=QVBoxLayout()
        container.setLayout(verticalLayout)
        
        label1=QLabel("¿DESEA ELIMINAR EL COMPONENTE?")
        
        verticalLayout.addWidget(label1)
        
        horizontalLayout=QHBoxLayout()
        button1=QPushButton("Cancelar")
        button2=QPushButton("Confirmar")
        horizontalLayout.addWidget(button1)
        horizontalLayout.addWidget(button2)
        verticalLayout.addLayout(horizontalLayout)

    
    
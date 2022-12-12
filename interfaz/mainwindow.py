from PyQt5.QtWidgets import QMainWindow,QVBoxLayout,QLabel,QWidget,QHBoxLayout,QLineEdit,QPushButton
from confirmwindows import ConfirmWindows

class MainWindow(QMainWindow):
    
    def borrar(self):
        print("Borrar")
        
    def button_onClick(self):
        print(self.textField.text())
        self.textField.seText("")
    
    def textField_onChange(self):
        text = self.textField.text()
        if (len(text)==0):
            self.button.setDisabled(True)
        else:
            self.button.setDisabled(False)
    
    def bottonBorrar_onClick(self):
        self.nuevaVentana=ConfirmWindows(self.borrar)
        self.nuevaVentana.show()
        
                
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(0,0,200,200)
        self.setWindowTitle("Mi programa re lindo :D")
        
        #Creamos el widget que representa el contenido de la ventana
        mainContainer= QWidget()
        #A ese contenido lo vamos a organizar verticalmente
        vLayout = QVBoxLayout()
        mainContainer.setLayout(vLayout)
        self.setCentralWidget(mainContainer)
        
        label1=QLabel("Esto es un label")
        label1.setStyleSheet("background-color: pink")
        vLayout.addWidget(label1)
        
        
        hLayout=QHBoxLayout()
        
        label2=QLabel("L1 INTERNO")
        label2.setStyleSheet("background-color: purple")
        hLayout.addWidget(label2)
        
        label3=QLabel("L2 INTERNO")
        label3.setStyleSheet("background-color: green")
        hLayout.addWidget(label3)
        
        self.textField=QLineEdit()
        self.textField.textChanged.connect(self.textField_onChange)
      
        hLayout.addWidget(self.textField)
        
        self.button=QPushButton("Reiniciar Valor")
        self.button.clicked.connect(self.button_onClick)
        self.button.clicked.connect(self.button_onClick)
        hLayout.addWidget(self.button)
        
        vLayout.addLayout(hLayout)
        
        label4=QLabel("Esto es OTRO label")
        label4.setStyleSheet("background-color: yellow")
        vLayout.addWidget(label4)
        
        btn=QPushButton("Borrame todo")
        vLayout.addWidget(btn)
        
        btn.clicked.connect(self.bottonBorrar_onClick)
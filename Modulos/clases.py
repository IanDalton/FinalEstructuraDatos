import pickle
from datetime import datetime
from .claseArbol import Arbol,NodoArbol
from .ListasEnlazadas import ListaEnlazada
from .verificador import verificador_municipios
import numpy as np
import time
import csv

class Dispositivo():
    def __init__(self,mac) -> None:
        self.mac = mac
    def conectar(self,router):
        router.conectar(self)
        pass
    def desconectar(self,router):
        pass


class Conexion():
    def __init__(self,dispositivo,ip,router,alta,baja=None) -> None: #dispositivo: como te identifican externamente / ip: como te identificas internamente 
        self.mac = dispositivo
        self.alta = alta
        self.baja = baja
        self.ip = ip
        self.router = router

    def __eq__(self, __o) -> bool:
        if type(__o) == object: 
            return self.ip == __o.ip
        elif type(__o) == Dispositivo:
            return self.mac == __o
            

    def __ge__(self, __o: object): # self >= __o
        return self.alta >= __o.alta
    def __gt__(self, __o: object): # self > __o
        return self.alta > __o.alta
    def __le__(self, __o: object): # self <= __o
        return self.alta <= __o.alta
    def __lt__(self, __o: object): # self < __o
        return self.alta < __o.alta    
    def __str__(self) -> str:
        return f'Conexion del dispotivo {self.mac.mac} a las {self.alta}'
        
class Pais():
    def __init__(self,nombre:str,poblacion:int) -> None:
        self.nombre = nombre
        self.poblacion = poblacion 
        self.provincias = list() # Saque el set porque es necesario un orden y es mas rapido para ubicar el archivo
        self.conexiones = Arbol()
    def save(self):
        with open('archivo.pickle','wb') as arch:
            pickle.dump(self,arch,protocol=pickle.HIGHEST_PROTOCOL)
    def load_data(self,archivo,type):
        with open(archivo, 'r') as arch:
            data = csv.DictReader(arch)
            match type: # Nos permite agregar mas funciones al archivo si es necesario 
                case 'Municipio':
                    print('Cargando los municipios...')
                    for muni in data:
                        if verificador_municipios(muni):
                            try:
                                self.create_municipio(muni)
                            except:
                                pass
                        pass
                    pass
                case 'Router':
                    print("Cargando los routers...")
    def create_municipio(self,municipio):
        provincia = arg.provincias.pop(arg.provincias.index('Cordoba'))

        Municipio()
        
        
        pass
    


class Provincia():
    def __init__(self,nombre:str,pais:Pais) -> None:
        self.nombre = nombre
        self.municipios = set()
        pais.provincias.append(self)
    def __hash__(self) -> int:
        return hash(self.nombre)
    def __eq__(self, __o: object) -> bool:
        if type(__o) == object:
            return self.nombre==__o.nombre
        else:
            return self.nombre==__o
    
class Municipio():
    def __init__(self,id:int,nombre:str,provincia:Provincia) -> None:
        self.id = id
        self.nombre = nombre
        self.departamentos = set()
        if id not in provincia.municipios:
            provincia.municipios.add(self)
        else:
            del self
            
    def __hash__(self) -> int:
        return hash(self.id)
    def __eq__(self, __o: object) -> bool:
        return self.id==__o.id

class Departamento():
    def __init__(self,id:int,nombre:str,municipio:Municipio) -> None:
        self.id = id
        self.nombre = nombre
        self.routers = set()
        municipio.departamentos.add(self)




class Router(): # Armar un dict que le asigne la ip a una mac
    def __init__(self,id:int,ubicacion:str,latitud:int,longitud:int,pais:Pais,departamento:Departamento,conexiones_max=20,fecha_alta=datetime.now(),fecha_baja=None) -> None:
        self.id = id
        self.ubicacion = ubicacion
        self.latitud = latitud
        self.longitud = longitud
        self.conexiones_max = conexiones_max
        self.conexiones = ListaEnlazada() #lista enlazada
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja
        self.pais = pais
        departamento.routers.add(self)
    
    def __str__(self) -> str:
        return str(self.id)

    def conectar(self,dispo:Dispositivo):
        if self.conexiones.len < self.conexiones_max:
            conexion = Conexion(dispo,self.generar_ip(),self,datetime.now())
            self.pais.conexiones.agregarnodo(NodoArbol(conexion))
            self.conexiones.append(conexion)

    def generar_ip(self)->str:
        base = '192.168.68.'
        #revisamos la lista de conexiones hasta encontrar una ip libre
        nro_esperado = 0
        for conexion in self.conexiones:
            if int(conexion.ip[-2:]) != nro_esperado:
                break
            nro_esperado += 1
        return f'{base}{str(nro_esperado).rjust(2,"0")}'

    def desconectar(self,dispo:Dispositivo):
        conexion = self.conexiones.delete_node(dispo)
        conexion.baja = datetime.now()
        
        
if __name__ == '__main__':
    arg = Pais('Argentina',4)
    bsas = Provincia('Buenos Aires',arg)
    Provincia('cu',arg)
    Provincia('cuso',arg)
    lomas = Municipio(1,'Lomas de Zamora',bsas)
    temperley = Departamento(1,'Temperley',lomas)
    router = Router(1,None,1,1,arg,temperley)
    celu = Dispositivo(1)
    
    ac = Dispositivo(12)
    celu.conectar(router)
    
    input()

    ac.conectar(router)

    print(arg.conexiones.root.derecho.dato)
    """ arg.load_data('Datos\municipios.csv','Municipio') """
    arg.save()

    for provincia in arg.provincias:
        print(provincia.nombre)
    pass

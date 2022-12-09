import pickle
from datetime import datetime
from claseArbol import Arbol,NodoArbol
from ListasEnlazadas import ListaEnlazada
import time


class Disitivo():
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

    def __eq__(self, __o: object) -> bool:
        return self.ip == __o.ip

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
        self.provincias = set()
        self.conexiones = Arbol()
    def save(self):
        with open('archivo.pickle','wb') as arch:
            pickle.dump(self,arch,protocol=pickle.HIGHEST_PROTOCOL)
    def load_data(self,archivo,type):
        match type: # Nos permite agregar mas funciones al archivo si es necesario 
            case 'Municipio':
                print('Cargando los municipios...')
                pass
            case 'Router':
                print("Cargando los routers...")
    


class Provincia():
    def __init__(self,nombre:str,pais:Pais) -> None:
        self.nombre = nombre
        self.municipios = set()
        pais.provincias.add(self)
    def __hash__(self) -> int:
        return hash(self.nombre)
    def __eq__(self, __o: object) -> bool:
        return self.nombre==__o.nombre
    
class Muncipio():
    def __init__(self,id:int,nombre:str,provincia:Provincia) -> None:
        self.id = id
        self.nombre = nombre
        self.departamentos = set()
        provincia.municipios.add(self)
    def __hash__(self) -> int:
        return hash(self.id)
    def __eq__(self, __o: object) -> bool:
        return self.id==__o.id

class Departamento():
    def __init__(self,id:int,nombre:str,municipio:Muncipio) -> None:
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
        self.longitus = longitud
        self.conexiones_max = conexiones_max
        self.conexiones = ListaEnlazada() #lista enlazada
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja
        self.pais = pais
        departamento.routers.add(self)
        
    def conectar(self,dispo:Disitivo):
        if self.conexiones.len < self.conexiones_max:
            conexion = Conexion(dispo,self.generar_ip(),self,datetime.now())
            self.pais.conexiones.agregarnodo(NodoArbol(conexion))
            self.conexiones.append(conexion)

    def generar_ip(self)->str:
        base = '192.168.68.'
        #revisamos la lista de conexiones hasta encontrar una ip libre
        nro_esperado = 0
        for conexion in self.conexiones:
            if conexion.ip != nro_esperado:
                break
            nro_esperado += 1
        return f'{base+str(nro_esperado)}'
    def desconectar(self,dispo:Disitivo):
        conexion = self.conexiones.delete_node(dispo)
        conexion.baja = datetime.now()
        
        

if __name__ == '__main__':
    arg = Pais('Argentina',4)
    bsas = Provincia('Buenos Aires',arg)
    lomas = Muncipio(1,'Lomas de Zamora',bsas)
    temperley = Departamento(1,'Temperley',lomas)
    router = Router(1,None,1,1,arg,temperley)
    celu = Disitivo(1)
    
    ac = Disitivo(12)
    celu.conectar(router)
    
    input()

    ac.conectar(router)

    print(arg.conexiones.root.derecho.dato)
    """ arg.load_data('Datos\municipios.csv','Municipio') """
    arg.save()
    pass
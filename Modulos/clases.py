import pickle
from datetime import datetime
from .claseArbol import Arbol,NodoArbol
from .ListasEnlazadas import ListaEnlazada
from .verificador import verificador_municipios
import numpy as np
import csv,os

class Dispositivo(): # La idea de la clase dispositivo es, por si uno ya existe, se pueda cargar directamente a las conexiones
    def __init__(self,mac,pais) -> None:
        self.mac = mac
        self.status_conexion = None
        pais.dispositivos[self.mac] = self
    def __hash__(self) -> int:
        return hash(self.mac)
    def __eq__(self, __o: object) -> bool:
        if type(__o) == object:
            return self.mac == __o.mac
        else:
            return self.mac == __o
    def conectar(self,router): # Se intenta conectar al router. Si el dispositivo ya esta conectado, se deconecta y se reconecta al nuevo router
        
        try:
            if not self.status_conexion:
                router.conectar(self)
                self.status_conexion=router
            else:
                self.desconectar(self.status_conexion)
                self.conectar(router)
        except ValueError:
            pass
    def desconectar(self,router):
        
        router.desconectar(self)
        self.status_conexion = None
        pass


class Conexion():
    def __init__(self,dispositivo,ip,router,alta,baja=None) -> None: #dispositivo: como te identifican externamente / ip: como te identificas internamente 
        self.mac = dispositivo
        self.alta = alta
        self.baja = baja
        self.ip = ip
        self.router = router

    def __eq__(self, __o) -> bool: # Todo esto es para que se pueda ordenar en el arbol
        if type(__o) == object: 
            return self.ip == __o.ip
        elif type(__o) == Dispositivo:
            return self.mac.mac == __o
            
    def __ge__(self, __o: object): # self >= __o'
        if type(__o)==object:
            return self.alta >= __o.alta
        else:
            return self.alta >= __o
    def __gt__(self, __o: object): # self > __o
        if type(__o)==object:
            return self.alta > __o.alta
        else:
            return self.alta > __o
        
    def __le__(self, __o: object): # self <= __o
        if type(__o)==object:
            return self.alta <= __o.alta
        else:
            return self.alta <= __o
    def __lt__(self, __o: object): # self < __o
        if type(__o)==object:
            return self.alta < __o.alta
        else:
            return self.alta < __o   
    def __str__(self) -> str:
        return f'Conexion del dispotivo {self.mac.mac} a las {self.alta}'
        
class Pais():
    def __init__(self,nombre:str) -> None:
        self.nombre = nombre
        self.provincias = dict() 
        self.conexiones = Arbol()
        self.dispositivos = dict()
    def save(self):
        with open('archivo.pickle','wb') as arch:
            pickle.dump(self,arch,protocol=pickle.HIGHEST_PROTOCOL)
    def load_data(self,archivo,type) -> list:
        
        errores = []
        with open(archivo, 'r') as arch:
            data = csv.DictReader(arch)
            match type: # Nos permite agregar mas funciones al archivo si es necesario 
                case 'Municipio':
                    print('Cargando los municipios...')
                    for muni in data:
                        if verificador_municipios(muni): #Verifica el formato y crea el departamento
                            try:
                                self.create_departamento(muni,self.create_municipio(muni))
                            except NameError as error:
                                muni['error'] = error
                                errores.append(muni)
                        else:
                            muni['error']='El formato del id de municipio no coincide con la provincia'
                            errores.append(muni)
                        
                    
                case 'Router':
                    print("Cargando los routers...")
                    for router in data:
                        try:
                            self.cargar_router(router)
                        except NameError as error:
                            router['error'] = error
                            errores.append(router)
                        except KeyError as error:
                            router['error'] = 'La provincia o el municipio que cargaste no existe'
                            errores.append(router)
                        except ValueError:
                            router['error'] = 'El formato del id departamento esta mal'
                            errores.append(router)
                        
        return errores

    def cargar_router(self,dict):
        depto = self.get_departamento(int(dict['id_departamento']),self.get_municipio(dict['municipio_id'],self.get_provincia(dict['provincia_id'])))
        if int(dict['id']) not in depto.routers:
            Router(
                int(dict['id']),
                dict['identificador'],
                dict['ubicacion'],
                dict['latitud'],
                dict['longitud'],
                self,
                depto,
                )
        else:
            raise NameError

    def get_departamento(self,id:int,municipio)->object:
        return  municipio.departamentos[id]
    def get_municipio(self,id,provincia)-> object:
        return provincia.municipios[id]
    def get_provincia(self,id) -> object:
        return self.provincias[id]

    def actualizar_conexiones(self): # Se actualizan todos los valores de todas las provincias
        for prov in self.provincias:
            prov.actualizar_conexiones()


    def create_municipio(self,municipio) -> object:
        provincia = self.get_provincia(municipio['provincia_id'])
        try:  # Estoy bastante contento de esto! Basicamente intenta conseguir el municipio y si no lo encuentra lo genera
            muni = self.get_municipio(municipio['municipio_id'],provincia)
        except KeyError:
            muni = Municipio(provincia=provincia,id=municipio['municipio_id'],nombre=municipio['municipio'])
            
        return muni
            

    def create_departamento(self,departamento,municipio):
        if int(departamento['id_departamento']) not in municipio.departamentos:
            Departamento(id=int(departamento['id_departamento']),nombre=departamento['departamento '],municipio=municipio)
        else:
            raise NameError('El ID del departamento no existe')
    
    def save_error(self,error:list,name:str):
        if not os.path.exists('Errores'):
            os.makedirs('Errores')
        if len(error) > 0:
            with open(f'Errores/{name}-{datetime.now().date()}.csv','w',newline='') as arch:
                data = csv.DictWriter(arch,error[0].keys())
                data.writeheader()
                for err in error:
                    data.writerow(err)
    
class Provincia():
    def __init__(self,nombre:str,pais:Pais,provincia_id) -> None:
        self.id = provincia_id
        self.nombre = nombre
        self.municipios = dict()
        pais.provincias[self.id] = self
        self.total = 0
        self.total_conectados = 0
    def actualizar_conexiones(self):
        self.total = 0
        self.total_conectados = 0
        for muni in self.municipios:
            muni.actualizar_conexiones()
            self.total += muni.total
            self.total_conectados += muni.total_conectados
    def __hash__(self) -> int:
        return hash(self.id)
    def __eq__(self, __o: object) -> bool:
        if type(__o) == object:
            return self.id==__o.id
        else:
            return self.id==__o
    
class Municipio():
    def __init__(self,id:int,nombre:str,provincia:Provincia) -> None:
        self.id = id
        self.nombre = nombre
        self.departamentos = dict()
        provincia.municipios[self.id]=self
        self.total = 0
        self.total_conectados = 0
    def actualizar_conexiones(self):
        self.total = 0
        self.total_conectados = 0
        for depto in self.departamentos:
            depto.actualizar_conexiones()
            self.total += depto.total
            self.total_conectados += depto.total_conectados
            
    def __hash__(self) -> int:
        return hash(self.id)
    def __eq__(self, __o: object) -> bool:
        if type(__o) == object:
            return self.id==__o.id
        else:
            return self.id==__o

class Departamento():
    def __init__(self,id:int,nombre:str,municipio:Municipio) -> None:
        self.id = id
        self.nombre = nombre
        self.routers = dict()
        self.total = 0
        self.total_conectados = 0
        municipio.departamentos[id] = self
    def actualizar_conexiones(self):
        self.total = 0
        self.total_conectados = 0
        for router in self.routers:
            if not router.fecha_baja:
                self.total += router.conexiones_max
                self.total_conectados += len(router.conexiones)
    def __eq__(self, __o: object) -> bool:
        if type(__o)==object:
            return self.id==__o.id
        else:
            return self.id == __o

class Router():
    def __init__(self,id:int,identificador:str,ubicacion:str,latitud,longitud,pais:Pais,departamento:Departamento,conexiones_max=20,fecha_alta=datetime.now(),fecha_baja=None) -> None:
        self.id = id
        self.identificador = identificador
        self.ubicacion = ubicacion
        self.latitud = latitud
        self.longitud = longitud
        self.conexiones_max = conexiones_max
        self.conexiones = ListaEnlazada() # Usamos lista enlazada ya que no sabemos cuando y en que orden se va a desconectar el dispositivo. Se podria usar un dict por cada ip pero esto es mas liviano
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja # Si
        self.pais = pais
        self.ips = self.generar_todas_ips()
        
        
        departamento.routers[id] = self
    
    def __len__(self):
        return len(self.conexiones)

    def __str__(self) -> str:
        return str(self.id)

    def conectar(self,dispo:Dispositivo):
        if self.conexiones.len < self.conexiones_max:
            conexion = Conexion(dispo,self.generar_ip(),self,datetime.now())
            self.pais.conexiones.agregarnodo(NodoArbol(conexion))
            self.conexiones.append(conexion)
        else:
            raise ValueError()
    def generar_todas_ips(self)->set:
        st = set()
        for i in range(self.conexiones_max):
            st.add(f'192.168.68.{str(i).rjust(2,"0")}')
        return st
    def generar_ip(self)->str: # Revisamos todos los elementos de la lista hasta que conseguimos una IP libre
        #revisamos la lista de conexiones hasta encontrar una ip libre

        ip = self.ips.pop()
        
        return ip

    def desconectar(self,dispo:Dispositivo):
        dato = self.conexiones.delete_node(dispo)
        self.ips.add(dato.ip)
        dato.baja = datetime.now()
        

import datetime

class NodoArbol:
    #constructor
    def __init__(self,dato=None):
        self.dato=dato
        self.derecho=None
        self.izquierdo=None

    def agregarnodos(self,nodo):

        if self.dato<nodo.dato:
            if self.derecho==None:
                self.derecho=nodo
            else:
                NodoArbol.agregarnodos(self.derecho,nodo)
        elif self.dato>nodo.dato:
            print('der2')
            if self.izquierdo==None:
                print('izq')
                self.izquierdo=nodo
            else:
                NodoArbol.agregarnodos(self.izquierdo,nodo)


class Arbol:
    def __init__(self,nodo=None):
        self.root=nodo
    
    # Mostrar el Arbol en preorden
    def preorder(self,nodo=None):
        try:
            nodo = self.root if nodo == 'root' else nodo
        except AttributeError:
            pass
        if nodo:
            print(nodo.dato)
            Arbol.preorder(nodo.izquierdo)
            Arbol.preorder(nodo.derecho)
    
    # Mostrar el Arbol en inorden
    def inorder(self,nodo=None):
        try:
            nodo = self.root if nodo == 'root' else nodo
        except AttributeError:
            pass
        if(nodo):
            Arbol.inorder(nodo.izquierdo)
            print(nodo.dato)
            Arbol.inorder(nodo.derecho)

    # Mostrar el Arbol en postorden
    def posorden(self,nodo=None):
        try:
            nodo = self.root if nodo == None else nodo
        except AttributeError:
            pass
        if nodo:
            Arbol.posorden(nodo.izquierdo)
            Arbol.posorden(nodo.derecho)
            print(nodo.dato)

    # agregar al Arbol
    def agregarnodo(self,nodo):
        if self.root==None:
            self.root=nodo
        else:
            self.root.agregarnodos(nodo) 

    def fechaLimites(self, fecha_inf: datetime,fecha_sup:datetime, nodo: NodoArbol = None) -> list:  
        nodo = self.root if nodo == None else nodo
        lista=[]
        if nodo.dato >= fecha_inf:
            if (
                nodo.dato > fecha_inf and nodo.izquierdo
            ):  # Es para evitar que recorra para la izquierda si el arbol tiene mas valores
                lista.extend(self.fechaLimites(fecha_inf,fecha_sup, nodo.izquierdo))
            lista.append(nodo.dato)

            if nodo.dato < fecha_sup and nodo.derecho:
                lista.extend(self.fechaLimites(fecha_inf,fecha_sup, nodo.derecho))
        return lista
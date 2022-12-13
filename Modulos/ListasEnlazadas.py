class Nodo():
  def __init__(self,dato=None,prox=None):
    self.dato=dato
    self.prox=prox
  def __str__(self):
    return str(self.dato)

class ListaEnlazada():
  def __init__(self):
    self.headvalue = None
    self.len = 0

  def __len__(self):
    return self.len

  def append(self,dato):
    nodo_dato = Nodo(dato)
    if self.len == 0:
      self.headvalue = nodo_dato
    else:
      recorrido = self.headvalue
      for i in  range(self.len-1):
        recorrido = recorrido.prox
      recorrido.prox = nodo_dato
    self.len += 1 

  def extend(self,conjunto):
    for elemento in conjunto:
      self.append(elemento)

  def construir_diccionario(dic):
    L = ListaEnlazada()
    for (clave,valor) in dict:
      L.append(valor)
    return L

# ingresar un nodo a la lista por referencia --> el valor de un dato en 
# la lista introducir un nuevo nodo inmediatamente después del anterior

  def insert_despues_de(self,valor_antes,valor_despues): #pos --> hasta una posicion 
    #i = 0
    actual = self.headvalue
    while (actual!=None and (actual.dato != valor_antes)): #or i<pos:
      actual= actual.prox
      #i += 1 
    if actual != None:
      nuevo_nodo = Nodo(valor_despues)
      nuevo_nodo.prox = actual.prox
      actual.prox = nuevo_nodo

#ingresar un nodo a la lista despues de una posicion determinada 

  def agregardspposicion(self,posicion,nodo:Nodo):
    nodomov = self.headvalue
    posmov = 0
    while posmov < posicion:
      nodomov = nodomov.prox
      posmov += 1
    nodo.prox = nodomov.prox
    nodomov.prox = nodo
    self.len += 1

#obtener el valor de un nodo de una determinada posición en la lista

  def get(self,posicion):
    if posicion >= self.len:
      return None
    i = 0
    actual = self.headvalue
    while (i<posicion):
      actual = actual.prox 
      i += 1
    return actual.dato

  def print_list(self):
      node = self.headvalue
      while node != None:
        print(node.dato, end =" => ")
        node = node.prox
      print("None")

#Unir listas 
  def unir_listas(self,lista1,lista2):
    if len(lista1) < len(lista2):
      lista1,lista2 = lista2,lista1 #lista1 va a ser la mas larga
    for i in range(len(lista1)):
      self.append(lista1[i])
      try:
        self.append(lista2[i])
      except IndexError:
        pass

#eliminar nodos con posiciones pares
  def eliminar_pares(self,lista):
    for i in range(len(lista)):
      if i % 2 != 0:
        self.append(lista[i])

  # Método para agregar elementos en el frente 
  def add_at_front(self, data):
      self.head = Nodo(data=data, prox=self.headvalue)

    # Método para verificar si la estructura de datos esta vacia
  def is_empty(self):
    return self.headvalue == None

    # Método para agregar elementos al final 
  def add_at_end(self, data):
    if not self.headvalue:
      self.head = Nodo(data=data)
      return
    actual = self.headvalue
    while actual.prox:
      actual = actual.prox
    actual.prox = Nodo(data=data)

  # Método para eleminar nodos
  def delete_node(self, valor):
    actual = self.headvalue
    prev = None
    while actual and actual.dato != valor:
        prev = actual
        actual = actual.prox
    if prev is None:
        self.headvalue = actual.prox
    elif actual:
        prev.prox = actual.prox
        actual.prox = None
    return actual.dato

    # Método para obtener el ultimo nodo
  def get_last_node(self):
    temp = self.headvalue
    while (temp.prox is not None):
        temp = temp.prox
    return temp.dato

  def __iter__(self):
    return LinkedListIterator(self.headvalue)


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.dato
            self.current = self.current.prox
            return item


if __name__ == '__main__':
  listita = ListaEnlazada()
  listita.append(5)
  listita.append(4)
  listita.append(2)
  listita.append(7)
  listita.append(4)
  # listita.insert_despues_de(4,6)
  # listita.print_list()

  # lista=[1,2,4,6,10,100,3,8,0,123]
  # lista2=[3,8,0,123]

  # lista_final = ListaEnlazada()
  # lista_final.unir_listas(lista,lista2)
  # lista_final.print_list()


  lista=[1,2,4,6,10,100,3,8,0,123]
  listota = ListaEnlazada()
  listota.eliminar_pares(lista)
  listota.print_list()
  for i in listota:
    print(i)
import pickle
from Modulos.clases import Pais
with open('archivo.pickle','rb') as arch:
    arg = pickle.load(arch)

print(arg.poblacion)
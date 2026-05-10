import random
from models.soldier import Soldier

class node:
    def __init__(condicion,accion,hijos = []):
        self.condicion = condicion
        self.accion = accion
        self.hijos = hijos
    
    def setHijos(self,hijo):
        self.hijos.append(hijo)

def generarCerebro():
    #g0
    g0 = node(True,None)
    #g1
    g1A = node(Soldier.tieneBlindaje,)


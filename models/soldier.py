import random
import math
class Soldier:
    def __init__(self,modelo="🧑‍🦱"):
        self.modelo = modelo
        self.shock = 0
        self.vHead = 100
        self.vArms = 100
        self.vChest = 100
        self.vLegs = 100
        self.bHead = 0
        self.bArms = 0
        self.bChest = 0
        self.bLegs = 0
        self.movimiento = 5
        self.velocidad = 100
        self.arma = None
        self.blindaje = None
        self.cerebro = None
        self.posX = 0
        self.posY = 0

    def spawn(mapa, posicion):
        self.posX = random.randint(0,len(mapa[0]))
        if posicion == "arriba":
            self.posY = random.randint(0,1)
        else:
            self.posY = random.randint(len(mapa)-1,len(mapa))

    def equiparArma(self,arma):
        self.arma = arma
        self.movimiento += arma.factorMovimiento
        self.velocidad += factorVelocidad

    def equiparBlindaje(self,blindaje):
        self.bHead += blindaje.pHead
        self.bArms += blindaje.pArms
        self.bChest += blindaje.pChest
        self.bLegs += blindaje.pLegs
    
    def moverse(self,x,y,mapa):
        while ((x!=self.posX)and(y!=self.posY)):
            if(x < self.posX):
                self.posX -= 1
            elif(x>self.posX):
                self.posX += 1
            if(y<self.posY):
                self.posY -=1
            elif(y>self.posY):
                self.posY +=1
    
    def tieneBlindaje(self):
        if self.blindaje != None:
            return True
        else:
            return False
    
    def buscarBlindaje(self,mapa):
        cercania = 9999
        ubicacionX = 0
        ubicacionY = 0
        for y in range(len(mapa)):
            for x in range((len(mapa[y]))):
                if(mapa[y][x] == g):
                    distancia = math.sqrt(((x-self.posX)**2)+((y-self.posY)**2))
                    if distancia < cercania:
                        cercania = distancia
                        ubicacionX = x
                        ubicacionY = y
        
        self.moverse(ubicacionX,ubicacionY,mapa)
        






    

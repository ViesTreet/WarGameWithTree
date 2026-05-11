import random
import math
class Soldier:
    def __init__(self,modelo="🧑"):
        self.modelo = modelo
        self.shock = 0#a
        self.vHead = 100#b
        self.vArms = 100#c
        self.vChest = 100#d
        self.vLegs = 100#e
        self.bHead = 0#f
        self.bArms = 0#g
        self.bChest = 0#h
        self.bLegs = 0#i
        self.movimiento = 5#j
        self.velocidad = 100#k
        self.arma = None#l
        self.blindaje = None#m
        self.posX = 0#n
        self.posY = 0#n

    def spawn(self,mapa, posicion):
        self.posX = random.randint(0,len(mapa[0]))
        if posicion == "arriba":
            self.posY = random.randint(0,1)
        else:
            self.posY = random.randint(len(mapa)-1,len(mapa))
        mapa[self.posY][self.posX-1]=self.modelo
        return mapa

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

    def buscarAlgo(self,mapa,objeto):
        cercania = 9999
        ubicacionX = 0
        ubicacionY = 0
        for y in range(len(mapa)):
            for x in range((len(mapa[y]))):
                if(mapa[y][x] == objeto):
                    distancia = math.sqrt(((x-self.posX)**2)+((y-self.posY)**2))
                    if distancia < cercania:
                        cercania = distancia
                        ubicacionX = x
                        ubicacionY = y
        return cercania,ubicacionX,ubicacionY

    #Cerebro
    def pensar(self,pesos):
        a = pesos[0]
        b = pesos[1]
        c = pesos[2]
        d = pesos[3]
        e = pesos[4]
        f = pesos[5]
        g = pesos[6]
        h = pesos[7]
        i = pesos[8]
        j = pesos[9]
        k = pesos[10]
        l = pesos[11]
        m = pesos[12]
        n = pesos[13]
        decisiones = []
        rendirse = (self.shock*a)-(self.vHead*b)-(self.vArms*c)-(self.bChest*d)-(self.vLegs*e)
        decisiones.append(["rendirse",rendirse])
        if self.arma == None:
            estadoArma = 1
        else:
            estadoArma = 0
        buscarArma = (estadoArma*l)
        decisiones.append(["buscarArma",buscarArma])
        if self.blindaje == None:
            estadoBlindaje = 1
        else:
            estadoBlindaje = 0
        buscarBlindaje = (estadoBlindaje*m)
        decisiones.append(["buscarBlindaje",buscarBlindaje])
        decisionFinal = sorted(decisiones, key=lambda x:x[1],reverse=True)
        print(decisionFinal)
        return decisionFinal[0][0]




        






    

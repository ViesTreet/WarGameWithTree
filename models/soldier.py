import random
import math
import models.arma
import models.blindaje
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
        self.status = None

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
        if ((x!=self.posX)and(y!=self.posY)):
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
    
    def medirDistancia(self,enemigo):
        distancia = (sqrt(((self.posX-enemigo.posX)**2)+((self.posY-enemigo.posY)**2)))
        posicionX = enemigo.posX
        posicionY = enemigo.posY
        if (self.arma.alcance >= distancia):
            rango = True
        else:
            rango = False

        return distancia, rango, posicionX, posicionY


    #Cerebro
    def pensar(self,pesos,mapa,enemigos = []):
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
        if self.arma != None:
            for enemigo in enemigos:
                
                    cercania,uX,uY=self.buscarAlgo(mapa,enemigo.modelo)
                    if(self.arma.alcance >= cercania):
                        atacar = (estadoBlindaje*m)+(estadoArma*l)-(self.shock*a)
                        decisionFinal.append([f"atacarA{self.modelo}",atacar])


        decisionFinal = sorted(decisiones, key=lambda x:x[1],reverse=True)
        print(decisionFinal)
        self.actuar(decisionFinal[0][0],mapa,enemigos)

    def disparar(self, enemigo):
        # 1. Cálculo de distancia y probabilidad
        distancia = sqrt(((self.posX - enemigo.posX)**2) + ((self.posY - enemigo.posY)**2))
        
        # Ajuste: En un mapa de 8x10, la distancia max es ~12.8. 
        # Mantengo tu fórmula pero con cuidado de no hacerla imposible.
        probabilidadAcertar = 0.80 - ((distancia / 100) * 1.1)
        
        if random.uniform(0, 1) <= probabilidadAcertar:
            partes = ["head", "chest", "legs", "arms"]
            impactada = random.choice(partes)
            
            # 2. Verificación de Perforación (Tier)
            # Si el enemigo tiene blindaje y el tier es mayor al que el arma puede perforar
            if enemigo.blindaje and enemigo.blindaje.tier > self.arma.tierMaxBlind:
                print(f"¡EL IMPACTO EN {impactada.upper()} REBOTÓ! El blindaje es demasiado resistente.")
                # Aplicamos un shock mínimo por el golpe cinético incluso si no perfora
                enemigo.shock += (self.arma.dano * 0.1) 
                return

            # 3. Cálculo de Daño por zona (Usando el factor de reducción)
            # Si no tiene blindaje, la reducción es 0
            reduccion = 0
            if enemigo.blindaje:
                reduccion = getattr(enemigo.blindaje, impactada, 0)

            # Daño base ajustado por la protección (1 - reduccion)
            # 1.0 de reducción = 0 daño | 0.4 de reducción = 0.6 daño recibido
            danio_final = self.arma.dano * (1 - reduccion)

            match impactada:
                case "head":
                    # Multiplicador crítico por ser cabeza
                    danio_final *= 2 
                    enemigo.vHead -= danio_final
                    if enemigo.vHead <= 0:
                        enemigo.status = "muerto"
                        print("¡Headshot! Enemigo eliminado.")
                
                case "chest":
                    enemigo.vChest -= danio_final
                    if enemigo.vChest <= 0:
                        enemigo.status = "muerto"
                        print("Impacto letal en el torso.")
                
                case "legs":
                    enemigo.vLegs -= danio_final
                    # El daño en piernas afecta el movimiento
                    enemigo.movimiento = max(1, enemigo.movimiento - 1)
                
                case "arms":
                    enemigo.vArms -= danio_final
                    # El daño en brazos podría afectar la puntería (opcional)
            
            # 4. Sistema de Shock
            # El shock aumenta proporcionalmente al daño recibido
            # Si el daño es 50, el shock sube 25 puntos.
            factor_shock = 0.5 
            enemigo.shock += (danio_final * factor_shock)
            
            print(f"¡Impacto en {impactada}! Daño: {round(danio_final, 1)}. Shock total: {round(enemigo.shock, 1)}")

        else:
            print("¡Disparo fallido!")

        def actuar(self,decision,mapa,enemigos):
            if "atacarA" in decision:
                objetivo = decision.replace("atacarA","")
                decision = "atacar"
            match decision:
                case "rendirse":
                    self.status = rendido
                case "buscarArma":
                    _,ubX,UbiY=self.buscarAlgo(mapa,"A")
                    if((ubX == self.posX)and(UbiY==self.posY)):
                        self.arma = arma.seleccionRandomArmas()
                    else:
                        self.moverse(ubX,UbiY,mapa)
                case "buscarBlindaje":
                    _,ubX,UbiY=self.buscarAlgo(mapa,"B")
                    if((ubX == self.posX)and(UbiY==self.posY)):
                        self.arma = blindaje.blindajeAleatorio()
                    else:
                        self.moverse(ubX,UbiY,mapa)
                case "atacar":
                    for enemigo in enemigos:
                        if enemigo.modelo == objetivo:
                            self.disparar(enemigo)
        

                
            

                




        






    

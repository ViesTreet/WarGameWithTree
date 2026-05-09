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

    def equiparArma(arma):
        self.arma = arma
        self.movimiento += arma.factorMovimiento
        self.velocidad += factorVelocidad

    def equiparBlindaje(blindaje):
        self.bHead += blindaje.pHead
        self.bArms += blindaje.pArms
        self.bChest += blindaje.pChest
        self.bLegs += blindaje.pLegs



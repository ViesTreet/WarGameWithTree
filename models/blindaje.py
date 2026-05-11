import random
class Blindaje:
    def __init__(self,tier,chest=0,head=0,legs=0,arms=0):
        self.tier = tier
        self.chest = chest
        self.head = head
        self.legs = legs
        self.arms = arms

def blindajeAleatorio():
    lista_blindajes = [
        # Tier 1: Protecciones ligeras o civiles
        # Solo pecho, protección mínima
        Blindaje(tier=1, chest=0.4), 
        
        # Tier 2: Chalecos policiales estándar
        # Protege bien el pecho y un poco las extremidades (hombros/brazos)
        Blindaje(tier=2, chest=0.6, arms=0.2),
        
        # Tier 3: Equipo táctico de fuerzas especiales
        # Incluye casco ligero y protección en pecho
        Blindaje(tier=3, chest=0.75, head=0.5, arms=0.3),
        
        # Tier 4: Armadura completa de soldado
        # Placas cerámicas pesadas, casco reforzado y rodilleras/coderas
        Blindaje(tier=4, chest=0.9, head=0.8, arms=0.5, legs=0.5),
        
        # Tier 5: Equipo de Juggernaut / Desactivación de explosivos
        # Máxima protección en todo el cuerpo, casi impenetrable
        Blindaje(tier=5, chest=0.95, head=0.9, arms=0.8, legs=0.8)
    ]
    blindajeselect = random.choice(lista_blindajes)
    return blindajeselect
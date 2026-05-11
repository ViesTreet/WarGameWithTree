import random
class Arma:
    def __init__(self,nombre,calibre,dano,alcance,tierMaxBlind):
        self.nombre = nombre
        self.calibre = calibre
        self.dano = dano
        self.alcance = alcance


def seleccionRandomArmas():
    lista_armas = [
        # --- Pistolas (Tier Máximo 2: No atraviesan blindaje militar) ---
        Arma("Glock 17", "9mm", 35, 4, 2),
        Arma("Colt M1911", ".45 ACP", 45, 3, 2),
        Arma("Beretta M9", "9mm", 32, 4, 2),
        Arma("Sig Sauer P226", "9mm", 34, 4, 2),
        Arma("Desert Eagle", ".50 AE", 85, 3, 3), # El .50 tiene más pegada
        
        # --- Subfusiles (Tier Máximo 2: Mucha cadencia, poca penetración) ---
        Arma("MP5", "9mm", 30, 5, 2),
        Arma("P90", "5.7mm", 28, 6, 3), # El 5.7mm es famoso por perforar blindaje
        Arma("UZI", "9mm", 25, 3, 2),
        Arma("Vector", ".45 ACP", 38, 4, 2),
        
        # --- Fusiles de Asalto (Tier Máximo 4: Diseñados para combate militar) ---
        Arma("AK-47", "7.62mm", 55, 7, 4),
        Arma("M4A1", "5.56mm", 48, 8, 4),
        Arma("SCAR-H", "7.62mm", 60, 7, 4),
        Arma("HK416", "5.56mm", 50, 8, 4),
        Arma("AUG", "5.56mm", 45, 7, 4),
        
        # --- Escopetas (Tier Máximo 2: Mucha masa, pero se detienen fácil) ---
        Arma("Remington 870", "12 gauge", 90, 2, 2),
        Arma("Mossberg 500", "12 gauge", 85, 2, 2),
        
        # --- Rifles de Precisión (Tier Máximo 5: Perforan todo) ---
        Arma("AWM", ".338 Lapua", 100, 10, 5),
        Arma("Barrett M82", ".50 BMG", 150, 10, 5),
        Arma("M24", "7.62mm", 80, 9, 4),
        Arma("Dragunov SVD", "7.62mm", 75, 8, 4)
    ]
    return random.choice(lista_armas)
from models.soldier import Soldier
# Matriz de 8 filas x 10 columnas
# Equipo A: Filas 0 y 1
# Equipo B: Filas 6 y 7
# 0: Espacio vacío

mapa1 = [
    ["A", "A", 0, "A", 0, 0, "A", "A", 0, "A"], # Fila 0 (Spawn A)
    [0, "A", "A", 0, 0, "A", 0, 0, "A", 0],     # Fila 1 (Spawn A)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],             # Fila 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],             # Fila 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],             # Fila 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],             # Fila 5
    [0, "B", 0, 0, "B", "B", 0, 0, "B", 0],     # Fila 6 (Spawn B)
    ["B", 0, "B", "B", 0, 0, "B", "B", 0, "B"]  # Fila 7 (Spawn B)
]

soldado = Soldier()
enemigo = Soldier()
with open("guardado.txt","w")as file:
    

mapa1=soldado.spawn(mapa1,"arriba")
mapa1= enemigo.spawn(mapa1,"abajo")
for z in range(len(mapa1)):
    print(mapa1[z])
for x in range(20):
    soldado.pensar()

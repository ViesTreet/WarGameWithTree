from models.soldier import Soldier
mapa1 = [
    ["A",0,0,"A",0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ["A","A",0,0,0,0,0,0]
]

soldado = Soldier()
mapa1=soldado.spawn(mapa1,"arriba")
for z in range(len(mapa1)):
    print(mapa1[z])
distancia,X,Y = soldado.buscarAlgo(mapa1,"A")
print(distancia,X,Y)
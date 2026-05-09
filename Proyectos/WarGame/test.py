import os
import neat
import random
import time

# Configuración del mapa (Igual que antes)
MAPA_TAMANO = 10
ACCIONES = ['Arriba', 'Abajo', 'Derecha', 'Izquierda']
MOVIMIENTOS = {'Arriba': (0,1), 'Abajo': (0,-1), 'Derecha': (1,0), 'Izquierda': (-1,0)}

TESORO = (8, 8)
INICIO = (1, 1)

def get_intensidad(x, y):
    if not (0 <= x < MAPA_TAMANO and 0 <= y < MAPA_TAMANO): return 0
    if (x, y) == TESORO: return 3
    d = abs(TESORO[0]-x) + abs(TESORO[1]-y)
    if d <= 2: return 2 # Carbón Fuerte
    if d <= 5: return 1 # Carbón Débil
    return 0

def evaluar_genoma(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        x, y = INICIO
        camino = set([(x, y)])
        fitness_acumulado = 0
        choques = 0
        dist_minima = 20
        
        for _ in range(40): # Pasos máximos
            # Entradas: 5 sensores de intensidad
            inputs = [
                get_intensidad(x, y) / 3,
                get_intensidad(x, y+1) / 3,
                get_intensidad(x, y-1) / 3,
                get_intensidad(x-1, y) / 3,
                get_intensidad(x+1, y) / 3
            ]
            
            output = net.activate(inputs)
            idx_acc = output.index(max(output))
            acc = ACCIONES[idx_acc]
            
            dx, dy = MOVIMIENTOS[acc]
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < MAPA_TAMANO and 0 <= ny < MAPA_TAMANO:
                x, y = nx, ny
                if (x, y) not in camino:
                    fitness_acumulado += 10 # Premio por explorar
                camino.add((x, y))
            else:
                choques += 1
                fitness_acumulado -= 20 # Castigo por chocar
            
            d_actual = abs(TESORO[0]-x) + abs(TESORO[1]-y)
            dist_minima = min(dist_minima, d_actual)
            
            if (x, y) == TESORO:
                fitness_acumulado += 2000
                break
        
        # Fitness final: Exploración - Choques + Bonus por cercanía
        genome.fitness = fitness_acumulado + (1000 / (dist_minima + 1))

def run_neat(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    p = neat.Population(config)

    # Añadimos reporteros para ver el progreso en consola
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Entrenar por 100 generaciones
    winner = p.run(evaluar_genoma, 100)

    print('\n¡Mejor genoma encontrado!')
    # Aquí podrías guardar el 'winner' con pickle si quisieras
    return winner

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run_neat(config_path)
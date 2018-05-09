from utils import extract_min, distancia_manhattan, define_caminho
import math

def bfs (g, inicio, fim, img):
    grafo = g.graph

    node = inicio
    
    if (fim == inicio):
        return node

    pai = [-1] * (g.height * g.width)

    distancias = [-1] * (g.height * g.width)
    distancias[inicio] = 0

    possivel_distancia = [-1] * (g.height * g.width)
    possivel_distancia[0] = 0

    fronteira = []
    fronteira.append(node)

    explorado = []
    while (len(fronteira) != 0):
        node = fronteira.pop(extract_min(grafo, fronteira, possivel_distancia))

        # pos_y = node % g.width
        # pos_x = math.floor(node / g.width)
        # img.putpixel( (  pos_y, pos_x ), (255,0,0) )

        if (node == fim):
            caminho = define_caminho(fim, pai, inicio)
            
            return caminho
        
        explorado.append(node)

        for filho in grafo[node]:
            nova_possivel_distancia = distancias[node] + distancia_manhattan (g, filho, fim)
            if ((filho not in explorado) and (filho not in fronteira)):
                if (grafo[node][filho] != 1.5):
                    fronteira.append(filho)
                    pai[filho] = node
                    distancias[filho] = distancias[node]
                    possivel_distancia[filho] = nova_possivel_distancia
            elif ((filho in fronteira) and ( possivel_distancia[filho] > nova_possivel_distancia )  ):
                pai[filho] = node
                distancias[filho] = distancias[node]
                possivel_distancia[filho] = nova_possivel_distancia
from utils import extract_min, define_caminho
import math

def ucs (g, inicio, fim, img):
    grafo = g.graph

    node = inicio
    
    if (fim == inicio):
        return node

    pai = [-1] * (g.height * g.width)

    distancias = [-1] * (g.height * g.width)
    distancias[inicio] = 0

    fronteira = []
    fronteira.append(node)

    explorado = []
    while (len(fronteira) != 0):
        node = fronteira.pop(extract_min(grafo, fronteira, distancias))


        # pos_y = node % g.width
        # pos_x = math.floor(node / g.width)
        # img.putpixel( (  pos_y, pos_x ), (255,0,0) )


        if (node == fim):
            caminho = define_caminho(fim, pai, inicio)
            
            return caminho
        
        explorado.append(node)

        for filho in grafo[node]:
            if ((filho not in explorado) and (filho not in fronteira)):
                fronteira.append(filho)
                pai[filho] = node
                distancias[filho] = distancias[node] + grafo[node][filho]
            elif ((filho in fronteira) and ( distancias[filho] > distancias[node] + grafo[node][filho] )  ):
                pai[filho] = node
                distancias[filho] = distancias[node] + grafo[node][filho]
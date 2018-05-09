import math
from PIL import Image

def extract_min (grafo, fronteira, distancias):
    dist_minima = distancias[fronteira[0]]
    i_dist_minima = 0
    for i in range(0, len(fronteira)):
        if (distancias[fronteira[i]] < dist_minima):
            dist_minima = distancias[fronteira[i]]
            i_dist_minima = i

    return i_dist_minima

def define_caminho (fim, pai, inicio):
    atual = fim
    caminho = []

    while (pai[atual] != -1):
        caminho.append(atual)
        atual = pai[atual]

    caminho.append(inicio)

    return caminho


def define_custo (g, caminho):
    grafo = g.graph
    lista_custos = [0]
    z = 0
    custo = 0

    for i in range(1, len(caminho)):
        vertice_proximo = caminho[i]
        vertice_atual = caminho[z]
        custo += grafo[vertice_atual][vertice_proximo]

        lista_custos.append(custo)
        
        z += 1
    
    return custo, lista_custos

def distancia_manhattan(g, node, goal):
    node_x = math.floor(node / g.width)    
    node_y = node % g.width
    
    goal_x = math.floor(goal / g.width)
    goal_y = goal % g.width

    return (math.fabs(node_x - goal_x) + math.fabs(goal_y - node_y))

def distancia_octille(g, node, goal):
    node_x = math.floor(node / g.width)    
    node_y = node % g.width
    
    goal_x = math.floor(goal / g.width)
    goal_y = goal % g.width

    dx = math.fabs(node_x - goal_x)
    dy = math.fabs(goal_y - node_y)

    return max(dx, dy) + 0.5 * min(dx, dy)


def escreve_output (caminho, g, img):
    caminho.reverse()
    custo_total, lista_custos = define_custo(g, caminho)

    print('<{0}, {1}, 0>'.format(caminho[0] % g.width, math.floor(caminho[0] / g.width)))
    print('<{0}, {1}, {2}>\n'.format(caminho[-1] % g.width, math.floor(caminho[-1] / g.width), custo_total))
    
    i = 0

    for vertice in caminho:
        pos_y = vertice % g.width
        pos_x = math.floor(vertice / g.width)

        # img.putpixel( (  pos_y, pos_x ), (255,128,0) )

        print('<{0}, {1}, {2}>'.format(pos_x, pos_y, lista_custos[i]), end='')

        if (i < len(lista_custos) - 1):
            print(end=' ')

        i += 1

    return img

def create_map_image (g):
    map_list = []
    for element in g.list:
        if (element == '@'):
            map_list.append(0)
        else:
            map_list.append((255,255,255))

    img = Image.new('RGB', (g.width, g.height))
    img.putdata(map_list)

    return img